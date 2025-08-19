import yfinance as yf
import pandas as pd
import streamlit as st
import requests
import os
from dotenv import  load_dotenv

load_dotenv()
# SLACK WEBHOOK URL
SLACK_WEBHOOK_URL = os.getenv("SLACK_WEBHOOK_URL")




# STOCK TRACKER CLASS (OOP)

class StockTracker:
    def __init__(self, symbol, target_price):
        self.symbol = symbol.upper()
        self.target_price = target_price
        self.stock = yf.Ticker(self.symbol)

    def get_stock_price(self):
        """Fetch the latest stock price"""
        data = self.stock.history(period="1d")
        if data.empty:
            return None
        return data["Close"].iloc[-1]

    def get_history(self, days=5):
        """Fetch stock history for chart"""
        return self.stock.history(period=f"{days}d")

    def send_slack_alert(self, message):
        """Send alert to Slack"""
        payload = {"text": message}
        try:
            response = requests.post(SLACK_WEBHOOK_URL, json=payload)
            if response.status_code != 200:
                st.error(f"Slack alert failed: {response.status_code}, {response.text}")
            else:
                st.success("✅ Slack alert sent successfully!")
        except Exception as e:
            st.error(f"Slack alert failed: {e}")

    def check_target(self, current_price):
        """Check if target price is reached"""
        if current_price is not None and current_price >= self.target_price:
            alert_message = f"🚨 {self.symbol} has reached ${current_price:.2f}!"
            st.warning(alert_message)
            self.send_slack_alert(alert_message)



# STREAMLIT DASHBOARD (GUI)

def main():
    st.title("📈 Stock Price Tracker")

    # Predefined stock options
    stock_options = {
        "Apple": "AAPL",
        "Tesla": "TSLA",
        "Google": "GOOGL",
        "Microsoft": "MSFT",
        "Amazon": "AMZN",
        "Nvidia": "NVDA",
        "Netflix": "NFLX",
        "Meta (Facebook)": "META"
    }

    # Dropdown for common stocks
    stock_choice = st.selectbox("Choose a Stock:", list(stock_options.keys()))

    # Also allow manual input
    custom_symbol = st.text_input("Or enter custom Stock Symbol (e.g., IBM, NVAX):", value="")
    stock_symbol = custom_symbol if custom_symbol else stock_options[stock_choice]

    target_price = st.number_input("Enter Target Price ($):", min_value=0.0, value=200.0, step=1.0)

    if stock_symbol:
        tracker = StockTracker(stock_symbol, target_price)
        price = tracker.get_stock_price()

        if price is not None:
            st.metric(label=f"Current Price of {stock_symbol}", value=f"${price:.2f}")
            tracker.check_target(price)

            # Show chart
            history = tracker.get_history(days=7)
            if not history.empty:
                st.subheader("📊 Price Trend (Last 7 Days)")
                st.line_chart(history["Close"])

                # Show pandas DataFrame
                st.subheader("📋 Stock Data Table")
                st.dataframe(pd.DataFrame(history["Close"]))
        else:
            st.error("❌ Could not fetch stock data. Please check the symbol.")


# RUN PROGRAM

if __name__ == "__main__":
    main()
