# Python/SQL Stock Market Analysis

DATASET: Historical stock market prices

DATASET Source: https://www.kaggle.com/datasets/borismarjanovic/price-volume-data-for-all-us-stocks-etfs

ROWS: 14,887,665

Columns:
date, open, high, low, close, volume, symbol

## Tools:
- Python
- PostgreSQL

### SQL
- Wrote SQL query to get 90 latest days from dataset. Also  didn't use openint  columns, because it had empty values.
- Exported dataset as **90_days.csv**


### Start
- Imported libraries.
- Got dataset from 90_days.csv

### Data Exploration
- Got basic information about the dataset 

### Preparation

### Null verifying
- Found 64 **Null** values in symbol column

### Duplicate test
- No duplicates found

### Logical Test
Ensured data had no logical errors.
 - HIgh >= Low
 - Volume >= 0
 - Close <= High / Close >= Low

### Dat standardazing
- Standardized date column






