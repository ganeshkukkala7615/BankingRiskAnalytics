import sqlite3
import pandas as pd

conn = sqlite3.connect("../banking.db")

print("=" * 70)
print("WINDOW FUNCTIONS & CTE ANALYSIS")
print("=" * 70)

# --------------------------------------------------
# Query 1 : Rank Jobs by Number of Customers
# --------------------------------------------------

query = """

SELECT
job,
COUNT(*) AS Total_Customers,

RANK() OVER(
ORDER BY COUNT(*) DESC
) AS Job_Rank

FROM customers

GROUP BY job;

"""

print("\nJob Ranking\n")
print(pd.read_sql(query, conn))

# --------------------------------------------------
# Query 2 : Dense Rank by Average Age
# --------------------------------------------------

query = """

SELECT
job,

ROUND(AVG(age),2) AS Average_Age,

DENSE_RANK() OVER(
ORDER BY AVG(age) DESC
) AS Age_Rank

FROM customers

GROUP BY job;

"""

print("\nAverage Age Ranking\n")
print(pd.read_sql(query, conn))

# --------------------------------------------------
# Query 3 : Row Number
# --------------------------------------------------

query = """

SELECT

ROW_NUMBER() OVER(
ORDER BY age DESC
) AS Row_ID,

age,
job,
marital

FROM customers

LIMIT 20;

"""

print("\nTop 20 Oldest Customers\n")
print(pd.read_sql(query, conn))

# --------------------------------------------------
# Query 4 : CTE Example
# --------------------------------------------------

query = """

WITH JobSummary AS
(

SELECT

job,

COUNT(*) AS Customers

FROM customers

GROUP BY job

)

SELECT *

FROM JobSummary

WHERE Customers > 2000

ORDER BY Customers DESC;

"""

print("\nJobs Having More Than 2000 Customers\n")
print(pd.read_sql(query, conn))

conn.close()

print("\nWindow Function Analysis Completed.")