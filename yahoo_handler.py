#!/usr/bin/env python
# coding: utf-8

# In[5]:


get_ipython().system('pip install yfinance')

import yfinance as yf
import pandas as pd

class StockDataFetcher:
    """
    A class to fetch and process stock price data using Yahoo Finance.
    """
    def __init__(self, ticker, start_date, end_date):
        """
        Initialize the StockDataFetcher with a ticker and date range.
        Args:
            ticker (str): Stock ticker symbol (e.g., 'AAPL' for Apple).
            start_date (str): Start date in 'YYYY-MM-DD' format.
            end_date (str): End date in 'YYYY-MM-DD' format.
        """
        self.ticker = ticker
        self.start_date = start_date
        self.end_date = end_date
        self.stock_data = None

    def fetch_stock_data(self):
        """
        Fetch historical stock price data using Yahoo Finance.
        Returns:
            pd.DataFrame: Stock price data.
        """
        print(f"Fetching stock data for {self.ticker}...")
        self.stock_data = yf.download(self.ticker, start=self.start_date, end=self.end_date, group_by="Ticker")

        # Flatten multi-level column names if present
        if isinstance(self.stock_data.columns, pd.MultiIndex):
            self.stock_data.columns = [col[1] if col[1] else col[0] for col in self.stock_data.columns]

        if self.stock_data.empty:
            print("No data fetched. Check the ticker and date range.")
            return None

        print("Stock data fetched successfully.")
        return self.stock_data.head()

    def aggregate_to_annual(self):
        """
        Aggregate stock data to annual average closing prices.
        Returns:
            pd.DataFrame: Annual average stock prices.
        """
        if self.stock_data is None:
            print("Stock data not available. Fetch data first.")
            return None

        # Flatten multi-index columns if necessary
        if isinstance(self.stock_data.columns, pd.MultiIndex):
            self.stock_data.columns = [col[1] if col[1] else col[0] for col in self.stock_data.columns]

        # Ensure 'Close' column exists
        if 'Close' not in self.stock_data.columns:
            raise KeyError("'Close' column not found in the stock data.")

        # Extract the year from the index and calculate annual averages
        self.stock_data['Year'] = self.stock_data.index.year
        annual_data = self.stock_data.groupby('Year')['Close'].mean().reset_index()
        annual_data = annual_data.rename(columns={'Close': 'Stock_Price'})

        print("Stock data aggregated to annual averages.")
        return annual_data

    def save_to_csv(self, file_name):
        """
        Save the stock data to a CSV file.
        Args:
            file_name (str): Name of the file to save the stock data.
        """
        if self.stock_data is not None:
            self.stock_data.to_csv(file_name, index=True)
            print(f"Stock data saved to '{file_name}'.")
        else:
            print("No stock data to save. Fetch data first.")


# In[ ]:




