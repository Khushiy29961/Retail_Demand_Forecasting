import streamlit as st
import pandas as pd
import joblib
import plotly.express as px
import plotly.graph_objects as go

# ---------------------------
# Page Configuration
# ---------------------------

st.set_page_config(
    page_title="Retail Demand Forecasting",
    page_icon="📈",
    layout="wide"
)

# ---------------------------
# Load Model
# ---------------------------
model = joblib.load("models/demand_forecasting_model (4).pkl")
# ==========================================================
# LOAD DATASET
# ==========================================================

df = pd.read_csv("processed_retail_data.csv")
# ---------------------------
# Title
# ---------------------------

st.title("📈 Retail Demand Forecasting Dashboard")



# ==========================================================
# 📌 SIDEBAR
# ==========================================================

with st.sidebar:

    st.image(
        "https://img.icons8.com/color/96/combo-chart--v1.png",
        width=80
    )

    st.title("Retail Demand Forecasting")

    st.markdown("---")

    st.success("📈 Machine Learning Dashboard")

    # =====================================
    # MODEL DETAILS
    # =====================================

    st.markdown("### 🤖 Model Used")
    st.info("Random Forest Regressor")

    st.markdown("### 🎯 Accuracy")
    st.success("92.50 %")

    st.markdown("### 👩‍💻 Developed By")
    st.write("**Khushi Yadav**")

    st.markdown("---")

    # =====================================
    # DASHBOARD NAVIGATION
    # =====================================

    st.markdown("## 📊 Dashboard Navigation")

    page = st.radio(
        "",
        [
            "🏠 Executive Summary",
            "📈 Sales Overview",
            "💰 Revenue Analysis",
            "📦 Product Performance",
            "👥 Customer Analytics",
            "📅 Monthly Trends",
            "🌦 Seasonal Analysis",
            "📊 Demand Analytics",
            "📦 Inventory Insights",
            "🤖 Demand Prediction",
            "💡 Business Insights",
            "👩‍💻 About Project"
        ]
    )
# ==========================================================
# 🏠 DASHBOARD 1 : EXECUTIVE SUMMARY
# ==========================================================

