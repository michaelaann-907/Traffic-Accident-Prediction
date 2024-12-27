# app/data_cleaning.py

import pandas as pd

def load_and_clean_data(file_path):
    """
    Loads and cleans the dataset.
    - Removes duplicates and null values.
    - Strips and standardizes text columns.
    """
    # Load dataset
    df = pd.read_csv(file_path)
    raw_df = pd.read_csv(file_path)
    print("raw file", raw_df.shape)  # Should print (841, number_of_columns)
    print("raw head", raw_df.head())
    # Check for missing values in each column
    print("null values", df.isnull().sum())
    # Check for duplicate rows
    print("duplicates", df.duplicated().sum())

# Clean dataset
    df = df.drop_duplicates()  # Remove duplicates
    df = df.dropna()  # Remove null values
    df['Weather'] = df['Weather'].str.strip().str.title()  # Standardize capitalization
    df['Time_of_Day'] = df['Time_of_Day'].str.strip().str.title()

    return df
