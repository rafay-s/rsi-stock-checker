import yfinance as yf

def calculate_rsi(ticker, period=14):
    stock = yf.Ticker(ticker)
    data = stock.history(period = "3mo")

    if data.empty:
        raise ValueError("No data found for the given ticker. Perhaps you mispelled it or it doesn't exist.")
    
    delta = data["Close"].diff()
    gain = delta.where(delta > 0, 0)
    loss = -delta.where(delta < 0, 0)

    avg_gain = gain.ewm(alpha=1/period, min_periods=period).mean()
    avg_loss = loss.ewm(alpha=1/period, min_periods=period).mean()

    rs = avg_gain / avg_loss
    rsi = 100 - (100 / (1 + rs))

    return round(rsi.iloc[-1],2)

def get_rsi_status(ticker, rsi_value):
    if rsi_value > 70:
        return f"{ticker} is OVERBOUGHT"
    elif rsi_value < 30:
        return f"{ticker} is OVERSOLD"
    else:
        return f"{ticker} is NEUTRAL"

if __name__ == "__main__":
    ticker = "AAPL"
    rsi = calculate_rsi(ticker)
    print(f"{ticker} RSI: {rsi}")
    print(get_rsi_status(ticker, rsi))