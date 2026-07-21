from flask import Flask, render_template, request
from rsi import calculate_rsi, get_rsi_status

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    error = None

    if request.method == "POST":
        ticker = request.form["ticker"].upper()
        try:
            rsi = calculate_rsi(ticker)
            status = get_rsi_status(ticker, rsi)
            result = {"ticker": ticker, "rsi": rsi, "status": status}
        except ValueError as e:
            error = str(e)

    return render_template("index.html", result=result, error=error)

if __name__ == "__main__":
    app.run(debug=True)