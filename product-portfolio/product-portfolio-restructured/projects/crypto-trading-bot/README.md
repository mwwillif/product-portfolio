# Automated Crypto Trading System

## Type
Financial automation system | Algorithmic trading workflow | Risk and monitoring tool

## Role
Product manager, system designer, strategy logic designer, and builder

## Overview
The Automated Crypto Trading System is a Python-based trading bot designed to ingest market data, calculate technical indicators, evaluate trade conditions, execute simulated or live trades, and log portfolio performance.

## Problem
Manual trading is difficult to scale because it requires constant monitoring, fast decision-making, consistent rules, and disciplined risk management.

## Users
- Technical product builder testing automated strategies
- Traders who want structured rules and logging
- Product teams exploring risk-based automation

## Solution
I built a Python-based trading bot that connects market data, indicator calculations, strategy logic, trade execution, and logging into one automated loop.

## Key Features
- Market data ingestion
- Indicator calculations
- Long and short strategy logic
- Risk controls
- Simulation mode
- Portfolio value tracking
- Detailed command-line logging
- Modular architecture

## Technical Approach

```text
Main trading loop
        |
        v
Fetch market data and balances
        |
        v
Calculate indicators
        |
        v
Evaluate long and short trade logic
        |
        v
Check risk controls and open positions
        |
        v
Execute simulated or live trade
        |
        v
Log market data, decision, trade, and portfolio value
```

## Supporting Artifacts
- [Sample CMD Output](sanitized-examples/sample-cmd-output.md)
- [Sample Trade Log](sanitized-examples/sample-trade-log.csv)
- [Risk Controls](sanitized-examples/risk-controls.md)
- [Architecture Diagram](diagrams/architecture.md)
- [Screenshot Notes](screenshots/screenshot-notes.md)
