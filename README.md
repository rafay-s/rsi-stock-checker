This is my RSI Stock Checker

When it is completed, it will be a Flask web app that can check a stock's RSI (Relative Strength Index) and tells you if it's overbought, oversold, or neutral.

How it works:
Type any stock ticker, and the app pulls recent price data via yfinance, calculates RSI using Wilder's smoothing method, and displays the result.

Currently, to run this you must do it locally:
1. Clone the repo
2. Create a virtual environment and install requirements: `pip install -r requirements.txt`
3. Run `python app.py`
4. Visit `http://127.0.0.1:5000`

My planned features are:
- Telegram bot integration so users can get alerted automatically when a stock crosses overbought/oversold thresholds
- Live deployment (currently runs locally only)
