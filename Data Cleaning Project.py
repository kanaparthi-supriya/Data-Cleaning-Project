DATA CLEANING PROJECT

# Import Libraries

import pandas as pd
import numpy as np

# Load Dataset
df=pd.read_csv("/content/AB_NYC_2019-selected-columns.csv")
print("===== DATA INTEGRITY CHECK =====")

# Dataset Information
print(df.info())

# Data Types
print(df.dtypes)

# Summary Statistics
print(df.describe())

"""MISSING DATA HANDLING"""

print("\n===== MISSING VALUES =====")
# Check Missing Values
print(df.isnull().sum())

# Total Missing Values
print("Total Missing Values:", df.isnull().sum().sum())

# Fill Missing Values
df['name'] = df['name'].fillna('Unknown')
df['host_name'] = df['host_name'].fillna('Unknown')
# df['reviews_per_month'] = df['reviews_per_month'].fillna(0)

# Verify Missing Values
print("\nAfter Handling Missing Values")
print(df.isnull().sum())

"""DUPLICATE REMOVAL"""

print("\n===== DUPLICATE RECORDS =====")
# Count Duplicates
print("Duplicate Rows:", df.duplicated().sum())

# Remove Duplicates
df = df.drop_duplicates()

# Verify
print("Duplicate Rows After Removal:", df.duplicated().sum())

""" STANDARDIZATION"""

print("\n===== STANDARDIZATION ====")

# Convert Text Columns to Lowercase
# Ensure the columns are of string type before applying .str accessor.
df['neighbourhood_group'] = df['neighbourhood_group'].astype(str).str.lower()
df['room_type'] = df['room_type'].astype(str).str.lower()

# Remove Extra Spaces
df['neighbourhood_group'] = df['neighbourhood_group'].str.strip()
df['room_type'] = df['room_type'].str.strip()

# Verify Unique Values
print(df['neighbourhood_group'].unique())
print(df['room_type'].unique())

"""OUTLIER DETECTION"""

print("\n===== OUTLIER DETECTION =====")

# Calculate Q1 and Q3
Q1 = df['price'].quantile(0.25)
Q3 = df['price'].quantile(0.75)

# Calculate IQR
IQR = Q3 - Q1

# Detect Outliers
outliers = df[
    (df['price'] < (Q1 - 1.5 * IQR)) |
    (df['price'] > (Q3 + 1.5 * IQR))
]

# Display Outliers
print(outliers)

# Count Outliers
print("Number of Outliers:", len(outliers))

"""SAVE CLEANED DATASET"""

df.to_csv("Cleaned_AB_NYC_2019.csv", index=False)

print("\nData Cleaning Completed Successfully")
