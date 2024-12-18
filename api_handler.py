#!/usr/bin/env python
# coding: utf-8

# In[11]:


from key import POLYGON_API_KEY
import requests

class APIHandler:
    """
    A handler to fetch data from external APIs like Polygon API.
    """
    def __init__(self, api_key):
        """
        Initialize the APIHandler with a Polygon API key.
        Args:
            api_key (str): Polygon API key.
        """
        self.api_key = api_key

    def fetch_last_trade(self, ticker):
        """
        Fetch the last trade data for a specific ticker.
        Args:
            ticker (str): Stock ticker symbol (e.g., 'AAPL').
        Returns:
            dict or None: JSON response with the last trade data.
        """
        url = f"https://api.polygon.io/v2/last/trade/{ticker}"
        params = {"apiKey": self.api_key}
        
        print(f"Fetching last trade data for {ticker}...")
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            print("Last trade data fetched successfully.")
            return response.json()
        else:
            print(f"Error: Failed to fetch last trade data. Status code: {response.status_code}")
            return None

    def fetch_previous_close(self, ticker):
        """
        Fetch the previous day's closing price for a specific ticker.
        Args:
            ticker (str): Stock ticker symbol (e.g., 'AAPL').
        Returns:
            dict or None: JSON response with previous close data.
        """
        url = f"https://api.polygon.io/v2/aggs/ticker/{ticker}/prev"
        params = {"apiKey": self.api_key}
        
        print(f"Fetching previous close data for {ticker}...")
        response = requests.get(url, params=params)
        
        if response.status_code == 200:
            print("Previous close data fetched successfully.")
            return response.json()
        else:
            print(f"Error: Failed to fetch previous close data. Status code: {response.status_code}")
            return None


# In[ ]:




