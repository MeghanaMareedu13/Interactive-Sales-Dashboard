# 📊 Interactive Sales Insights Dashboard

![Day 06](https://img.shields.io/badge/Day-06-purple?style=for-the-badge)
![Streamlit](https://img.shields.io/badge/Streamlit-FF4B4B?style=flat&logo=streamlit&logoColor=white)
![Plotly](https://img.shields.io/badge/Plotly-3F4F75?style=flat&logo=plotly&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.8+-blue?style=flat&logo=python&logoColor=white)

> **Day 6 of 30-Day Challenge** | A premium, interactive business dashboard built to transform raw sales data into actionable strategic insights.

## 🚀 Experience the Live Data

This project demonstrates how to build a production-quality internal tool for business analysts and sales managers using Python.

### Key Features:
- ⚡ **Real-time Filtering**: Slice data by Date Range, Region, and Product line instantly.
- 📈 **Dynamic KPIs**: High-level metrics (Revenue, Avg Deal Value, Deal Count) that update as you filter.
- 🎨 **Interactive Visuals**: Developed with Plotly for hover effects, zooming, and high-fidelity rendering.
- 🌗 **Premium Dark Theme**: Designed for modern business environments with a focus on readability and aesthetics.
- 📁 **Data Transparency**: Expandable section to inspect the underlying raw data.

## 🛠️ The Tech Stack

- **Streamlit**: The fastest way to build and share data apps.
- **Plotly Express**: High-level API for creating complex, interactive charts.
- **Pandas**: Deep data manipulation and filtering logic.
- **Numpy**: Efficient synthetic data generation.

## 🏃 Run it Locally

```bash
# Clone the repository
git clone https://github.com/MeghanaMareedu13/Interactive-Sales-Dashboard.git
cd Interactive-Sales-Dashboard

# Install dependencies
pip install -r requirements.txt

# Launch the dashboard
streamlit run app.py
```

## 🌐 Deployment Guide

### Option 1: Streamlit Community Cloud (Recommended)
1. Push your code to a public GitHub repository.
2. Sign in to [share.streamlit.io](https://share.streamlit.io/).
3. Click "New app", then select your repo (`Interactive-Sales-Dashboard`).
4. Set the Main file path to `app.py`.
5. Click **Deploy!**

### Option 2: Render
1. Create a new **Web Service** on [Render](https://render.com/).
2. Connect your GitHub repository.
3. **Environment**: `Python`
4. **Build Command**: `pip install -r requirements.txt`
5. **Start Command**: `streamlit run app.py --server.port $PORT --server.address 0.0.0.0`
6. Click **Create Web Service**.


## 📈 Business Use Case

I designed this dashboard to solve a common problem I've seen in my projects: **Data Silos**. 
By centralizing regional and product performance into one interactive view, decision-makers can identify underperforming sectors in seconds rather than waiting for weekly manual reports.

---

⭐ **Part of my 30-Day Project Challenge** | Building technical authority through visualization!

#DataVisualization #Streamlit #BusinessIntelligence #Python #30DayChallenge #DataAnalysis
