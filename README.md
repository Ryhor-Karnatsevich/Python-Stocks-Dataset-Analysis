# Python/SQL Stock Market Analysis

DATASET: Historical stock market prices

Dataset source: https://www.kaggle.com/datasets/borismarjanovic/price-volume-data-for-all-us-stocks-etfs

ROWS: 14,887,665

Columns:
date, open, high, low, close, volume, symbol

---

## Project Overview

This project analyzes historical U.S. stock market data using SQL and Python.

The workflow includes extracting data from a large financial dataset, performing data validation and cleaning, and conducting analytical exploration of the most actively traded stocks. The analysis focuses on identifying the most liquid stocks based on trading volume and evaluating their short-term behavior using financial metrics.

Key aspects of the analysis include:

- identifying the most actively traded stocks
- calculating daily returns
- volatility analysis across multiple time horizons (10 / 30 / 90 days)
- trading activity analysis using average volume
- correlation analysis between highly liquid stocks

The project demonstrates a typical **data analysis pipeline using SQL and Python**.

---

## Tools

- Python
- PostgreSQL

---
### Data Wrangling
The original dataset consisted of multiple text files, each representing a single stock ticker. 
All files were aggregated into one unified CSV table to enable large-scale analysis across all stocks.


## SQL

- Wrote a SQL query to extract the **latest 90 days** of data.
- Excluded the **openint** column because it contained missing values.
- Exported the filtered dataset as **90_days.csv**.

---

## Start

- Imported the required Python libraries.
- Loaded the dataset **90_days.csv**.

---

## Data Exploration

- Checked the basic structure of the dataset.

---

## Data Preparation

### Null Test

- Found **64 null values** in the `symbol` column.
- Removed rows with missing values.

### Duplicate Test

- No duplicates were found.

### Logical Test

Ensured the dataset contained no logical errors:

- High ≥ Low
- Volume ≥ 0
- Close ≤ High
- Close ≥ Low

### Date Standardization

- Converted the `date` column to datetime format.

### Data Export

- Exported the cleaned dataset as **clean_data.csv**.

---

## Analysis

### Quick Check

- Verified that the cleaned dataset loaded correctly.

### Tickers Amount

- Identified **7161 unique stock tickers** in the dataset.

### Grouping Tickers

- Calculated the total trading volume for each stock symbol.

### Top 20

- Selected the **top 20 stocks by total trading volume**.

### Tickers List

- Created the **top_symbols** list from the previous table.

### Ticker Filtration

- Filtered the dataset using the **top_symbols** list.

---

## Main Analysis

### Daily Return

- Sorted the dataset by symbol and date.
- Calculated daily percentage returns.

### Volatility

- Calculated volatility for each stock using **10, 30, and 90 day windows**.
- Created an additional **volatility ranking** based on 30-day volatility.

### Average Volume

- Calculated average trading volume over **10, 30, and 90 days**.

### Correlation Matrix

- Generated a correlation matrix for the **top 20 most actively traded stocks**.
- Exported a heatmap visualization as **correlation_heatmap.png**.

![matrix](correlation_heatmap.png)

---

## Conclusion

The analysis identified the most actively traded stocks based on total trading volume and examined their short-term market behavior.

The results show differences in volatility and trading activity across the most liquid stocks. Volatility metrics reveal which stocks experience larger daily price fluctuations, while average volume highlights trading intensity over different time horizons.

The correlation analysis also provides insights into how highly traded stocks move relative to one another, revealing relationships between certain groups of companies.

Overall, this project demonstrates a complete data analysis workflow including **SQL data extraction, data cleaning, financial metric calculation, and visualization using Python**.





















