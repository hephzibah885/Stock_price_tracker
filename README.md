# 📈 Stock Price Tracker

A **Stock Price Tracker** built with **Python, Streamlit, yFinance, and Slack Webhooks**.  
This app allows users to monitor stock prices, visualize trends, and receive real-time alerts via Slack when a target price is reached.  

---

## 🚀 Features
- Fetch **real-time stock prices** using [yFinance](https://pypi.org/project/yfinance/).  
- View **7-day price trends** as interactive charts.  
- Track **predefined popular stocks** (Apple, Tesla, Google, Microsoft, Amazon, Nvidia, Netflix, Meta).  
- Enter **custom stock symbols** manually.  
- Set a **target price** and receive Slack alerts when it’s reached.  
- **GUI dashboard** powered by Streamlit.  

---

## 🛠️ Installation

## 1. Clone the Repository
git clone https://github.com/<your-username>/stock-price-tracker.git
cd stock-price-tracker
2. Create & Activate a Virtual Environment

python -m venv venv
source venv/bin/activate   # macOS/Linux
venv\Scripts\activate      # Windows
3. Install Dependencies

pip install -r requirements.txt
4. Setup Environment Variables
Create a .env file in the project root and add:


SLACK_WEBHOOK_URL=https://hooks.slack.com/services/xxxx/yyyy/zzzz
5. Run the Streamlit App
streamlit run stock_tracker.py

---

## 📖 Walkthrough of the Code
##1. Imports & Environment Setup
python

import yfinance as yf
import pandas as pd
import streamlit as st
import requests
import os
from dotenv import load_dotenv
yFinance → Fetches stock market data.

pandas → Handles stock history in tabular form.

streamlit → GUI dashboard.

requests → Sends Slack alerts.

dotenv → Loads environment variables securely.

## 2. StockTracker Class
Encapsulates stock-tracking logic with OOP principles.

get_stock_price() → Fetch latest stock price.

get_history(days) → Fetch last N days of stock history.

send_slack_alert(message) → Sends alert to Slack.

check_target(current_price) → Checks if stock has reached target price.

## 3. Streamlit Dashboard
Dropdown menu for popular stocks.

Manual input for custom stock symbols.

Displays:
✅ Current stock price
✅ Price trend (last 7 days)
✅ Stock history in DataFrame
✅ Alerts if target price reached

## 4. Main Function
Runs the app when executed:


if __name__ == "__main__":
    main()
## ⚠️ Disclaimer
This project is for educational purposes only.
It does not provide financial advice or guarantee data accuracy.
Always verify financial information with reliable sources before making investment decisions.

---


##✅ Requirements
Example requirements.txt:

nginx
Copy
Edit
yfinance
pandas
streamlit
requests
python-dotenv

---

##⚠️ Notes
On requirements.txt

This file lists all dependencies required to run the project.

Package versions may change over time, which could affect compatibility.

Always use a virtual environment when installing dependencies.

This project is for educational purposes only and should not be used for real-world financial decisions.

On .env

This file is used to securely store sensitive information such as API keys and Slack Webhook URLs.

⚠️ Never share or commit your .env file to GitHub or any public repository.

Replace the placeholder SLACK_WEBHOOK_URL with your own webhook for alerts.

Intended strictly for learning and demonstration purposes, not production use.


