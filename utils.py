"""
Utility functions for processing order data.
This module contains functions for data cleaning, transformation, and processing.
"""

import pandas as pd
import re


def load_json_data(filepath):
    """
    Load JSON data into a DataFrame.
    
    Args:
        filepath (str): Path to the JSON file
        
    Returns:
        pd.DataFrame: DataFrame containing the loaded data
    """
    df = pd.read_json(filepath)
    return df


def convert_data_types(df):
    """
    Convert columns to appropriate data types with cleaning.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        
    Returns:
        pd.DataFrame: DataFrame with converted data types
    """
    # Create a copy to avoid modifying original
    df_copy = df.copy()
    
    # Convert total_amount: remove $ and convert to float
    df_copy['total_amount'] = df_copy['total_amount'].str.replace('$', '', regex=False).astype(float)
    
    # Convert shipping_days to int
    df_copy['shipping_days'] = df_copy['shipping_days'].astype(int)
    
    # Convert customer_age to int
    df_copy['customer_age'] = df_copy['customer_age'].astype(int)
    
    # Convert rating to float
    df_copy['rating'] = df_copy['rating'].astype(float)
    
    # Convert order_date to datetime
    df_copy['order_date'] = pd.to_datetime(df_copy['order_date'])
    
    return df_copy


def remove_html_tags(text):
    """
    Remove HTML tags from text while preserving spaces between words.
    
    Args:
        text (str): Text containing HTML tags
        
    Returns:
        str: Clean text without HTML tags
    """
    # Replace <br> tags with space
    text = text.replace('<br>', ' ')
    # Remove other HTML tags
    text = re.sub(r'<[^>]+>', '', text)
    # Remove extra spaces
    text = ' '.join(text.split())
    return text


def clean_items_html(df):
    """
    Clean the items_html column by removing HTML tags.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        
    Returns:
        pd.DataFrame: DataFrame with cleaned items_html column
    """
    df_copy = df.copy()
    df_copy['items_html'] = df_copy['items_html'].apply(remove_html_tags)
    return df_copy


def clean_coupon_column(df):
    """
    Replace empty strings in coupon_used column with 'no coupon'.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        
    Returns:
        pd.DataFrame: DataFrame with cleaned coupon_used column
    """
    df_copy = df.copy()
    df_copy['coupon_used'] = df_copy['coupon_used'].replace('', 'no coupon')
    return df_copy


def add_order_month(df):
    """
    Add order_month column based on order_date.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        
    Returns:
        pd.DataFrame: DataFrame with added order_month column
    """
    df_copy = df.copy()
    df_copy['order_month'] = df_copy['order_date'].dt.month
    return df_copy


def add_high_value_order(df):
    """
    Add high_value_order column indicating if order is above average.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        
    Returns:
        pd.DataFrame: DataFrame with added high_value_order column
    """
    df_copy = df.copy()
    average_amount = df_copy['total_amount'].mean()
    df_copy['high_value_order'] = df_copy['total_amount'] > average_amount
    return df_copy


def sort_by_total_amount(df):
    """
    Sort DataFrame by total_amount in descending order.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        
    Returns:
        pd.DataFrame: Sorted DataFrame
    """
    df_sorted = df.sort_values(by='total_amount', ascending=False).reset_index(drop=True)
    return df_sorted


def add_average_rating_by_country(df):
    """
    Add column with average rating per country.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        
    Returns:
        pd.DataFrame: DataFrame with added average_rating_by_country column
    """
    df_copy = df.copy()
    avg_rating_by_country = df_copy.groupby('country')['rating'].transform('mean')
    df_copy['average_rating_by_country'] = avg_rating_by_country
    return df_copy


def filter_high_value_high_rating(df):
    """
    Filter orders where total_amount > 1000 and rating > 4.5.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        
    Returns:
        pd.DataFrame: Filtered DataFrame
    """
    filtered_df = df[(df['total_amount'] > 1000) & (df['rating'] > 4.5)].copy()
    return filtered_df


def add_delivery_status(df):
    """
    Add delivery_status column based on shipping_days.
    
    Args:
        df (pd.DataFrame): Input DataFrame
        
    Returns:
        pd.DataFrame: DataFrame with added delivery_status column
    """
    df_copy = df.copy()
    df_copy['delivery_status'] = df_copy['shipping_days'].apply(
        lambda x: 'delayed' if x > 7 else 'on time'
    )
    return df_copy


def save_to_csv(df, filename):
    """
    Save DataFrame to CSV file.
    
    Args:
        df (pd.DataFrame): DataFrame to save
        filename (str): Output CSV filename
    """
    df.to_csv(filename, index=False)
    print(f"Data successfully saved to {filename}")
