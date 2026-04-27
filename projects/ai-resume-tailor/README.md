# AI Resume Tailoring Engine

## Overview

The AI Resume Tailoring Engine is a Python-based tool I built to tailor resumes to specific job descriptions. It analyzes the job description, identifies the most important role requirements, and updates approved sections of a resume template while preserving structure and formatting.

The goal was to make resume tailoring faster, more consistent, and more targeted without relying on generic AI rewriting or manually editing the resume from scratch for every application.

## Problem

Tailoring a resume for each job is time-consuming and inconsistent. Generic AI tools often rewrite too much, break formatting, or add claims that are not supported by the candidate's actual experience.

I wanted a controlled workflow that could:

- Analyze a job description.
- Identify required skills and screening keywords.
- Use my actual experience as the source material.
- Rewrite only approved resume sections.
- Preserve the Word document structure.
- Export a clean final resume.

## Solution

I built a Python workflow that uses a master resume template, job description analysis, and controlled AI prompting to produce tailored resume drafts.

The system is designed around human review. It accelerates the tailoring process, but the final resume is still reviewed before submission.

## Key Features

- Job description intake.
- Job requirement analysis.
- AI-assisted resume tailoring.
- Section-bounded editing using template markers.
- Resume formatting preservation.
- DOCX output.
- PDF output.
- Company-specific file naming.
- Guardrails to avoid unsupported claims.

## How It Works

1. The user provides a job description.
2. The system analyzes the job description.
3. The system identifies required skills, keywords, and role priorities.
4. The system loads the master resume template and approved experience material.
5. The AI updates only approved sections.
6. The system creates a tailored DOCX file.
7. The system creates a matching PDF.
8. The user reviews the final output before applying.

## Product Decisions

### Controlled editing instead of full AI rewriting

I used template markers so the system only updates approved sections. This prevents the AI from changing employer names, dates, education, or other fixed resume content.

### Job analysis before tailoring

The system analyzes the job first, then uses that analysis to tailor the resume. This creates stronger alignment than asking the AI to rewrite the resume in one step.

### Human review remains part of the workflow

The system is designed to improve speed and consistency, not remove judgment. Every final resume still requires review before submission.

## Tools Used

- Python.
- OpenAI API.
- python-docx.
- Playwright.
- Word resume template.
- PDF export workflow.

## What This Demonstrates

This project demonstrates:

- AI workflow design.
- Prompt engineering.
- Product automation.
- Document generation.
- Workflow control.
- User-centered guardrail design.
- Practical use of AI for a real productivity problem.

## Sensitive Information Removed

This public version removes or sanitizes:

- Real resumes.
- Personal contact information.
- API keys.
- Private job application data.
- Full prompt details where sensitive.
- Any private file paths or credentials.
