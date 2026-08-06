import pandas as pd
import sqlite3

# Load dataset
df = pd.read_csv("../data/raw/bank-full.csv", sep=";")

# Connect to SQLite database
conn = sqlite3.connect("banking.db")

# Store data into SQL table
df.to_sql(
    "customers",
    conn,
    if_exists="replace",
    index=False
)

print("Database created successfully.")
print("Table Name: customers")
print("Rows Inserted:", len(df))

conn.close()