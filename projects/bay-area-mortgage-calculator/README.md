# Bay Area Mortgage Calculator and Lead Generation Platform

## Type
Customer-facing web product | Mortgage calculator platform | Lead generation funnel

## Role
Product manager, product designer, funnel strategist, analytics designer, and builder

## Overview
The Bay Area Mortgage Calculator and Lead Generation Platform is a customer-facing website designed to help Bay Area homebuyers estimate affordability, monthly mortgage payments, and closing costs while generating high-intent mortgage leads.

## Problem
Mortgage shoppers want quick answers before they are ready to speak with a lender. Lenders need better ways to identify high-intent buyers and understand the context behind each lead.

## Users
- Bay Area homebuyers
- First-time buyers
- Mortgage shoppers
- Mortgage professionals and lead operators

## Solution
I built a mortgage calculator site with multiple calculator experiences, lead capture, analytics tracking, and backend lead collection.

## Key Features
- Affordability calculator
- Mortgage payment calculator
- Closing cost calculator
- Lead-gated full results
- Google Sheets backend integration
- GA4 conversion tracking
- UTM capture

## Technical Approach

```text
User visits calculator page
        |
        v
User enters calculator inputs
        |
        v
Teaser result is displayed
        |
        v
User submits lead form with consent
        |
        v
Full result is unlocked
        |
        v
Lead data is sent to Google Apps Script
        |
        v
Google Sheets stores lead record
        |
        v
GA4 lead_unlocked event fires
```

## Supporting Artifacts
- [Lead Schema](sanitized-examples/lead-schema.md)
- [GA4 Events](sanitized-examples/ga4-events.md)
- [Calculator Inputs](sanitized-examples/calculator-inputs.md)
- [Architecture Diagram](diagrams/architecture.md)
- [Screenshot Notes](screenshots/screenshot-notes.md)
