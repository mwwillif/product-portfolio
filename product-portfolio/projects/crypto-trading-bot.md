# Automated Crypto Trading System

## Type

Financial automation system | Algorithmic trading workflow | Risk and monitoring tool

## Role

Product manager, system designer, strategy logic designer, and builder

## Overview

The Automated Crypto Trading System is a Python-based trading bot designed to ingest market data, calculate technical indicators, evaluate trade conditions, execute simulated or live trades, and log portfolio performance.

The system is best understood as a data-driven decision engine with risk controls, monitoring, and execution logic.

## Problem

Manual trading is difficult to scale because it requires constant monitoring, fast decision-making, consistent rules, and disciplined risk management.

The project was designed to solve several workflow problems:

- Continuously monitor crypto market data.
- Evaluate multiple technical indicators.
- Apply consistent entry and exit rules.
- Support long and short logic.
- Track balances, holdings, and portfolio value.
- Log decisions and skipped trades clearly.
- Support simulation before live execution.
- Reduce emotional decision-making.

## Users

Primary user:

- A technical product builder testing automated trading strategies.

Potential future users:

- Quant hobbyists
- Financial automation builders
- Traders who want structured rules and logging
- Product teams exploring risk-based automation

## Solution

I built a Python-based trading bot that connects market data, indicator calculations, strategy logic, trade execution, and logging into one automated loop.

The system can operate in simulation mode or live mode. It also includes portfolio tracking and detailed command-line output so decisions are explainable and debuggable.

## Key Features

### Market Data Ingestion

The bot retrieves market data and price information used to calculate indicators and evaluate trade conditions.

### Technical Indicator Logic

The system uses indicators such as:

- RSI
- MACD
- ATR
- Bollinger Bands
- DMI
- ADX
- Moving averages
- Volume ratio logic

### Long and Short Strategy Logic

The bot supports both long and short strategy paths, including entry and exit conditions.

### Risk Controls

Risk-related logic includes:

- Trade size calculation
- Stop-loss logic
- Trailing stop concepts
- Cooldown checks
- Open order validation
- Position duration tracking
- Stagnant trade detection

### Simulation Mode

Simulation mode allows the strategy logic to be tested without executing real trades.

### Portfolio Value Tracking

The system tracks portfolio value by combining cash balance and holdings valued in USD.

### Detailed Logging

The bot logs:

- Market data
- Balances
- Holdings
- Trade decisions
- Skipped trade reasons
- Executed trades
- Portfolio value
- PnL-related context

## Product Decisions

### Decision 1: Prioritize logging and explainability

Automated trading systems need transparency. A trade bot that makes decisions without clear logs is difficult to debug or trust.

### Decision 2: Support simulation before live execution

Simulation reduces risk and allows strategy testing before real capital is used.

### Decision 3: Use modular architecture

Separating configuration, authentication, fetching, trading, logging, and simulation logic makes the system easier to maintain.

### Decision 4: Include skipped trade reasons

Knowing why a trade did not happen is as important as knowing why a trade did happen.

### Decision 5: Treat portfolio value as a first-class metric

Portfolio value gives a clearer picture than cash balance alone because holdings must be included.

## Technical Approach

High-level architecture:

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

## Tools and Technologies

- Python
- Kraken API
- Yahoo Finance data concepts
- Pandas
- CSV logging
- Modular Python files
- Command-line monitoring

## Impact

The system created a repeatable decision workflow for evaluating trading conditions and managing risk-based automation. It also improved debugging by making trade decisions, skipped trades, balances, and portfolio value visible in logs.

## What I Would Improve Next

- Add a dashboard for portfolio and trade history.
- Add unit tests for indicator calculations.
- Add backtesting across historical data.
- Add stronger config validation.
- Add alerting for execution failures.
- Add cloud deployment option.
- Add database-backed trade history.
- Add strategy comparison reports.

## Portfolio Note

This case study intentionally avoids publishing API keys, private trading logic, account data, or any proprietary strategy details. It is presented as a technical product and automation case study, not as investment advice or a claim of trading performance.
