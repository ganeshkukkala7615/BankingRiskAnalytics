import streamlit as st
import pandas as pd
import sqlite3
import plotly.express as px
from pathlib import Path

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="SQL Analytics",
    page_icon="📈",
    layout="wide"
)

st.title("📈 SQL Analytics Dashboard")

# -----------------------------
# Connect Database
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DB_PATH = BASE_DIR / "banking.db"

conn = sqlite3.connect(DB_PATH)

# -----------------------------
# Query 1
# -----------------------------
query = """
SELECT job,
COUNT(*) AS Customers
FROM customers
GROUP BY job
ORDER BY Customers DESC;
"""

job_df = pd.read_sql(query, conn)

st.subheader("Customers by Job")

fig = px.bar(
    job_df,
    x="job",
    y="Customers",
    color="Customers",
    title="Customer Distribution by Job"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Query 2
# -----------------------------
query = """
SELECT education,
COUNT(*) AS Customers
FROM customers
GROUP BY education
ORDER BY Customers DESC;
"""

edu_df = pd.read_sql(query, conn)

st.subheader("Education Distribution")

fig = px.pie(
    edu_df,
    names="education",
    values="Customers",
    title="Education Distribution"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Query 3
# -----------------------------
query = """
SELECT marital,
COUNT(*) AS Customers
FROM customers
GROUP BY marital;
"""

marital_df = pd.read_sql(query, conn)

st.subheader("Marital Status")

fig = px.bar(
    marital_df,
    x="marital",
    y="Customers",
    color="Customers"
)

st.plotly_chart(fig, use_container_width=True)

# -----------------------------
# Show Tables
# -----------------------------
st.subheader("SQL Query Results")

st.dataframe(job_df)

st.dataframe(edu_df)

st.dataframe(marital_df)

conn.close()

st.success("SQL Analytics Loaded Successfully")