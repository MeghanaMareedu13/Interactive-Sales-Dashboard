import streamlit as st
import pandas as pd
import plotly.express as px
import numpy as np
from datetime import datetime, timedelta

# Set page configuration
st.set_page_config(
    page_title="Meghana's Sales Insights Dashboard",
    page_icon="📊",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS for premium look
st.markdown("""
    <style>
    .main {
        background-color: #0e1117;
    }
    .stMetric {
        background-color: #1e2130;
        padding: 20px;
        border-radius: 10px;
        box-shadow: 2px 2px 5px rgba(0,0,0,0.3);
    }
    h1, h2, h3 {
        color: #ff4b4b;
    }
    </style>
    """, unsafe_allow_html=True)

# Generate Synthetic Data
@st.cache_data
def load_data():
    np.random.seed(42)
    dates = pd.date_range(start="2023-01-01", end=datetime.now(), freq='D')
    products = ['Cloud Services', 'Data Pipeline', 'API Integration', 'Consulting']
    regions = ['North America', 'EMEA', 'APAC', 'LATAM']
    
    data = []
    for date in dates:
        num_sales = np.random.randint(1, 10)
        for _ in range(num_sales):
            data.append({
                'Date': date,
                'Product': np.random.choice(products),
                'Region': np.random.choice(regions),
                'Sales': np.random.uniform(500, 5000),
                'Customer_Segment': np.random.choice(['Enterprise', 'SME', 'Startup'])
            })
    return pd.DataFrame(data)

df = load_data()

# Sidebar Filters
st.sidebar.header("📊 Dashboard Filters")
date_range = st.sidebar.date_input(
    "Select Date Range",
    value=[df['Date'].min(), df['Date'].max()],
    min_value=df['Date'].min(),
    max_value=df['Date'].max()
)

selected_region = st.sidebar.multiselect(
    "Select Region(s)",
    options=df['Region'].unique(),
    default=df['Region'].unique()
)

selected_product = st.sidebar.multiselect(
    "Select Product(s)",
    options=df['Product'].unique(),
    default=df['Product'].unique()
)

# Filter Logic
mask = (
    (df['Date'] >= pd.to_datetime(date_range[0])) & 
    (df['Date'] <= pd.to_datetime(date_range[1])) &
    (df['Region'].isin(selected_region)) &
    (df['Product'].isin(selected_product))
)
filtered_df = df.loc[mask]

# Title and Header
st.title("🚀 Sales Insights Dashboard")
st.markdown("### Turning Raw Data into Actionable Insights")

# Key Metrics
col1, col2, col3, col4 = st.columns(4)
total_sales = filtered_df['Sales'].sum()
avg_sale = filtered_df['Sales'].mean()
num_deals = len(filtered_df)
top_region = filtered_df.groupby('Region')['Sales'].sum().idxmax() if not filtered_df.empty else "N/A"

with col1:
    st.metric("Total Revenue", f"${total_sales:,.2f}")
with col2:
    st.metric("Avg Deal Value", f"${avg_sale:,.2f}")
with col3:
    st.metric("Total Deals", num_deals)
with col4:
    st.metric("Top Region", top_region)

st.divider()

# Charts
c1, c2 = st.columns(2)

with c1:
    st.subheader("📈 Revenue Over Time")
    daily_sales = filtered_df.groupby('Date')['Sales'].sum().reset_index()
    fig_line = px.line(daily_sales, x='Date', y='Sales', template='plotly_dark', color_discrete_sequence=['#ff4b4b'])
    st.plotly_chart(fig_line, use_container_width=True)

with c2:
    st.subheader("🍕 Revenue by Product")
    product_sales = filtered_df.groupby('Product')['Sales'].sum().reset_index()
    fig_pie = px.pie(product_sales, values='Sales', names='Product', hole=0.4, template='plotly_dark')
    st.plotly_chart(fig_pie, use_container_width=True)

c3, c4 = st.columns(2)

with c3:
    st.subheader("🌍 Regional Performance")
    region_sales = filtered_df.groupby('Region')['Sales'].sum().reset_index()
    fig_bar = px.bar(region_sales, x='Region', y='Sales', color='Region', template='plotly_dark')
    st.plotly_chart(fig_bar, use_container_width=True)

with c4:
    st.subheader("👥 Customer Segments")
    segment_sales = filtered_df.groupby('Customer_Segment')['Sales'].sum().reset_index()
    fig_sun = px.sunburst(filtered_df, path=['Region', 'Customer_Segment'], values='Sales', template='plotly_dark')
    st.plotly_chart(fig_sun, use_container_width=True)

# Raw Data Table
with st.expander("🔍 View Raw Filtered Data"):
    st.dataframe(filtered_df.sort_values(by='Date', ascending=False), use_container_width=True)

# Footer
st.markdown("---")
st.markdown("Created by **Meghana Mareedu** | Day 6 of 30-Day Recruiter Challenge")
