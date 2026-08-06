import sqlite3
import pandas as pd

# Connect to the database
conn = sqlite3.connect("../banking.db")

print("=" * 70)
print("BANKING RISK ANALYTICS PLATFORM - SQL ANALYTICS")
print("=" * 70)

# ------------------------------
# Query 1 - Total Customers
# ------------------------------

query = """
SELECT COUNT(*) AS Total_Customers
FROM customers;
"""

print("\n1. Total Customers")
print(pd.read_sql(query, conn))

# ------------------------------
# Query 2 - Average Age
# ------------------------------

query = """
SELECT ROUND(AVG(age),2) AS Average_Age
FROM customers;
"""

print("\n2. Average Age")
print(pd.read_sql(query, conn))

# ------------------------------
# Query 3 - Customers by Job
# ------------------------------

query = """
SELECT
job,
COUNT(*) AS Customers
FROM customers
GROUP BY job
ORDER BY Customers DESC;
"""

print("\n3. Customers by Job")
print(pd.read_sql(query, conn))

# ------------------------------
# Query 4 - Customers by Marital Status
# ------------------------------

query = """
SELECT
marital,
COUNT(*) AS Customers
FROM customers
GROUP BY marital;
"""

print("\n4. Marital Status")
print(pd.read_sql(query, conn))

# ------------------------------
# Query 5 - Customers by Education
# ------------------------------

query = """
SELECT
education,
COUNT(*) AS Customers
FROM customers
GROUP BY education
ORDER BY Customers DESC;
"""

print("\n5. Education Distribution")
print(pd.read_sql(query, conn))

# ------------------------------
# Query 6 - Housing Loan
# ------------------------------

query = """
SELECT
housing,
COUNT(*) AS Customers
FROM customers
GROUP BY housing;
"""

print("\n6. Housing Loan")
print(pd.read_sql(query, conn))

# ------------------------------
# Query 7 - Personal Loan
# ------------------------------

query = """
SELECT
loan,
COUNT(*) AS Customers
FROM customers
GROUP BY loan;
"""

print("\n7. Personal Loan")
print(pd.read_sql(query, conn))

# ------------------------------
# Query 8 - Subscription Result
# ------------------------------

query = """
SELECT
y,
COUNT(*) AS Customers
FROM customers
GROUP BY y;
"""

print("\n8. Term Deposit Subscription")
print(pd.read_sql(query, conn))

conn.close()

print("\nSQL Analysis Completed Successfully.")