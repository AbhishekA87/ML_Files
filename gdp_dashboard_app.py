import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt

st.set_page_config(page_title="Global GDP & Unemployment", layout="wide")

st.title("🌍 Global GDP & Unemployment Trends")

# Load data
@st.cache_data
def load_data():
    return pd.read_csv("global_gdp_unemployment.csv")

df = load_data()

# Sidebar filters
country = st.sidebar.selectbox("Select Country", df["Country"].unique())

filtered = df[df["Country"] == country]

# Plot
fig, ax = plt.subplots(figsize=(8,4))
ax.plot(filtered["Year"], filtered["GDP"], label="GDP", linewidth=2)
ax.plot(filtered["Year"], filtered["Unemployment"], label="Unemployment", linewidth=2)
ax.legend()
ax.set_xlabel("Year")
ax.set_ylabel("Value")
ax.set_title(f"{country} GDP & Unemployment Over Time")

st.pyplot(fig)