if page == "🏠 Executive Summary":

    st.header("🏠 Executive Summary")

    # ================= KPI CARDS =================

    col1, col2, col3, col4 = st.columns(4)

    col1.metric("💰 Revenue", f"₹ {df['Revenue'].sum():,.0f}")
    col2.metric("📦 Quantity Sold", int(df["Quantity"].sum()))
    col3.metric("🛍 Products", df["Product_ID"].nunique())
    col4.metric("👥 Customers", int(df["Unique_Customers"].sum()))

    st.divider()

    # ================= REVENUE CHART =================

    st.subheader("Monthly Revenue")

    revenue = (
        df.groupby("Month")["Revenue"]
        .sum()
        .reset_index()
    )

    fig = px.line(
        revenue,
        x="Month",
        y="Revenue",
        markers=True,
        title="Monthly Revenue Trend"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.subheader("Revenue Distribution")

    fig2 = px.histogram(
        df,
        x="Revenue",
        nbins=30,
        color_discrete_sequence=["royalblue"]
    )

    st.plotly_chart(fig2, use_container_width=True)

    st.success(
        "Business performance is healthy with stable revenue generation."
    )
    # ==========================================================
# 📈 DASHBOARD 2 : SALES OVERVIEW
# ==========================================================

elif page == "📈 Sales Overview":

    st.header("📈 Sales Overview")

    monthly_sales = (
        df.groupby("Month")["Quantity"]
        .sum()
        .reset_index()
    )

    col1, col2 = st.columns(2)

    with col1:

        fig = px.bar(
            monthly_sales,
            x="Month",
            y="Quantity",
            color="Quantity",
            title="Monthly Quantity Sold"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        fig = px.line(
            monthly_sales,
            x="Month",
            y="Quantity",
            markers=True,
            title="Monthly Sales Trend"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.info("Sales trend helps identify peak demand periods.")
    # ==========================================================
# 💰 DASHBOARD 3 : REVENUE ANALYSIS
# ==========================================================

elif page == "💰 Revenue Analysis":

    st.header("💰 Revenue Analysis")

    revenue = (
        df.groupby("Month")["Revenue"]
        .sum()
        .reset_index()
    )

    col1, col2 = st.columns(2)

    with col1:

        fig = px.area(
            revenue,
            x="Month",
            y="Revenue",
            title="Revenue Trend"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        fig = px.bar(
            revenue,
            x="Month",
            y="Revenue",
            color="Revenue",
            title="Monthly Revenue"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.success("Revenue shows the overall business growth.")
    # ==========================================================
# 📦 DASHBOARD 4 : PRODUCT PERFORMANCE
# ==========================================================

elif page == "📦 Product Performance":

    st.header("📦 Product Performance")

    top_products = (
        df.groupby("Product_ID")["Quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(10)
        .reset_index()
    )

    col1, col2 = st.columns(2)

    with col1:

        fig = px.bar(
            top_products,
            x="Product_ID",
            y="Quantity",
            color="Quantity",
            title="Top 10 Products"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        fig = px.pie(
            top_products,
            names="Product_ID",
            values="Quantity",
            title="Product Contribution"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.success("These products contribute the highest sales volume.")
    # ==========================================================
# 👥 DASHBOARD 5 : CUSTOMER ANALYTICS
# ==========================================================

elif page == "👥 Customer Analytics":

    st.header("👥 Customer Analytics")

    customer_data = (
        df.groupby("Month")["Unique_Customers"]
        .sum()
        .reset_index()
    )

    col1, col2 = st.columns(2)

    with col1:
        fig = px.bar(
            customer_data,
            x="Month",
            y="Unique_Customers",
            color="Unique_Customers",
            title="Monthly Customers"
        )
        st.plotly_chart(fig, use_container_width=True)

    with col2:
        fig = px.line(
            customer_data,
            x="Month",
            y="Unique_Customers",
            markers=True,
            title="Customer Growth"
        )
        st.plotly_chart(fig, use_container_width=True)

    st.success("Customer engagement is increasing across the months.")
    # ==========================================================
# 📅 DASHBOARD 6 : MONTHLY TRENDS
# ==========================================================

elif page == "📅 Monthly Trends":

    st.header("📅 Monthly Trends")

    monthly = (
        df.groupby("Month")[["Revenue","Quantity"]]
        .sum()
        .reset_index()
    )

    fig = px.line(
        monthly,
        x="Month",
        y=["Revenue","Quantity"],
        markers=True,
        title="Revenue vs Quantity"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.info("Monthly trends help identify seasonal business performance.")
    # ==========================================================
# 🌦 DASHBOARD 7 : SEASONAL ANALYSIS
# ==========================================================

elif page == "🌦 Seasonal Analysis":

    st.header("🌦 Seasonal Analysis")

    season = (
        df.groupby("Month")["Revenue"]
        .mean()
        .reset_index()
    )

    fig = px.area(
        season,
        x="Month",
        y="Revenue",
        title="Average Monthly Revenue"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.success("Seasonality analysis helps identify high-demand periods.")
    # ==========================================================
# 📊 DASHBOARD 8 : DEMAND ANALYTICS
# ==========================================================

elif page == "📊 Demand Analytics":

    st.header("📊 Demand Analytics")

    fig = px.scatter(
        df,
        x="Average_Product_Sales",
        y="Quantity",
        color="Revenue",
        size="Revenue",
        title="Average Sales vs Quantity"
    )

    st.plotly_chart(fig, use_container_width=True)

    corr = df[
        ["Revenue","Quantity","Average_Product_Sales"]
    ].corr()

    st.subheader("Correlation Matrix")

    fig = px.imshow(
        corr,
        text_auto=True,
        color_continuous_scale="Blues"
    )

    st.plotly_chart(fig, use_container_width=True)

    st.success("Higher average product sales generally lead to higher demand.")
    # ==========================================================
# 📦 DASHBOARD 9 : INVENTORY INSIGHTS
# ==========================================================

elif page == "📦 Inventory Insights":

    st.header("📦 Inventory Insights")

    inventory = (
        df.groupby("Product_ID")["Quantity"]
        .sum()
        .sort_values(ascending=False)
        .head(15)
        .reset_index()
    )

    col1, col2 = st.columns(2)

    with col1:

        fig = px.bar(
            inventory,
            x="Product_ID",
            y="Quantity",
            color="Quantity",
            title="Top 15 Products by Quantity"
        )

        st.plotly_chart(fig, use_container_width=True)

    with col2:

        fig = px.box(
            df,
            y="Quantity",
            title="Inventory Quantity Distribution"
        )

        st.plotly_chart(fig, use_container_width=True)

    st.success(
        "Inventory analysis helps identify products requiring frequent restocking."
    )
    # ==========================================================
# 🤖 DASHBOARD 10 : DEMAND PREDICTION
# ==========================================================

elif page == "🤖 Demand Prediction":

    st.header("🤖 Demand Prediction")
     # =========================================
    # 📊 MODEL PERFORMANCE KPI CARDS
    # =========================================

    st.markdown("---")

    col1, col2, col3, col4 = st.columns(4)

    with col1:
        st.metric(
            label="📦 Model",
            value="Random Forest"
        )

    with col2:
        st.metric(
            label="🎯 Accuracy (R²)",
            value="92.50%"
        )

    with col3:
        st.metric(
            label="📉 MAE",
            value="26.69"
        )

    with col4:
        st.metric(
            label="📈 RMSE",
            value="56.58"
        )

    st.markdown("---")
    # ---------------------------
# Input Section
# ---------------------------

st.header("📝 Enter Product Details")

col1, col2 = st.columns(2)

with col1:

    product_id = st.number_input(
        "Product ID",
        min_value=1,
        value=1000
    )

    year = st.number_input(
        "Year",
        min_value=2010,
        max_value=2035,
        value=2011
    )

    month = st.slider(
        "Month",
        1,
        12,
        1
    )


    lag1 = st.number_input(
        "Lag 1",
        value=100.0
    )


    lag2 = st.number_input(
        "Lag 2",
        value=100.0
    )

with col2:

    

    lag3 = st.number_input(
        "Lag 3",
        value=100.0
    )

    last_transaction = st.number_input(
        "Last Transaction",
        value=30
    )

    unique_customers = st.number_input(
        "Unique Customers",
        value=10
    )

    average_sales = st.number_input(
        "Average Product Sales",
        value=150.0
    )
    # --------------------------------
# --------------------------------
# Prediction
# --------------------------------

if st.button("🔮 Predict Demand"):

    # Create input dataframe
    input_data = pd.DataFrame({
        'Product_ID': [product_id],
        'Year': [year],
        'Month': [month],
        'lag_1': [lag1],
        'lag_2': [lag2],
        'lag_3': [lag3],
        'last_transaction': [last_transaction],
        'Unique_Customers': [unique_customers],
        'Average_Product_Sales': [average_sales]
    })

    # Make prediction
    prediction = model.predict(input_data)[0]

    # Show success message
    st.success("Prediction Completed Successfully! ✅")

    # Display predicted demand
    st.metric(
        label="📦 Predicted Demand",
        value=f"{prediction:.2f} Units"
    )

    # Demand Status
    if prediction < 100:
        st.error("🔴 Low Demand Expected")

    elif prediction < 250:
        st.warning("🟡 Moderate Demand Expected")

    else:
        st.success("🟢 High Demand Expected")

    # Balloons animation
    st.balloons()
    # ---------------------------
    # Business Insight
    # ---------------------------

    st.markdown("---")
    st.subheader("💡 Business Insight")

    if prediction >= 200:
        st.success("🔥 High Demand Expected. Increase inventory to avoid stock-outs.")

    elif prediction >= 100:
        st.info("📦 Moderate Demand Expected. Current inventory should be sufficient.")

    else:
        st.warning("⚠️ Low Demand Expected. Avoid overstocking to reduce holding costs.")
# ==========================================================
# 💡 DASHBOARD 11 : BUSINESS INSIGHTS
# ==========================================================

elif page == "💡 Business Insights":

    st.header("💡 Business Insights")

    st.markdown("## Key Business Insights")

    st.success("✔ Random Forest achieved an R² Score of 92.50%.")

    st.info("✔ Revenue shows consistent growth across months.")

    st.info("✔ Top-selling products contribute the majority of sales.")

    st.warning("✔ Low-demand products should not be overstocked.")

    st.success("✔ Customer count has steadily increased over time.")

    st.info("✔ Seasonal patterns can improve inventory planning.")

    st.markdown("---")

    st.subheader("Recommendations")

    st.write("• Maintain inventory for high-demand products.")

    st.write("• Offer discounts on low-demand inventory.")

    st.write("• Increase stock before peak sales months.")

    st.write("• Focus marketing on top-performing products.")
    # ==========================================================
# 👩‍💻 DASHBOARD 12 : ABOUT PROJECT
# ==========================================================

elif page == "👩‍💻 About Project":

    st.header("👩‍💻 About This Project")

    st.markdown("""
### 📈 Retail Demand Forecasting Dashboard

This project predicts future retail demand using a **Random Forest Regression Model**.

### 🔹 Technologies Used

- Python
- Streamlit
- Pandas
- Plotly
- Scikit-Learn
- Joblib

### 🔹 Dataset

Online Retail Dataset

### 🔹 Machine Learning Model

Random Forest Regressor

### 🔹 Model Performance

- Accuracy (R²): **92.50%**
- MAE: **26.69**
- RMSE: **56.58**

### 🔹 Features Used

- Product ID
- Year
- Month
- Lag Features
- Last Transaction
- Unique Customers
- Average Product Sales

---

### 👩‍💻 Developed By

**Khushi Yadav**
""")
# --------------------------------
# Footer
# --------------------------------

st.markdown("---")

st.caption(
    "Developed by Khushi Yadav | Retail Demand Forecasting Project"
)    