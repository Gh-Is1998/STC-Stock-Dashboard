# STC (Saudi Telecom Company) Stock Market Analysis — Historical Price & Volume

## Project Overview

This project focuses on analyzing the historical stock performance of **Saudi Telecom Company (STC)**. STC was chosen because it is one of the largest and most influential companies in the Saudi stock market, making it a relevant example for understanding market trends and investor behavior.

The dataset was selected from **Yahoo Finance** because it provides accurate, reliable, and complete historical stock data, including daily open, close, high, low prices, and trading volume. This allows for meaningful analysis of price trends, volatility, and technical indicators such as moving averages and RSI.

By combining this dataset with interactive visualizations, the dashboard enables users to explore STC stock trends over time and identify potential buy/sell opportunities.
## Data Source
This project provides a comprehensive historical dataset of Saudi Telecom Company (STC) stock prices and trading volumes on the Saudi Stock Exchange (Tadawul), spanning over 15 years from March 2010 to December 2025. STC (ticker: 7010) is the largest telecommunications company in the Middle East and North Africa (MENA) region and a cornerstone of Saudi Arabia's Vision 2030 digital transformation agenda
The dataset was obtained from Yahoo Finance. It includes historical stock market data such as:
- Date  
- Open price  
- High price  
- Low price  
- Close price  
- Adjusted Close  
- Trading Volume  

This dataset provides daily historical records that allow for time-series analysis and trend identification.


## Steps & Methodology

- Started the project with **Google Colab** for data exploration and cleaning because of its flexible, cloud-based environment.
- ## Analysis Approach

1. **Data Collection**:  
   Retrieved historical stock price data for Saudi Telecom Company (STC) from Yahoo Finance using the `yfinance` Python library.

2. **Data Cleaning and Preparation**:  
   - Converted date columns to datetime format for easier filtering and time-based analysis.  
   - Handled missing or erroneous data by applying data cleaning methods such as coercing invalid dates and removing duplicates.

3. **Feature Engineering**:  
   Calculated technical indicators including:  
   - Moving Averages (MA20, MA50, MA200) to identify trends.  
   - Relative Strength Index (RSI) to detect overbought or oversold conditions.  
   - Buy/Sell signals based on moving average crossovers.

4. **Data Visualization**:  
   - Used Matplotlib and Plotly for static and interactive visualizations respectively.  
   - Developed a Streamlit dashboard to allow users to interactively explore the stock data with filtering options and dynamic charts.

5. **Interpretation**:  
   Analyzed patterns and signals from the visualizations to gain insights into STC’s stock performance, including price trends, volume changes, and potential buy/sell opportunities.
- Transitioned to **Visual Studio Code** for local development and final implementation of the interactive dashboard using Streamlit.
- Used the `yfinance` library to fetch historical stock data of STC from Yahoo Finance.
- Calculated technical indicators such as moving averages (MA20, MA50, MA200) and the Relative Strength Index (RSI).
- Designed the user interface with Streamlit, incorporating interactive visualizations powered by Plotly.
  ## Live Interactive Dashboard

Click the link below to explore the interactive STC stock analysis dashboard, including dynamic charts, moving averages, RSI indicator, and buy/sell signals:

🔗 
 https://stc-stock-dashboard-mep9zf8ybreafwiw8sztwv.streamlit.app/
 https://stc-stock-dashboard-nyos3srcskxxmxbms8oenu.streamlit.app/
https://stc-stock-dashboard-nyos3srcskxxmxbms8oenu.streamlit.app/
