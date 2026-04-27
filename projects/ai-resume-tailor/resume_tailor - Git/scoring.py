import re

def normalize_text(text: str) -> str:
    return re.sub(r"\s+", " ", text.lower()).strip()

def keyword_overlap_score(full_resume_text: str, keywords: list[str]) -> int:
    text = normalize_text(full_resume_text)
    if not keywords:
        return 0

    matched = 0
    for kw in keywords:
        if normalize_text(kw) in text:
            matched += 1

    return round((matched / len(keywords)) * 100)

def combine_scores(model_score: int, keyword_score: int) -> int:
    return round((model_score * 0.75) + (keyword_score * 0.25))