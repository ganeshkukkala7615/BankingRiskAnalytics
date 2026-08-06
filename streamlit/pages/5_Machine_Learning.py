import streamlit as st
import pandas as pd
import plotly.express as px
from pathlib import Path

st.set_page_config(
    page_title="Business Dashboard",
    layout="wide"
)

BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_PATH = BASE_DIR / "data" / "raw" / "bank-full.csv"

df = pd.read_csv(DATA_PATH, sep=";")

st.title("📊 Business Dashboard")

# ---------------- KPI ----------------

c1, c2, c3, c4 = st.columns(4)

c1.metric("Customers", len(df))
c2.metric("Average Age", round(df["age"].mean(),2))
c3.metric("Average Balance", round(df["balance"].mean(),2))
c4.metric("Subscription Rate", f"{round((df['y']=='yes').mean()*100,2)}%")

st.divider()

# ---------------- Age Distribution ----------------

st.subheader("Age Distribution")

fig = px.histogram(
    df,
    x="age",
    nbins=30
)

st.plotly_chart(fig, use_container_width=True)

# ---------------- Job Distribution ----------------

st.subheader("Job Distribution")

fig = px.bar(
    df["job"].value_counts().reset_index(),
    x="job",
    y="count"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------- Balance Distribution ----------------

st.subheader("Balance Distribution")

fig = px.box(
    df,
    y="balance"
)

st.plotly_chart(fig, use_container_width=True)

# ---------------- Subscription ----------------

st.subheader("Deposit Subscription")

fig = px.pie(
    df,
    names="y"
)

st.plotly_chart(fig, use_container_width=True)

st.success("Business Dashboard Loaded Successfully")