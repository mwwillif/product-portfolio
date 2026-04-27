import os
import json
import re
from win32com.client import Dispatch
from config import ALLOWED_SECTIONS, TEMPLATE_FILENAME
from resume_parser import extract_template_sections, load_all_experience
from job_fetcher import fetch_job_description
from prompt_builder import build_job_analysis_messages, build_resume_messages
from openai_client import get_job_analysis, get_resume_updates
from docx_patcher import apply_updates


def validate_updates(updates: dict, allowed_sections: list):
    if "updates" not in updates:
        raise ValueError("Missing 'updates' in model response.")

    if not isinstance(updates["updates"], list):
        raise ValueError("'updates' must be a list.")

    seen_sections = set()

    for item in updates["updates"]:
        if not isinstance(item, dict):
            raise ValueError("Each update must be an object.")

        if "section_id" not in item or "content" not in item:
            raise ValueError("Each update must contain 'section_id' and 'content'.")

        section_id = item["section_id"]
        content = item["content"]

        if section_id not in allowed_sections:
            raise ValueError(f"Disallowed section returned: {section_id}")

        if section_id in seen_sections:
            raise ValueError(f"Duplicate section returned: {section_id}")
        seen_sections.add(section_id)

        if not isinstance(content, list):
            raise ValueError(f"Section content must be a list: {section_id}")

        if any(not isinstance(line, str) for line in content):
            raise ValueError(f"All content lines must be strings: {section_id}")

        if len(content) == 0:
            raise ValueError(f"Empty content returned for section: {section_id}")

        if section_id == "summary" and len(content) > 2:
            raise ValueError("Summary must return 1 or 2 lines max.")

        if section_id.endswith("_desc") and len(content) != 1:
            raise ValueError(f"{section_id} must return exactly 1 line.")

        if section_id.endswith("_bullets"):
            for line in content:
                if line.strip().startswith(("•", "-", "*")):
                    raise ValueError(f"{section_id} should not include bullet symbols.")

        if section_id.startswith("skills_"):
            if len(content) != 1:
                raise ValueError(f"{section_id} must return exactly 1 comma-separated line.")
            if ":" in content[0]:
                raise ValueError(f"{section_id} must not include labels like 'Tools:'.")


def export_docx_to_pdf(docx_path: str, pdf_path: str):
    word = Dispatch("Word.Application")
    word.Visible = False
    doc = None
    try:
        doc = word.Documents.Open(os.path.abspath(docx_path))
        doc.ExportAsFixedFormat(
            OutputFileName=os.path.abspath(pdf_path),
            ExportFormat=17,
            OpenAfterExport=False,
            OptimizeFor=0,
            CreateBookmarks=1
        )
    finally:
        if doc is not None:
            doc.Close(False)
        word.Quit()


def sanitize_filename(text: str) -> str:
    text = text.strip()
    text = re.sub(r'[<>:"/\\\\|?*]', "", text)
    text = re.sub(r"\s+", "_", text)
    text = re.sub(r"_+", "_", text)
    return text[:80].strip("_")


def extract_company_name(job_text: str, job_analysis: dict) -> str:
    # First try obvious company names in the job text
    company_patterns = [
        r"\bAt\s+([A-Z][A-Za-z&.\- ]{1,40})[, ]",
        r"\bJoin\s+([A-Z][A-Za-z&.\- ]{1,40})\b",
        r"\b([A-Z][A-Za-z&.\- ]{1,40})\s+delivers\b",
    ]

    for pattern in company_patterns:
        match = re.search(pattern, job_text)
        if match:
            candidate = match.group(1).strip()
            if len(candidate) > 1:
                return sanitize_filename(candidate)

    # Fall back to common known names if present
    known_companies = ["Ernst & Young", "Google", "Amazon", "Microsoft", "Meta", "Apple"]
    for company in known_companies:
        if company.lower() in job_text.lower():
            return sanitize_filename(company)

    # Final fallback
    return "Company"


