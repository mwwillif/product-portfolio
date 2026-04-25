# AI Resume Tailoring Engine

## Type

AI automation product | Document generation system | Career workflow tool

## Role

Product manager, workflow designer, prompt architect, and builder

## Overview

The AI Resume Tailoring Engine is a Python-based system that helps create tailored resumes for specific job descriptions while preserving formatting, truthfulness, and control over what sections can be rewritten.

The system uses a structured two-step AI workflow. First, it analyzes a job description to extract required skills, screening keywords, domain signals, preferred tools, and leadership expectations. Second, it uses that analysis to rewrite only approved sections of a master resume template.

## Problem

Tailoring a resume manually for each role is time-consuming, inconsistent, and easy to overdo. Generic AI resume tools can also create problems because they may rewrite too much, break formatting, invent experience, or weaken the candidate's strongest positioning.

The workflow needed to solve several issues:

- Job descriptions vary widely across companies and roles.
- Strong resumes need to align with recruiter, ATS, and AI screening signals.
- The resume must remain truthful and supported by real experience.
- Formatting must survive the tailoring process.
- Each output needs to be saved as a usable DOCX and PDF file.
- The system should support both pasted job descriptions and job URLs.

## Users

Primary user:

- A product manager applying to PM, technical PM, AI PM, data PM, and platform PM roles.

Secondary users:

- Career coaches
- Resume writers
- Job seekers with multiple resumes
- Professionals applying across adjacent domains

## Solution

I built a structured resume automation workflow using Python, a master DOCX template, section markers, and a two-step AI prompting process.

The system is designed to update only approved sections of the resume, such as summary, selected bullets, skills, and role-specific positioning. This prevents the AI from rewriting the entire document or damaging the formatting.

## Key Features

### Job Description Input

The system supports two methods:

- Paste a full job description directly into the program.
- Scrape a job description from a URL using browser automation.

### Job Analysis Step

Before tailoring the resume, the system analyzes the job description and extracts:

- Top required skills
- Screening keywords
- Domain signals
- Preferred tools
- Leadership expectations
- Product responsibilities
- Technical requirements
- Business context

### Section-Bounded Resume Tailoring

The master resume uses section markers such as:

- `[[SUMMARY_START]]`
- `[[SUMMARY_END]]`
- `[[SKILLS_START]]`
- `[[SKILLS_END]]`

Only marked sections are eligible for rewriting.

### Truthfulness Guardrails

The prompt is designed to optimize the resume without inventing experience. It must use the candidate's real background and experience pool.

### Formatting Preservation

The system uses a DOCX template and updates only targeted content areas so the resume keeps its original layout, spacing, and formatting.

### Output Generation

The system creates:

- A tailored DOCX resume
- A matching PDF version
- Company-specific file names, such as `Mete_Williford_Resume_CompanyName.docx`

## Product Decisions

### Decision 1: Use a two-step AI process

A single prompt can produce generic or weak results. A two-step process improves the output by forcing the AI to understand the job first, then tailor the resume with that understanding.

### Decision 2: Use section markers instead of full-document rewriting

Full-document rewriting creates formatting and truthfulness risks. Section markers create clear boundaries.

### Decision 3: Preserve a master template

The resume template acts as the controlled source of truth. This keeps the system repeatable and reduces formatting errors.

### Decision 4: Load prior resumes as an experience pool

Instead of relying on one static resume, the system can use a broader set of past resumes to identify relevant experience.

## Technical Approach

High-level architecture:

```text
Job Description Input
        |
        v
Job Analysis Prompt
        |
        v
Structured Job Analysis
        |
        v
Experience Pool + Master Resume Template
        |
        v
Section-Bounded Resume Tailoring Prompt
        |
        v
Updated DOCX Resume
        |
        v
PDF Export + Company-Specific File Name
```

## Tools and Technologies

- Python
- OpenAI API
- python-docx
- Playwright
- DOCX template markers
- PDF conversion workflow
- File naming automation

## Impact

The system creates a repeatable resume tailoring workflow that reduces manual rewriting time and improves consistency across applications. It also creates a stronger process for aligning resumes to specific job requirements without sacrificing accuracy or authenticity.

## What I Would Improve Next

- Add a web interface for uploading job descriptions and selecting target resume versions.
- Add scoring that compares the tailored resume against the job description.
- Add a dashboard showing keyword coverage and missing gaps.
- Add version history for each tailored resume.
- Add safer handling for company-specific job scrape failures.
- Add a review screen before final DOCX/PDF generation.

## Portfolio Note

This case study intentionally summarizes implementation details and avoids publishing private resumes, API keys, or sensitive personal information.
