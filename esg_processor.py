#!/usr/bin/env python
# coding: utf-8

# In[3]:


import pandas as pd

class ESGProcessor:
    """
    A class to process and analyze ESG data.
    """
    def __init__(self, file_path):
        """
        Initialize the ESGProcessor with a file path.
        Args:
            file_path (str): Path to the cleaned ESG CSV file.
        """
        self.file_path = file_path
        self.data = None  # Raw ESG data
        self.long_data = None  # Reshaped ESG data

    def load_data(self):
        """Load the cleaned ESG dataset."""
        self.data = pd.read_csv(self.file_path)
        print("ESG data loaded successfully.")
        return self.data.head()

    def reshape_data(self):
        """Reshape the dataset from wide format to long format."""
        self.long_data = pd.melt(self.data,
                                 id_vars=['Country Name', 'Country Code', 'Series Name', 'Series Code'],
                                 var_name='Year',
                                 value_name='Value')
        # Convert the 'Year' column to numeric
        self.long_data['Year'] = pd.to_numeric(self.long_data['Year'], errors='coerce')
        print("ESG data reshaped to long format.")
        return self.long_data.head()

    def clean_missing_values(self):
        """Replace '..' in the 'Value' column with NaN and convert to numeric."""
        if self.long_data is None:
            print("Data has not been reshaped yet. Call reshape_data() first.")
            return None
        
        # Replace '..' with NaN and convert 'Value' column to numeric
        self.long_data['Value'] = pd.to_numeric(self.long_data['Value'].replace('..', None), errors='coerce')
        print("Missing values in 'Value' column replaced with NaN.")
        return self.long_data.head()

    def filter_data(self, country, indicator):
        """
        Filter the ESG data for a specific country and indicator.
        Args:
            country (str): Country to filter data for (e.g., 'United States').
            indicator (str): ESG indicator to filter.
        Returns:
            pd.DataFrame: Filtered ESG data.
        """
        if self.long_data is None:
            print("Data has not been reshaped yet. Call reshape_data() first.")
            return None
        
        filtered_data = self.long_data[(self.long_data['Country Name'] == country) &
                                       (self.long_data['Series Name'] == indicator)]
        print(f"Filtered data for {country} - {indicator}")
        return filtered_data


# In[ ]:




