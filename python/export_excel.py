import sqlite3
import pandas as pd

# Connect to database
conn = sqlite3.connect("../banking.db")

# Create an Excel writer
writer = pd.ExcelWriter("../excel/Banking_Report.xlsx", engine="openpyxl")

# Query 1
query1 = """
SELECT job,
COUNT(*) AS Total_Customers
FROM customers
GROUP BY job
ORDER BY Total_Customers DESC;
"""

pd.read_sql(query1, conn).to_excel(
    writer,
    sheet_name="Customers_by_Job",
    index=False
)

# Query 2
query2 = """
SELECT education,
COUNT(*) AS Total_Customers
FROM customers
GROUP BY education
ORDER BY Total_Customers DESC;
"""

pd.read_sql(query2, conn).to_excel(
    writer,
    sheet_name="Education",
    index=False
)

# Query 3
query3 = """
SELECT marital,
COUNT(*) AS Total_Customers
FROM customers
GROUP BY marital;
"""

pd.read_sql(query3, conn).to_excel(
    writer,
    sheet_name="Marital_Status",
    index=False
)

# Query 4
query4 = """
SELECT housing,
COUNT(*) AS Customers
FROM customers
GROUP BY housing;
"""

pd.read_sql(query4, conn).to_excel(
    writer,
    sheet_name="Housing_Loan",
    index=False
)

# Query 5
query5 = """
SELECT loan,
COUNT(*) AS Customers
FROM customers
GROUP BY loan;
"""

pd.read_sql(query5, conn).to_excel(
    writer,
    sheet_name="Personal_Loan",
    index=False
)

writer.close()
conn.close()

print("Excel report generated successfully!")