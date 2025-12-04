"""
Main script for processing order data.
This script orchestrates the complete data processing pipeline.
"""

import utils

# Replace with your ID number
ID_NUMBER = "123456789"


def main():
    """
    Main processing pipeline for order data.
    """
    print("Starting data processing pipeline...")
    
    # Step 0: Load JSON data
    print("\nStep 0: Loading JSON data...")
    df = utils.load_json_data('orders_simple.json')
    print(f"Loaded {len(df)} rows and {len(df.columns)} columns")
    
    # Step 1: Convert data types
    print("\nStep 1: Converting data types...")
    df = utils.convert_data_types(df)
    print("Data types converted successfully")
    
    # Step 2: Clean items_html column
    print("\nStep 2: Cleaning items_html column...")
    df = utils.clean_items_html(df)
    print("HTML tags removed from items_html")
    
    # Step 3: Clean coupon_used column
    print("\nStep 3: Cleaning coupon_used column...")
    df = utils.clean_coupon_column(df)
    print("Empty coupons replaced with 'no coupon'")
    
    # Step 4: Add order_month column
    print("\nStep 4: Adding order_month column...")
    df = utils.add_order_month(df)
    print("order_month column added")
    
    # Step 5: Add high_value_order column and sort
    print("\nStep 5: Adding high_value_order column and sorting...")
    df = utils.add_high_value_order(df)
    df = utils.sort_by_total_amount(df)
    print("high_value_order column added and data sorted by total_amount")
    
    # Step 6: Add average rating by country
    print("\nStep 6: Adding average rating by country...")
    df = utils.add_average_rating_by_country(df)
    print("average_rating_by_country column added")
    
    # Step 7: Filter high value and high rating orders
    print("\nStep 7: Filtering orders (total_amount > 1000 AND rating > 4.5)...")
    initial_rows = len(df)
    df = utils.filter_high_value_high_rating(df)
    print(f"Filtered from {initial_rows} to {len(df)} rows")
    
    # Step 8: Add delivery_status column
    print("\nStep 8: Adding delivery_status column...")
    df = utils.add_delivery_status(df)
    print("delivery_status column added")
    
    # Step 9: Save to CSV
    print("\nStep 9: Saving to CSV...")
    output_filename = f"clean_orders_{ID_NUMBER}.csv"
    utils.save_to_csv(df, output_filename)
    
    print("\n" + "="*50)
    print("Pipeline completed successfully!")
    print(f"Final dataset: {len(df)} rows, {len(df.columns)} columns")
    print(f"Output file: {output_filename}")
    print("="*50)


if __name__ == "__main__":
    main()
