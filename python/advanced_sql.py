import sqlite3
import pandas as pd

conn = sqlite3.connect("../banking.db")

print("=" * 70)
print("ADVANCED SQL ANALYTICS")
print("=" * 70)

# ---------------------------------------
# Query 1
# Customers older than average age
# ---------------------------------------

query = """

SELECT
age,
job,
marital,
education

FROM customers

WHERE age >
(
SELECT AVG(age)
FROM customers
)

ORDER BY age DESC;

"""

print("\nCustomers Older Than Average Age\n")
print(pd.read_sql(query, conn).head(20))

# ---------------------------------------
# Query 2
# Average Age by Job
# ---------------------------------------

query = """

SELECT

job,

ROUND(AVG(age),2) AS Average_Age,

COUNT(*) AS Total

FROM customers

GROUP BY job

ORDER BY Average_Age DESC;

"""

print("\nAverage Age By Job\n")
print(pd.read_sql(query, conn))

# ---------------------------------------
# Query 3
# Customers having Housing Loan
# ---------------------------------------

query = """

SELECT

job,

COUNT(*) AS Customers

FROM customers

WHERE housing='yes'

GROUP BY job

ORDER BY Customers DESC;

"""

print("\nHousing Loan Analysis\n")
print(pd.read_sql(query, conn))

# ---------------------------------------
# Query 4
# Customers subscribed to Term Deposit
# ---------------------------------------

query = """

SELECT

education,

COUNT(*) AS Subscribers

FROM customers

WHERE y='yes'

GROUP BY education

ORDER BY Subscribers DESC;

"""

print("\nSuccessful Marketing Campaign\n")
print(pd.read_sql(query, conn))

conn.close()

print("\nAdvanced SQL Completed Successfully.")