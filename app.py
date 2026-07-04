import streamlit as st
import pandas as pd
import joblib

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
# ---------------------------
# Title
# ---------------------------

st.title("📈 Retail Demand Forecasting Dashboard")

st.markdown("---")

st.markdown("""
## 📌 Project Overview

This application predicts **future product demand (Quantity Sold)** using a
**Random Forest Regression** model trained on historical retail sales data.

### 🎯 Objectives
- Predict future product demand.
- Support inventory planning.
- Help businesses optimize stock levels.
- Improve sales forecasting using Machine Learning.

### 📊 Dataset
- Online Retail Dataset
- Historical sales transactions
- Customer purchase behaviour
- Product-wise sales information
""")
# ---------------------------
# Sidebar
# ---------------------------

st.sidebar.title("📌 Project Information")

st.sidebar.success("Retail Demand Forecasting")

st.sidebar.markdown("### 🤖 Model")
st.sidebar.write("Random Forest Regressor")

st.sidebar.markdown("### 📚 Learning Type")
st.sidebar.write("Supervised Learning")

st.sidebar.markdown("### 🎯 Problem")
st.sidebar.write("Regression")

st.sidebar.markdown("### 📊 Target")
st.sidebar.write("Quantity")

st.sidebar.markdown("### 👩‍💻 Developer")
st.sidebar.write("Khushi Yadav")

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
# Prediction
# --------------------------------

if st.button("🔮 Predict Demand"):
    st.write("Button Clicked!")

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

    prediction = model.predict(input_data)

    st.success("Prediction Completed Successfully! ✅")

    st.metric(
        label="📦 Predicted Demand (Quantity)",
        value=f"{prediction[0]:.2f}"
    )

    st.balloons()

     # ---------------------------
    # Business Insight
    # ---------------------------
    st.markdown("---")
    st.subheader("💡 Business Insight")

    pred = prediction[0]

    if pred >= 200:
        st.success("🔥 High Demand Expected. Maintain sufficient inventory.")

    elif pred >= 100:
        st.info("📦 Moderate Demand Expected. Current inventory should be sufficient.")

    else:
        st.warning("⚠️ Low Demand Expected. Avoid overstocking.")
    # --------------------------------
# Model Information
# --------------------------------

st.markdown("---")

st.subheader("📊 Model Performance")

c1, c2, c3, c4 = st.columns(4)

with c1:
    st.metric("🤖 Model", "Random Forest")

with c2:
    st.metric("🎯 MAE", "26.69")

with c3:
    st.metric("📉 RMSE", "56.58")

with c4:
    st.metric("📈 R² Score", "92.50%")



# --------------------------------
# Footer
# --------------------------------

st.markdown("---")

st.caption(
    "Developed by Khushi Yadav | Retail Demand Forecasting Project"
)    