def get_job_text():
    print("\nChoose job description input method:")
    print("1 = Paste job URL")
    print("2 = Paste full job description text")
    choice = input("Enter 1 or 2: ").strip()

    if choice == "1":
        job_url = input("Paste job URL: ").strip()
        if not job_url:
            raise ValueError("Job URL is required.")

        print("Fetching job description from URL...")
        job_text = fetch_job_description(job_url)

        if not job_text or len(job_text.strip()) < 500:
            raise ValueError(
                "Job description text looks too short.\n"
                "The page may be heavily JS-rendered or blocked.\n"
                "Use option 2 and paste the job description directly."
            )

        return job_text

    elif choice == "2":
        print("\nPaste full job description text below.")
        print("When finished, enter a line with only: END")
        lines = []

        while True:
            line = input()
            if line.strip() == "END":
                break
            lines.append(line)

        job_text = "\n".join(lines).strip()

        if not job_text or len(job_text) < 300:
            raise ValueError("Pasted job description text looks too short.")

        return job_text

    else:
        raise ValueError("Invalid option. Enter 1 or 2.")


def main():
    input_folder = "input"
    output_folder = "output"
    template_path = os.path.join(input_folder, TEMPLATE_FILENAME)

    os.makedirs(output_folder, exist_ok=True)

    if not os.path.exists(template_path):
        raise FileNotFoundError(
            f"Template not found: {template_path}\n"
            f"Make sure {TEMPLATE_FILENAME} is in the input folder."
        )

    print("Loading template...")
    template_sections = extract_template_sections(template_path)

    if not template_sections:
        raise ValueError(
            "No template sections were found.\n"
            "Check that your Master_Resume.docx contains the section markers."
        )

    print("Loading all experience...")
    full_experience = load_all_experience(input_folder, TEMPLATE_FILENAME)

    if not full_experience.strip():
        raise ValueError(
            "No source experience was found.\n"
            "Make sure you have other .docx resumes in the input folder besides Master_Resume.docx."
        )

    job_text = get_job_text()

    with open("debug_job_text.txt", "w", encoding="utf-8") as f:
        f.write(job_text)

    print("Saved job description text to debug_job_text.txt")

    print("Analyzing job...")
    job_analysis_messages = build_job_analysis_messages(job_text)
    job_analysis = get_job_analysis(job_analysis_messages)

    with open("debug_job_analysis.json", "w", encoding="utf-8") as f:
        json.dump(job_analysis, f, indent=2, ensure_ascii=False)

    print("Saved job analysis to debug_job_analysis.json")

    company_name = extract_company_name(job_text, job_analysis)
    base_filename = f"Mete_Williford_Resume_{company_name}"

    output_docx_path = os.path.join(output_folder, f"{base_filename}.docx")
    output_pdf_path = os.path.join(output_folder, f"{base_filename}.pdf")

    print(f"Output base filename: {base_filename}")

    print("Building resume prompt...")
    resume_messages = build_resume_messages(
        template_sections=template_sections,
        full_experience=full_experience,
        job_text=job_text,
        job_analysis=job_analysis,
        allowed_sections=ALLOWED_SECTIONS
    )

    with open("debug_prompt.json", "w", encoding="utf-8") as f:
        json.dump(resume_messages, f, indent=2, ensure_ascii=False)

    print("Saved resume prompt to debug_prompt.json")

    print("Calling OpenAI for resume rewrite...")
    updates = get_resume_updates(resume_messages)

    with open("debug_model_output.json", "w", encoding="utf-8") as f:
        json.dump(updates, f, indent=2, ensure_ascii=False)

    print("Saved model output to debug_model_output.json")

    print("Validating output...")
    validate_updates(updates, ALLOWED_SECTIONS)

    print("Applying updates to DOCX...")
    apply_updates(template_path, output_docx_path, updates)

    print("Exporting PDF...")
    export_docx_to_pdf(output_docx_path, output_pdf_path)

    print(f"\nDone DOCX -> {output_docx_path}")
    print(f"Done PDF  -> {output_pdf_path}")


if __name__ == "__main__":
    main()