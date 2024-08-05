import pandas as pd
import numpy as np

# Load the data
file_path = r'D:\sonasm2 T2\sonasm2\Sonasm2.csv'
data = pd.read_csv(file_path)

# Display the first few rows of the dataframe
print("Initial Data:")
print(data.head())

# 1. Handle missing values
# Replace 'null' values with NaN
data.replace('null', np.nan, inplace=True)

# Convert date and time columns to proper datetime format
data['access_date'] = pd.to_datetime(data['access_date'], errors='coerce')
data['access_time'] = pd.to_datetime(data['access_time'], format='%I:%M %p', errors='coerce').dt.time

# Convert numerical columns to proper data types
data['session_duration'] = pd.to_numeric(data['session_duration'], errors='coerce')

# Handle incorrect or inconsistent data in categorical columns
# For example, standardize 'browser_type', 'device_type', 'operating_system', and 'referral_source'
data['browser_type'] = data['browser_type'].astype('category')
data['device_type'] = data['device_type'].astype('category')
data['operating_system'] = data['operating_system'].astype('category')
data['referral_source'] = data['referral_source'].astype('category')

# Fill missing values where appropriate, e.g., forward fill for 'actions_taken'
data['actions_taken'] = data['actions_taken'].fillna(data['actions_taken'].mode()[0])

# Print cleaned data
print("Cleaned Data:")
print(data.head())

# Summary of missing values and data types
print("Missing Values Summary:")
print(data.isnull().sum())
print("\nData Types:")
print(data.dtypes)

# Save the cleaned data to a new CSV file
cleaned_file_path = r'D:\sonasm2 T2\sonasm2\Cleaned_Sonasm2.csv'
data.to_csv(cleaned_file_path, index=False)

print(f"Cleaned data saved to {cleaned_file_path}")
