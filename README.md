# CIS3120-Project1

# Impact of ESG scores in stock prices

This project explores the relationship between Environmental, Social, and Governance (ESG) scores and stock prices. By analyzing ESG data and stock performance, the project investigates whether companies with better ESG practices demonstrate stronger financial outcomes. The project includes multiple stages, from data acquisition to the development of reusable Python classes for data processing and analysis.

# Steps Implemented in the Project

## 1.Data Collection from World Bank Group:
Downloaded ESG data from the World Bank Group ESG Dataset.
This dataset contains global ESG indicators across countries(United States) and industries.
## 2. Data Cleaning:
Processed the raw dataset to handle missing values, reformat columns, and prepare it for analysis.
## 3. Create a Clean CSV File:
I decided to export the cleaned data to a new CSV file (Cleaned_ESG_Data.csv) for further analysis and ease of use.
## 4. Developed the esg_processor.py Class:
I Built a reusable class to handle ESG data processing tasks, including loading, reshaping, and filtering data.
Functions include:
   a. load_data: 
  Load the cleaned ESG dataset.
   b. reshape_data:
  Reshape the data for analysis.
   c. clean_missing_values: 
  Replace invalid values with NaN.
   d. filter_data:
  Filter data by country and ESG indicator.
## 5. Obtained API(free) Key from Polygon:
Generated an API key from Polygon.io to retrieve stock price data. (free key)
## 6. Secured API Credentials:
Created a separate  file (key.py) to securely store the API key.
## 7. Developed the api_handler Class:
Built the api_handler class to interact with the Polygon API.
The class fetches stock price data (e.g., open, close, high, low, and volume) for specific companies and unfortunelly with vey limit days. 
## 8. Developed the yahoo_handler.py Class:
Built the yahoo_handler class to fetch stock data from Yahoo Finance for deeper insights and supplementary information about stocks.
This class retrieves additional stock metrics like historical trends and aggregated data.
## 9. Integrated All Components in the Main File:
Integrated all components (esg_processor, api_handler, and yahoo_handler) into the main script.
The main file coordinates ESG data processing, stock data fetching, and visualizations.

# Conclusion
This project successfully demonstrates the relationship between ESG scores and stock prices, providing valuable insights into the financial benefits of sustainable practices. By integrating ESG data from the World Bank Group with stock data retrieved from Yahoo Finance and the Polygon API, the project highlights how ESG metrics can influence stock performance.
Although the limitations of the free tier of the Polygon API restricted access to comprehensive data, this project lays the groundwork for future research. With more robust API access, there is significant potential to explore deeper relationships between ESG scores and stock performance. This project could be extended next year to unlock these insights.
In the ESG analysis, the first graph illustrates CO₂ emissions (metric tons per capita) in the United States from 1960 to 2023. It reveals irregularities in data, such as missing values from 1960 to 1990, and a sharp increase in emissions in the 1990s, likely due to recording inconsistencies. A notable decline is observed from 2022 to 2023, where emissions decrease from approximately 19 metric tons to near zero, reflecting improved environmental policies or shifts in energy use. These trends emphasize the importance of accurate data collection to effectively monitor emissions over time.
The second graph highlights the inverse relationship between CO₂ emissions and renewable energy consumption. While CO₂ emissions rose sharply between the late 1980s and early 2000s before declining, renewable energy consumption started increasing steadily in the late 1990s. This trend underscores how renewable energy adoption has contributed to emission reductions, emphasizing the effectiveness of clean energy policies and ESG-driven initiatives. However, abrupt changes at the start and end of the graph signal potential data inconsistencies that merit further investigation.
Lastly, in the main file, I integrated ESG data with stock price data for focused analysis. For the years 2022 and 2023, I plotted two key indicators—CO₂ emissions and renewable energy consumption—on the same graph, providing a comparative view. The orange line represents stock prices, while the blue dashed line shows ESG indicators. The graph highlights the interplay between financial performance and ESG metrics. For this analysis, I selected MSFT (Microsoft) and CRM (Salesforce) as companies known for their high ESG performance, based on their inclusion in "10 Best ESG Stocks". Additionally, the Stock Prices vs ESG Indicator graph demonstrates a steady increase in the stock prices of Microsoft and Salesforce from 2022 to 2023. While both companies showed consistent financial growth, the ESG indicator (CO₂ emissions) remained at zero due to missing data. This highlights the challenge of incomplete ESG reporting and underscores the importance of reliable environmental data for understanding its impact on stock performance.
Overall, this project successfully visualizes the impact of ESG metrics on financial outcomes while identifying areas for future enhancement. By integrating ESG and financial data, it explores the growing significance of sustainability in investment decisions. With improvements in data availability and analysis, the project has the potential to provide deeper insights into the value of ESG-friendly practices, making it a strong foundation for further research.
