# Trading Journal

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen)

**Created by SIMOEEEEX**

---

## Description

**Trading Journal** is a professional tool to track and analyze your trades.

It helps traders:
- Log trades with all details: symbol, side, lot, risk, RRR, and bias
- Track win rate, net profit, and risk/reward ratio
- See equity growth with charts
- Analyze profit distribution
- Improve trading strategy and discipline

---

## Features

- ✅ Log trades with symbol, side, lot, risk, RRR, bias
- ✅ Calculate win rate and net profit
- ✅ Calculate risk/reward ratio and max drawdown
- ✅ Equity curve chart
- ✅ Profit distribution chart
- ✅ Store trade history in CSV (`data/trades.csv`)
- ✅ Professional GUI in black theme
- ✅ Footer: "Created by SIMOEEEEX"

---

## Trade Data

Each trade stores:

- Date and time
- Symbol (BTCUSDT, EURUSD, US30, etc.)
- Side (BUY / SELL)
- Lot
- Strategy
- Bias (Bullish / Bearish / Neutral)
- Risked amount
- Profit

All trades are saved in:

data/trades.csv

yaml
Copy code

---

## Installation

1. Make sure **Python 3** is installed  
2. Clone the project:

```bash

cd TradingJournal
Install dependencies:

bash
Copy code
pip install -r requirements.txt
Run the app:

bash
Copy code
python3 main.py
Usage
Open the app

Fill in the trade details

Click Log Trade

View summary, equity curve, or profit distribution

Review stats to improve strategy

Project Structure
graphql
Copy code
TradingJournal/
│
├── main.py                # GUI and trade input
├── trade_logger.py        # Save trades to CSV
├── analyzer.py            # Analyze performance, win rate, drawdown
├── portfolio.py           # Virtual account logic
├── charts.py              # Equity and profit distribution charts
├── data/
│   └── trades.csv         # Trade history
├── tests/
│   ├── test_analyzer.py
│   └── test_trade_logger.py
├── requirements.txt
└── README.md
License
Free to use for learning and personal trading.

Created by SIMOEEEEX
