# -*- coding: utf-8 -*-
"""Data Cleansing turnbackhoax.id.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/12gQqaXvdg8r3uXyV1aIxaTNeN_Tl5oG4
"""

from google.colab import drive
drive.mount('/content/gdrive')

import csv
import pandas as pd
import re
import numpy as np

file_path = '/content/gdrive/MyDrive/[CAPSTONE OASEE]/[ML]/[2.1] Dataset/RAW/turnbackhoax.id_20230518143309.csv'

with open(file_path, 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        # Process each row of the CSV file
        print(row)

data = pd.read_csv(file_path)

# Display the first few rows of the DataFrame
print(data.head())

data.info()

# Check the dimensions of the DataFrame (rows, columns)
print(f"Dimensions: {data.shape}")

# Check the column names
print(f"Column names: {data.columns}")

# Get summary statistics of numerical columns
print(data.describe())

# Count the occurrences of each value in a specific column
print(data['Label'].value_counts())

# Check for missing values in the DataFrame
missing_values = data.isna().sum()
print(missing_values)

rows_with_missing_values = data[data.isna().any(axis=1)]
print(rows_with_missing_values)

# Delete rows with missing values from the DataFrame
data_without_missing = data.dropna()

# Verify that the rows have been removed
print(data_without_missing.shape)

data.dropna(inplace=True)

data.isnull().sum()

# Remove text within square brackets from the 'Title' column
data['Title'] = data['Title'].str.replace(r'\[.*?\]', '', regex=True)
data['Title'] = data['Title'].str.replace(r'\(.*?\)', '', regex=True)

# Display the updated DataFrame
print(data['Title'])

# Display the updated DataFrame
print(data.head())

# Remove sentences before "penjelasan" in the 'Content' column
data['Content'] = data['Content'].str.replace(r'^.*?(penjelasan)', 'penjelasan', regex=True)

# Remove sentences before '[PENJELASAN]' in the 'Content' column
data['Content'] = data['Content'].str.replace(r'^.*?\[PENJELASAN\]', '', regex=True)

# Remove the word '[PENJELASAN]' from the 'Content' column
data['Content'] = data['Content'].str.replace(r'\[PENJELASAN\]', '', regex=True)

# Remove sentences before "PENJELASAN" or "penjelasan" in the 'Content' column
data['Content'] = data['Content'].str.replace(r'^.*?(PENJELASAN|penjelasan)', 'PENJELASAN', regex=True)

# Display the updated DataFrame
print(data.head())

# Remove addresses/links in the 'Content' column
data['Content'] = data['Content'].str.replace(r'http\S+|www.\S+', '', regex=True)

# Remove punctuation and special characters in the 'Content' column
data['Content'] = data['Content'].str.replace(r'[^a-zA-Z0-9\s]', '', regex=True)

# Remove phone numbers in the 'Content' column
data['Content'] = data['Content'].str.replace(r'\d{10,}', '', regex=True)

# Display the updated DataFrame
print(data.head())

# Replace 'HOAX' with 1 in the 'Label' column
data['Label'] = data['Label'].replace('HOAX', 1)

# Display the updated DataFrame
print(data.head())

# Remove "â€œ" from the DataFrame
data = data.replace("â€œ", "", regex=True)

# Remove single quotation marks (')
data['Content'] = data['Content'].str.replace("'", "")

# Remove double quotation marks (")
data['Content'] = data['Content'].str.replace('"', '')

sampled_data = data.sample(n=20, random_state=42)  # Adjust the random_state if needed

print(sampled_data)

"""# save"""

new_file_path = '/content/gdrive/MyDrive/[CAPSTONE OASEE]/[ML]/[2.1] Dataset/Clean/turnbackhoax.id_20230518143309_clean.csv'

# Save the modified DataFrame as a new CSV file
data.to_csv(new_file_path, index=False)

print("New CSV file saved successfully.")

from google.colab import files

# Download the file
files.download(new_file_path)