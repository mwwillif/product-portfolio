# Bay Area Mortgage Calculator and Lead Generation Platform

## Type

Customer-facing web product | Mortgage calculator platform | Lead generation funnel

## Role

Product manager, product designer, funnel strategist, analytics designer, and builder

## Overview

The Bay Area Mortgage Calculator and Lead Generation Platform is a customer-facing website designed to help Bay Area homebuyers estimate affordability, monthly mortgage payments, and closing costs while generating high-intent mortgage leads.

The site combines useful financial calculators with a gated full-results experience. Users can view teaser results upfront and unlock detailed results by submitting contact information and consent.

## Problem

Mortgage shoppers often want quick answers before they are ready to speak with a lender. At the same time, lenders and mortgage professionals need better ways to identify high-intent buyers.

The problem had two sides:

For users:

- Mortgage costs are confusing.
- Affordability depends on many inputs.
- Closing costs are hard to estimate.
- Users want immediate value before talking to anyone.

For the business:

- Lead forms with no value exchange convert poorly.
- Mortgage leads need context, not just name and email.
- Campaign performance needs tracking.
- Lead source, calculator type, and user intent need to be captured.

## Users

Primary users:

- Bay Area homebuyers
- First-time buyers
- Mortgage shoppers comparing affordability
- Users trying to estimate closing costs before speaking with a lender

Business users:

- Mortgage professionals
- Lead buyers
- Sales teams
- Marketing operators

## Solution

I built a mortgage calculator site with multiple calculator experiences, lead capture, analytics tracking, and backend lead collection.

The product gives users a useful teaser result first, then gates the detailed breakdown behind a form. This creates a stronger value exchange and captures more context than a generic contact form.

## Key Features

### Affordability Calculator

Helps users estimate the home price range they may be able to afford based on income, debt, down payment, interest rate, and related assumptions.

### Mortgage Payment Calculator

Estimates monthly payment using home price, loan amount, interest rate, taxes, insurance, and other assumptions.

### Closing Cost Calculator

Estimates closing costs using lender fees, title and escrow fees, recording fees, transfer taxes, prepaid interest, prepaid taxes, and prepaid insurance.

### Lead-Gated Full Results

Users receive an initial teaser result. Full details are unlocked after form submission.

### Lead Capture Form

The form captures:

- First name
- Last name
- Phone
- Email
- Whether the user is already working with a lender
- Consent language
- Calculator type
- User intent fields
- UTM parameters
- User agent
- Referrer

### Google Sheets Backend

Lead submissions are sent to a Google Sheets backend through a Google Apps Script workflow.

### GA4 Event Tracking

The platform emits a conversion event only when the gate is actually passed.

Example event:

```text
lead_unlocked
```

Example parameter:

```text
calculator: affordability
```

### UTM Capture

The site captures source, medium, campaign, referrer, and user agent to support campaign measurement.

## Product Decisions

### Decision 1: Use calculators as the lead magnet

A calculator provides immediate user value. This is stronger than asking users to submit a form before seeing anything useful.

### Decision 2: Show teaser results before gating

Teaser results build trust and give users a reason to unlock the full breakdown.

### Decision 3: Track conversion only after the gate is passed

A conversion should represent real lead unlock behavior, not just a page view or button click.

### Decision 4: Use Google Sheets for the first backend

Google Sheets is simple, low-cost, fast to launch, and easy to inspect. It is appropriate for an early lead generation product before moving to a CRM.

### Decision 5: Capture detailed lead context

A lead with calculator inputs, intent fields, and source data is more valuable than a basic contact record.

## Technical Approach

High-level architecture:

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

## Tools and Technologies

- Framer
- JavaScript / React-style components
- Google Apps Script
- Google Sheets
- GA4
- UTM tracking
- Calculator logic
- Lead funnel design

## Impact

The product creates a practical lead generation funnel that offers real value before asking for contact information. It also creates better lead intelligence by capturing calculator type, user assumptions, campaign data, and conversion behavior.

## What I Would Improve Next

- Add CRM integration.
- Add lead scoring.
- Add lender matching.
- Add email follow-up automation.
- Add dashboard reporting for conversion rates by calculator type.
- Add A/B testing infrastructure for form fields and CTA copy.
- Add compliance review workflow for financial and TCPA language.

## Portfolio Note

This case study avoids publishing private lead records, contact information, campaign data, or backend endpoint details.
