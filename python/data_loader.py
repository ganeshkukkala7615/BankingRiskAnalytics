import pandas as pd

# Load the dataset
df = pd.read_csv("data/raw/bank-full.csv", sep=";")

# Display basic information
print("\nFirst 5 Rows:")
print(df.head())

print("\nShape:")
print(df.shape)

print("\nColumns:")
print(df.columns.tolist())

print("\nData Types:")
print(df.dtypes)

print("\nMissing Values:")
print(df.isnull().sum())