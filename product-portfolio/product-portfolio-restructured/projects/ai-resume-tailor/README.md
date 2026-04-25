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

## Users
- Product managers applying to technical, AI, data, and platform roles
- Job seekers with multiple resume versions
- Career operators who need repeatable tailoring workflows

## Solution
I built a structured resume automation workflow using Python, a master DOCX template, section markers, and a two-step AI prompting process.

## Key Features
- Job description input by pasted text or URL scraping
- AI-powered job analysis before rewriting
- Section-bounded resume tailoring using template markers
- DOCX and PDF output
- Company-specific file naming
- Formatting preservation
- Guardrails to keep content truthful

## Technical Approach

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

## Supporting Artifacts
- [Sample Job Analysis](sanitized-examples/sample-job-analysis.md)
- [Sample Prompt Flow](sanitized-examples/sample-prompt-flow.md)
- [Architecture Diagram](diagrams/architecture.md)
- [Screenshot Notes](screenshots/screenshot-notes.md)
