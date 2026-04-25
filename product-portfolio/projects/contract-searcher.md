# Public Sector Contract Search and Triage System

## Type

Procurement automation tool | Public-sector opportunity tracker | Data extraction workflow

## Role

Product manager, workflow designer, procurement operator, and builder

## Overview

The Public Sector Contract Search and Triage System is a Python-based workflow for monitoring public procurement opportunities, parsing bid event exports, normalizing opportunity data, and supporting triage for a small business contracting pipeline.

The system was designed to help identify relevant government opportunities more efficiently and reduce manual search effort.

## Problem

Public-sector contracting opportunities can be difficult to monitor manually. Bid portals contain many events, inconsistent formats, and changing opportunity details. For a small business, the challenge is not just finding opportunities, but quickly identifying which ones are relevant enough to pursue.

The workflow needed to solve several issues:

- Manual portal searches take time.
- Opportunity exports need parsing and normalization.
- Event IDs may have inconsistent formats.
- Relevant opportunities can be missed.
- Bid packages need to be tracked.
- Opportunities need triage and follow-up status.
- Errors need to be visible and recoverable.

## Users

Primary users:

- Small business owner pursuing government contracts
- Government contracting operator
- Proposal support team

Potential future users:

- Capture managers
- Procurement analysts
- Business development teams
- DVBE, SDVOSB, and small business contractors

## Solution

I built a Python-based system to monitor procurement events, parse exported data, store opportunities in a local database, and support triage workflows.

The system was designed around a daily monitoring workflow, with local storage and status fields to help track processing state.

## Key Features

### Bid Event Search

The system searches public procurement opportunities using target keywords and categories.

### Export Parsing

The workflow can process exported bid event files and normalize them into a more usable structure.

### SQLite Storage

Opportunities are stored in a local SQLite database for tracking and comparison across runs.

### Event Normalization

The system accounts for event IDs that are not always simple numeric values.

### Triage Workflow

Opportunities can be assigned processing statuses such as pending, processing, reviewed, or error.

### Package Tracking Concept

The system includes a concept for downloading or associating bid packages and related documents with each opportunity.

### Error Tracking

The workflow is designed to capture processing errors so issues can be diagnosed instead of silently failing.

## Product Decisions

### Decision 1: Use local database storage

A local SQLite database is simple, fast, and appropriate for an early-stage internal contracting workflow.

### Decision 2: Normalize event IDs flexibly

Event identifiers may include numbers, letters, dashes, or agency-specific formats. Strict numeric validation could drop real opportunities.

### Decision 3: Separate search, parsing, storage, and grading concepts

Breaking the workflow into stages makes the system easier to debug and improve.

### Decision 4: Treat triage as a workflow, not just a data table

The goal is not only to collect opportunities, but to help decide what to do next.

## Technical Approach

High-level architecture:

```text
Public procurement portal
        |
        v
Search and export workflow
        |
        v
Parse export or visible results
        |
        v
Normalize bid event data
        |
        v
Store in SQLite
        |
        v
Apply filters and triage status
        |
        v
Review opportunities and packages
```

## Tools and Technologies

- Python
- Playwright
- SQLite
- CSV / spreadsheet parsing
- Local file storage
- Procurement search workflows

## Impact

The system created a more structured way to monitor contracting opportunities and reduced reliance on manual portal searches. It also improved opportunity tracking by creating a persistent database and triage workflow.

## What I Would Improve Next

- Add a web dashboard for reviewing opportunities.
- Add email alerts for high-priority matches.
- Add automated document summarization.
- Add retry and backoff logic for rate limits.
- Add scoring by industry, NAICS, UNSPSC, deadlines, and contract fit.
- Add integration with a CRM or pipeline tracker.
- Add stronger package download management.

## Portfolio Note

This case study avoids publishing private business data, bid strategy, credentials, portal session details, or sensitive procurement information.
