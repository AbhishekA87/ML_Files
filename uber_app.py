import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Set page configuration
st.set_page_config(page_title="Uber Data Analytics", layout="wide")

# Title
st.title("Uber Data Analytics Dashboard")

# Load dataset
@st.cache
def load_data():
    return pd.read_csv("data/uber_data.csv")

df = load_data()

# Show raw data
if st.checkbox("Show Raw Data"):
    st.write(df.head())

# Data Overview
st.subheader("Data Overview")
st.write(df.describe())

# Visualizations
st.subheader("Hourly Ride Distribution")
hourly_data = df.groupby('hour')['ride_id'].count()
fig, ax = plt.subplots()
hourly_data.plot(kind='bar', ax=ax)
ax.set_title("Number of Rides per Hour")
ax.set_xlabel("Hour")
ax.set_ylabel("Number of Rides")
st.pyplot(fig)
