
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="Retail Sales Dashboard", layout="wide")

st.title("🛍️ Retail Sales Performance Dashboard")
  st.markdown("""
## 🛍️ Project Overview

Retail companies need to analyze product and regional sales performance to drive business decisions. This dashboard provides intuitive visualizations for understanding trends, top categories, and region-wise metrics.

### 🔍 Problem Statement
Retail companies struggle with manual sales data tracking. This dashboard helps automate the process and extract actionable insights.

### 🎯 Objective
- Understand which product categories and regions generate the most revenue  
- Track monthly sales performance  
- Monitor KPIs like total revenue, average order value, and total units sold  
- Visualize sales distribution across categories and regions

### 🧰 Tools Used
- **Python** (Pandas, Seaborn, Matplotlib)  
- **Streamlit** for web-based dashboard  
- **CSV** for data source

### 📊 Sample Visuals
- Bar Chart: Revenue by Region  
- Line Chart: Monthly Sales Trend  
- Pie Chart: Category Revenue Share  

### 📎 GitHub:
[https://github.com/pankajrajbhar19](https://github.com/pankajrajbhar19)

""", unsafe_allow_html=True)
)

# Load data
df = pd.read_csv("retail_sales_data.csv", parse_dates=['Date'])

# KPI calculations
total_revenue = df['Revenue'].sum()
total_units = df['UnitsSold'].sum()
avg_order_value = total_revenue / len(df)

# KPIs
st.metric("Total Revenue", f"₹{total_revenue:,.0f}")
st.metric("Total Units Sold", f"{total_units}")
st.metric("Average Order Value", f"₹{avg_order_value:,.0f}")

# Charts
st.subheader("📊 Revenue by Region")
fig1, ax1 = plt.subplots()
sns.barplot(data=df.groupby('Region')['Revenue'].sum().reset_index(), x='Region', y='Revenue', ax=ax1)
ax1.set_title("Revenue by Region")
st.pyplot(fig1)

st.subheader("📈 Monthly Revenue Trend")
monthly_sales = df.groupby(df['Date'].dt.to_period("M"))['Revenue'].sum().reset_index()
monthly_sales['Date'] = monthly_sales['Date'].astype(str)
fig2, ax2 = plt.subplots()
sns.lineplot(data=monthly_sales, x='Date', y='Revenue', marker='o', ax=ax2)
plt.xticks(rotation=45)
ax2.set_title("Monthly Revenue Trend")
st.pyplot(fig2)

st.subheader("🍕 Revenue Share by Category")
category_sales = df.groupby('Category')['Revenue'].sum()
fig3, ax3 = plt.subplots()
ax3.pie(category_sales, labels=category_sales.index, autopct='%1.1f%%', startangle=140)
ax3.set_title("Revenue Share by Category")
st.pyplot(fig3)
