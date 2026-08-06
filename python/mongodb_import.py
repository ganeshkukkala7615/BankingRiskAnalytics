import pandas as pd
from pymongo import MongoClient

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")

# Create Database
db = client["BankingRiskAnalytics"]

# Create Collection
collection = db["customers"]

# Read CSV
df = pd.read_csv("../data/raw/bank-full.csv", sep=";")

# Convert DataFrame to dictionary
records = df.to_dict(orient="records")

# Remove old data
collection.delete_many({})

# Insert new data
collection.insert_many(records)

print("=" * 60)
print("MongoDB Import Successful")
print("=" * 60)
print("Documents Inserted:", collection.count_documents({}))