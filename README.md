# Pandas Order Data Processing Assignment

## Overview
This project processes order data from a JSON file through a series of cleaning, transformation, and filtering steps to produce a clean CSV output.

## Files
- `orders_simple.json` - Original data source
- `utils.py` - Utility functions for data processing
- `main.py` - Main execution script
- `clean_orders_[ID_NUMBER].csv` - Output file (generated)

## Requirements
- Python 3.x
- pandas library

## Installation
```bash
pip install pandas
```

## Usage
1. Update the `ID_NUMBER` variable in `main.py` with your ID number
2. Run the main script:
```bash
python main.py
```

## Processing Steps

### Step 0: Load Data
Loads the JSON file into a pandas DataFrame.

### Step 1: Data Type Conversion
Converts columns to appropriate data types:
- `total_amount`: Removes $ symbol and converts to float
- `shipping_days`: Converts to int
- `customer_age`: Converts to int
- `rating`: Converts to float
- `order_date`: Converts to datetime

### Step 2: Clean HTML Tags
Removes HTML tags from `items_html` column while preserving spaces between words.

### Step 3: Clean Coupon Column
Replaces empty strings in `coupon_used` with "no coupon".

### Step 4: Add Order Month
Creates `order_month` column containing the month number (1-12) from `order_date`.

### Step 5: High Value Orders and Sorting
- Creates `high_value_order` column (True if `total_amount` > average)
- Sorts data by `total_amount` in descending order

### Step 6: Average Rating by Country
Adds `average_rating_by_country` column with the mean rating for each country.

### Step 7: Filter Orders
Filters to keep only orders where:
- `total_amount` > 1000 AND
- `rating` > 4.5

### Step 8: Delivery Status
Creates `delivery_status` column:
- "delayed" if `shipping_days` > 7
- "on time" otherwise

### Step 9: Save Output
Saves the final DataFrame to CSV file.

## Output
The final CSV file contains all original columns (some modified) plus the new columns created during processing, filtered and sorted according to the specifications.

## Project Structure
```
week7_padnas/
├── orders_simple.json          # Source data
├── utils.py                    # Utility functions
├── main.py                     # Main execution script
├── README.md                   # This file
└── clean_orders_[ID].csv       # Generated output
```

## Notes
- All functions are modular and well-documented
- Only pandas and built-in Python libraries are used
- The pipeline preserves data integrity through each step
