import streamlit as st
import dask.dataframe as dd
import plotly.express as px
import pandas as pd
from datetime import datetime
import matplotlib.pyplot as plt
import seaborn as sns


# Load custom CSS
st.set_page_config(layout='wide', initial_sidebar_state='expanded')

with open('style.css') as f:
    st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

# Import dataset
df = pd.read_csv("fake_healthcare.csv")

# Header and app description
st.title("Helpman Hospital Healthcare Dashboard")
st.write("This dashboard visualizes key healthcare metrics.")

# Page selection
page = st.sidebar.selectbox(
    "Select a page",
    ["Overview", "Patients", "Operations", "Financials", "Settings"]
)

# Sidebar for data selection (optional)
selected_dep = st.sidebar.selectbox(
    "Department", df["departments"].unique()
)
filtered_df = df[df['departments'] == selected_dep]

# Setup page layout
st.write("## First row")

# Example layout with columns
col1, col2 = st.columns(2)

with col1:
    st.write("### Admission rate")
    
    # Admission rate visualization
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor('lightgray')
    sns.histplot(df['admission_rate'], ax=ax, color='skyblue', kde=True)
    ax.set_title('Admission Rate Distribution', fontsize=16)
    ax.set_xlabel('Admission Rate', fontsize=14)
    ax.set_ylabel('Frequency', fontsize=14)
    ax.grid(True)
    st.pyplot(fig)

with col2:
    st.write("### Admission rate")
    
    # Admission rate visualization
    fig, ax = plt.subplots(figsize=(8, 6))
    fig.patch.set_facecolor('lightyellow')
    sns.histplot(df['admission_rate'], ax=ax, color='salmon', kde=True)
    ax.set_title('Admission Rate Distribution', fontsize=16)
    ax.set_xlabel('Admission Rate', fontsize=14)
    ax.set_ylabel('Frequency', fontsize=14)
    ax.grid(True)
    st.pyplot(fig)

# Example of a full-width row
st.write("## Second row")

col3, col4 = st.columns((6, 4))

with col3:
    st.write("### Admission rate")
    
    # Admission rate visualization
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('lightblue')
    sns.histplot(df['admission_rate'], ax=ax, color='lightgreen', kde=True)
    ax.set_title('Admission Rate Distribution', fontsize=16)
    ax.set_xlabel('Admission Rate', fontsize=14)
    ax.set_ylabel('Frequency', fontsize=14)
    ax.grid(True)
    st.pyplot(fig)

with col4:
    st.write("### Admission rate")
    
    # Admission rate visualization
    fig, ax = plt.subplots(figsize=(6, 6))
    fig.patch.set_facecolor('lightpink')
    sns.histplot(df['admission_rate'], ax=ax, color='lightcoral', kde=True)
    ax.set_title('Admission Rate Distribution', fontsize=16)
    ax.set_xlabel('Admission Rate', fontsize=14)
    ax.set_ylabel('Frequency', fontsize=14)
    ax.grid(True)
    st.pyplot(fig)
    
# Plotting functions
def plot_daily_visits():
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('lightgray')
    sns.barplot(x='date', y='daily_visits', data=filtered_df, ax=ax, color='skyblue')
    ax.set_title('Daily Visits', fontsize=16)
    ax.set_xlabel('Date', fontsize=14)
    ax.set_ylabel('Number of Visits', fontsize=14)
    ax.grid(True)
    st.pyplot(fig)

def plot_admission_rate():
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('lightyellow')
    sns.lineplot(x='date', y='admission_rate', data=filtered_df, ax=ax, marker='o', color='salmon')
    ax.set_title('Admission Rate', fontsize=16)
    ax.set_xlabel('Date', fontsize=14)
    ax.set_ylabel('Admission Rate', fontsize=14)
    ax.grid(True)
    st.pyplot(fig)

def plot_daily_revenue():
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('lightblue')
    sns.barplot(x='date', y='daily_revenue', data=filtered_df, ax=ax, color='lightgreen')
    ax.set_title('Daily Revenue', fontsize=16)
    ax.set_xlabel('Date', fontsize=14)
    ax.set_ylabel('Revenue ($)', fontsize=14)
    ax.grid(True)
    st.pyplot(fig)

def plot_daily_profit():
    fig, ax = plt.subplots(figsize=(10, 6))
    fig.patch.set_facecolor('lightpink')
    sns.barplot(x='date', y='daily_profit', data=filtered_df, ax=ax, color='lightcoral')
    ax.set_title('Daily Profit', fontsize=16)
    ax.set_xlabel('Date', fontsize=14)
    ax.set_ylabel('Profit ($)', fontsize=14)
    ax.grid(True)
    st.pyplot(fig)

# Display plots based on the selected page
if page == "Overview":
    st.write("### Overview")
    col1, col2, col3 = st.columns(3)
    with col1:
        plot_daily_visits()
    with col2:
        plot_admission_rate()
    with col3:
        plot_daily_revenue()

    col4, col5, col6 = st.columns(3)
    with col4:
        plot_daily_profit()
    # You can add more plots to these columns as needed

elif page == "Patients":
    st.write("### Patient Data")
    col1, col2, col3 = st.columns(3)
    with col1:
        plot_daily_visits()
    with col2:
        plot_admission_rate()
    # Add more plots if needed

elif page == "Operations":
    st.write("### Operations Data")
    col1, col2, col3 = st.columns(3)
    with col1:
        plot_daily_revenue()
    with col2:
        plot_daily_profit()
    # Add more plots if needed
# Add more pages as needed


