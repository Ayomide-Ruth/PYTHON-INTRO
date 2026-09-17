import streamlit as st
import pandas as pd
import numpy as np
import joblib

# Set page configuration
st.set_page_config(
    page_title="Loan Approval Predictor",
    page_icon="💳",
    layout="wide"
)

# Title and Subtitle
st.title("💳 Credit Approval Prediction System")
st.markdown("Use this interactive tool to assess loan application risk using your trained Logistic Regression model.")

st.divider()

# Load Model Function (cached for performance)
@st.cache_resource
def load_model():
    try:
        model = joblib.load("logistic_regression_model.pkl")
        return model
    except Exception as e:
        st.error(f"Error loading model file `logistic_regression_model.pkl`: {e}")
        return None

model = load_model()

# Sidebar for Input Features
st.sidebar.header("📋 Application Details")

income = st.sidebar.number_input(
    "Annual Income ($)",
    min_value=0,
    max_value=2_000_000,
    value=500_000,
    step=10_000,
    help="Enter total annual income in USD."
)

credit_score = st.sidebar.slider(
    "Credit Score",
    min_value=300,
    max_value=850,
    value=680,
    help="Standard FICO Credit Score range (300 - 850)."
)

employment_years = st.sidebar.number_input(
    "Employment Duration (Years)",
    min_value=0,
    max_value=50,
    value=5,
    step=1
)

debt_ratio = st.sidebar.slider(
    "Debt Ratio",
    min_value=0.0,
    max_value=1.0,
    value=0.35,
    step=0.01,
    help="Monthly debt payments divided by gross monthly income."
)

# Prepare dataframe for prediction matching training column order
input_data = pd.DataFrame({
    "income": [income],
    "credit_score": [credit_score],
    "employment_years": [employment_years],
    "debt_ratio": [debt_ratio]
})

# Layout: Split into two columns for input overview and prediction output
col1, col2 = st.columns([1, 1], gap="large")

with col1:
    st.subheader("Submitted Applicant Summary")
    
    # Render input data cleanly
    summary_df = pd.DataFrame({
        "Feature": ["Annual Income", "Credit Score", "Employment Years", "Debt Ratio"],
        "Value": [f"${income:,.2f}", credit_score, f"{employment_years} yrs", f"{debt_ratio:.2%}"]
    })
    st.table(summary_df)

with col2:
    st.subheader("Model Decision")
    
    if st.button("Evaluate Application", type="primary", use_container_width=True):
        if model is not None:
            # Predict class and probability
            prediction = model.predict(input_data)[0]
            probability = model.predict_proba(input_data)[0][1]
            
            st.write("---")
            
            if prediction == 1:
                st.success("🎉 **Application Approved**")
                st.metric("Approval Probability", f"{probability:.1%}")
                st.progress(probability)
            else:
                st.error("❌ **Application Rejected**")
                st.metric("Approval Probability", f"{probability:.1%}")
                st.progress(probability)
                
            # Decision Insights
            with st.expander("See Risk Breakdown"):
                st.write(f"- **Approval Likelihood:** {probability:.2%}")
                st.write(f"- **Rejection Likelihood:** {1 - probability:.2%}")
                if credit_score < 600:
                    st.caption("⚠️ *Note:* Credit score is in a higher risk band.")
                if debt_ratio > 0.5:
                    st.caption("⚠️ *Note:* High debt ratio detected (> 50%).")
        else:
            st.warning("Model file `logistic_regression_model.pkl` is missing or invalid.")