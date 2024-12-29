import streamlit as st

# Title for the dashboard
st.title("AI-Powered Financial Advisor")

# Input Fields
st.header("Enter Your Financial Details")
monthly_income = st.number_input("Monthly Income (₹)", min_value=0.0, step=1000.0)
monthly_expenses = st.number_input("Monthly Expenses (₹)", min_value=0.0, step=1000.0)
savings_goal = st.number_input("Savings Goal (₹)", min_value=0.0, step=10000.0)
risk_tolerance = st.selectbox("Risk Tolerance Level", ["Low", "Medium", "High"])

# Process Inputs
if st.button("Get Recommendations"):
    remaining_income = monthly_income - monthly_expenses
    st.subheader("Financial Summary")
    st.write(f"Remaining Income After Expenses: ₹{remaining_income}")

    if remaining_income > 0:
        monthly_savings_needed = savings_goal / 12
        st.write(f"Monthly Savings Needed to Achieve Your Goal: ₹{monthly_savings_needed}")
        
        # Recommendations based on risk tolerance
        st.subheader("Investment Recommendations")
        if risk_tolerance == "Low":
            st.write("FDs, Savings Accounts")
        elif risk_tolerance == "Medium":
            st.write("Balanced Mutual Funds")
        elif risk_tolerance == "High":
            st.write("Stocks, Crypto")
    else:
        st.warning("Your expenses exceed your income. Consider reducing expenses.")
