# Trading Dashboard

![Python](https://img.shields.io/badge/Python-3.13-blue)
![Trading](https://img.shields.io/badge/Project-Trading-success)

**Created by SIMOEEEEX**

---

## Description

**Trading Dashboard** is a Python-based trading application for **crypto and forex markets**.

It uses:
- EMA (50 / 200)
- RSI
- Simple automated strategy
- Paper trading (virtual portfolio)

The project includes a **modern black GUI dashboard** with real-time charts and performance tracking.

---

## Features

- 📊 Live price data using **yfinance**
- 📈 Technical indicators: EMA & RSI
- 🤖 Automated BUY / SELL / HOLD signals
- 💼 Paper trading portfolio simulation
- 🖥️ Interactive Tkinter GUI
- 📉 RSI and price charts
- 🧾 Trade history tracking
- 🖤 Professional dark theme
- 🔻 Footer: *created by SIMOEEEEX*

---

## Supported Markets

- Crypto: `BTC-USD`, `ETH-USD`
- Forex: `EURUSD=X`, `GBPUSD=X`

> ⚠️ Indices are not supported by `yfinance`

---

## Strategy Logic

- **BUY**
  - EMA 50 > EMA 200
  - RSI < 30 (oversold)

- **SELL**
  - EMA 50 < EMA 200
  - RSI > 70 (overbought)

- Otherwise → **HOLD**

---

## Installation

1. Make sure Python 3 is installed  
2. Open terminal in the project folder

```bash
pip install -r requirements.txt
Run the dashboard:

bash
Copy code
python3 dashboard_gui.py
Project Structure
bash
Copy code
TradingDashboard/
│
├── dashboard_gui.py     # GUI dashboard
├── data_fetch.py        # Market data (yfinance)
├── indicators.py        # EMA & RSI
├── strategy.py          # Trading logic
├── portfolio.py         # Paper trading system
├── main.py
├── tests/
│   ├── test_data_fetch.py
│   ├── test_indicators.py
│   └── test_strategy.py
├── requirements.txt
└── README.md
Disclaimer
This project is for education and paper trading only.
Not financial advice.

Created by SIMOEEEEX
