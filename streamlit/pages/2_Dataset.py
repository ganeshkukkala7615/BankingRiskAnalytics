import streamlit as st
import pandas as pd
from pathlib import Path

# -----------------------------
# Page Config
# -----------------------------
st.set_page_config(
    page_title="Dataset Explorer",
    page_icon="📊",
    layout="wide"
)

# -----------------------------
# Load Dataset
# -----------------------------
BASE_DIR = Path(__file__).resolve().parent.parent.parent
DATA_PATH = BASE_DIR / "data" / "raw" / "bank-full.csv"

df = pd.read_csv(DATA_PATH, sep=";")

# -----------------------------
# Title
# -----------------------------
st.title("📊 Dataset Explorer")

st.write("Explore, Search, Filter and Download the Banking Dataset.")

# -----------------------------
# Search Box
# -----------------------------
search = st.text_input("Search by Job")

if search:
    filtered_df = df[df["job"].str.contains(search, case=False)]
else:
    filtered_df = df

# -----------------------------
# Filter
# -----------------------------
education = st.selectbox(
    "Filter by Education",
    ["All"] + sorted(df["education"].unique().tolist())
)

if education != "All":
    filtered_df = filtered_df[
        filtered_df["education"] == education
    ]

# -----------------------------
# Display Data
# -----------------------------
st.subheader("Dataset")

st.dataframe(filtered_df, use_container_width=True)

# -----------------------------
# Download CSV
# -----------------------------
csv = filtered_df.to_csv(index=False).encode("utf-8")

st.download_button(
    label="Download Filtered Dataset",
    data=csv,
    file_name="filtered_dataset.csv",
    mime="text/csv"
)

st.success("Dataset Explorer Loaded Successfully!")