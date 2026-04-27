# Diagram Flow

```text
Job Description Input
        |
        v
Job Description Extraction
        |
        v
AI Job Analysis
        |
        v
Structured Role Requirements
        |
        v
Master Resume Template + Approved Experience
        |
        v
Section-Bounded Resume Tailoring
        |
        v
DOCX Resume Output
        |
        v
PDF Export
        |
        v
Human Review
        |
        v
Final Resume for Application
```

## Workflow Explanation

The tool separates the process into three major stages.

### 1. Understand the job

The system first analyzes the job description and identifies the role type, required skills, keywords, domain signals, and likely screening priorities.

### 2. Tailor the resume

The system uses the job analysis and approved resume content to update only the resume sections that are allowed to change.

### 3. Generate the output

The system creates a tailored DOCX file and a matching PDF. The final output is reviewed before submission.

## Control Points

```text
Template markers control what can be changed.
Approved experience controls what the AI can use.
Human review controls the final submission.
```
