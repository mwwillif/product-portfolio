# Public Sector Contract Search and Triage System

## Type
Procurement automation tool | Public-sector opportunity tracker | Data extraction workflow

## Role
Product manager, workflow designer, procurement operator, and builder

## Overview
The Public Sector Contract Search and Triage System is a Python-based workflow for monitoring public procurement opportunities, parsing bid event exports, normalizing opportunity data, and supporting triage for a small business contracting pipeline.

## Problem
Public-sector contracting opportunities are difficult to monitor manually. Bid portals contain many events, inconsistent formats, and changing opportunity details.

## Users
- Small business owner pursuing government contracts
- Government contracting operator
- Proposal support team
- Capture managers and procurement analysts

## Solution
I built a Python-based system to monitor procurement events, parse exported data, store opportunities in a local database, and support triage workflows.

## Key Features
- Bid opportunity scraping
- Export parsing
- SQLite storage
- Opportunity filtering
- Triage workflow
- Relevance scoring concept
- Local package tracking concept

## Technical Approach

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

## Supporting Artifacts
- [Sample Event Schema](sanitized-examples/sample-event-schema.sql)
- [Sample Opportunity Record](sanitized-examples/sample-opportunity-record.md)
- [Triage Workflow](sanitized-examples/triage-workflow.md)
- [Architecture Diagram](diagrams/architecture.md)
- [Screenshot Notes](screenshots/screenshot-notes.md)
