import pandas as pd
import streamlit as st


class DashboardUI:
    """ Sets up and manages the Streamlit UI components """

    def __init__(self):
        st.set_page_config(layout="wide")
        self.load_css()

    def load_css(self):
        with open('style.css') as f:
            st.markdown(f'<style>{f.read()}</style>', unsafe_allow_html=True)

    def display_title(self, title):
        st.markdown(title, unsafe_allow_html=True)

    def display_columns_inputs(self):
        cols = st.columns(4)
        car_price = cols[0].number_input('Car Price', value=53305.50, format="%.2f", key='car_price')
        annual_interest_rate = cols[1].number_input('Annual Interest Rate', value=8.20, format="%.2f",
                                                    key='annual_interest_rate')
        loan_term_months = cols[2].number_input('Loan Term (months)', value=60, min_value=1, max_value=120, step=1,
                                                key='loan_term_months')
        monthly_admin_fee = cols[3].number_input('Monthly Admin Fee', value=8, min_value=0, max_value=100, step=1,
                                                 key='monthly_admin_fee')
        return car_price, annual_interest_rate, loan_term_months, monthly_admin_fee

    def setup_layout(self):
        left_col, right_col = st.columns([3, 1])
        return left_col, right_col

    def setup_tabs(self):
        tab1, tab2 = st.tabs(["Monthly Balances", "Principal and Interest Chart"])
        return tab1, tab2

    def display_time_info(self, start_date, loan_term_months):
        today_date = pd.to_datetime('today')
        months_since_start = (today_date.year - start_date.year) * 12 + today_date.month - start_date.month
        months_since_start = min(months_since_start, loan_term_months)  # Ensure we don't exceed the loan term
        remaining_months = loan_term_months - months_since_start

        cols = st.columns(2)
        with cols[0]:
            st.markdown(
                f'<div class="content-box" style="background-color: #293745; padding: 1px; padding-left: 20px;"><h4 style="color: #F63366; font-size: 16px;">Months Paid: {months_since_start}</h4></div>',
                unsafe_allow_html=True)
        with cols[1]:
            st.markdown(
                f'<div class="content-box" style="background-color: #293745; padding: 1px; padding-left: 20px;"><h4 style="color: #F63366; font-size: 16px;">Remaining Months: {remaining_months}</h4></div>',
                unsafe_allow_html=True)

    def display_summary_boxes(self, dataframe):
        """ Display summary statistics in styled boxes """
        with st.container():
            st.write("---")
            col1, col2, col3, col4, col5 = st.columns(5)
            col1.metric("Monthly Repayment", f"${dataframe['Monthly Repayment'].iloc[-1]:,.2f}")
            col2.metric("Principal Paid", f"${dataframe['Principal Paid'].sum():,.2f}")
            col3.metric("Interest Paid", f"${dataframe['Interest Paid'].sum():,.2f}")
            col4.metric("Admin Fee", f"${dataframe['Admin Fee'].sum():,.2f}")
            col5.metric("Total Payment", f"${dataframe['Total Payment'].sum():,.2f}")
            st.write("---")
