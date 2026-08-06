import streamlit as st
import pandas as pd
from pathlib import Path

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Home",
    page_icon="🏦",
    layout="wide"
)

# -----------------------------
# Read Dataset
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_PATH = BASE_DIR / "data" / "raw" / "bank-full.csv"

df = pd.read_csv(DATA_PATH, sep=";")

# -----------------------------
# Title
# -----------------------------
st.title("🏦 Banking Risk Analytics Platform")

st.markdown("""
### End-to-End Data Analytics Project

This project demonstrates:

- SQL Analytics
- Advanced SQL
- Excel Automation
- MongoDB
- Machine Learning
- Streamlit Dashboard
""")

# -----------------------------
# KPI Cards
# -----------------------------

total_customers = len(df)

average_age = round(df["age"].mean(),2)

housing_yes = round((df["housing"]=="yes").mean()*100,2)

deposit_yes = round((df["y"]=="yes").mean()*100,2)

col1,col2,col3,col4 = st.columns(4)

col1.metric("Total Customers",total_customers)

col2.metric("Average Age",average_age)

col3.metric("Housing Loan %",f"{housing_yes}%")

col4.metric("Deposit Subscription %",f"{deposit_yes}%")

st.divider()

st.subheader("Dataset Preview")

st.dataframe(df.head(10),use_container_width=True)

st.success("Home Page Loaded Successfully")