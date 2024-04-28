"""Module for managing the dashboard facade which integrates UI components with data calculation."""

import pandas as pd
import streamlit as st
import plotly.express as px

from src.dashboard_ui import DashboardUI
from src.loan_calculator import LoanCalculator


class DashboardFacade:
    """Facade that coordinates the loan calculation and the UI components."""

    def __init__(self):
        """
        Constructor for the DashboardFacade class.
        :return: None
        :rtype: None
        """
        self.ui = DashboardUI()
        self.calculator = LoanCalculator()

    def setup_dashboard(self):
        """
        Method to setup the dashboard.
        :return: None
        :rtype: None
        """
        self.ui.display_title(
            "<h2 style='text-align: left; color: #F63366; font-size: 24px;'>Car Loan Payment Dashboard</h2>")
        car_price, annual_interest_rate, loan_term_months, monthly_admin_fee = self.ui.display_columns_inputs()
        monthly_interest_rate = annual_interest_rate / 100 / 12
        start_date = pd.to_datetime('2023-06-12')
        monthly_balances_df = self.calculator.calculate_balances(car_price, monthly_interest_rate, loan_term_months,
                                                                 monthly_admin_fee, start_date)
        tab1, tab2 = self.ui.setup_tabs()

        with tab1:
            main_col, side_col = st.columns([3, 1])
            with main_col:
                st.dataframe(monthly_balances_df.set_index('Month'), height=400)
            with side_col:
                today_date = pd.to_datetime('today')
                months_since_start = (today_date.year - start_date.year) * 12 + today_date.month - start_date.month
                months_since_start = min(months_since_start, loan_term_months)
                remaining_months = loan_term_months - months_since_start
                st.markdown(
                    f'<div class="content-box" style="background-color: #293745; padding: 60px; padding-left: 20px;">'
                    f'<h4 style="color: #F63366; font-size: 20px;">Months Paid: {months_since_start}</h4></div>',
                    unsafe_allow_html=True)
                st.markdown(
                    f'<div class="content-box" style="background-color: #293745; padding: 60px; padding-left: 20px;">'
                    f'<h4 style="color: #F63366; font-size: 20px;">Remaining Months: {remaining_months}</h4></div>',
                    unsafe_allow_html=True)

            self.ui.display_summary_boxes(monthly_balances_df)

        with tab2:
            fig = px.line(monthly_balances_df, x='Date', y=['Principal Paid', 'Interest Paid'],
                          labels={'value': 'Amount ($)', 'variable': 'Type of Payment'},
                          title='Monthly Principal and Interest Payments')
            fig.update_layout(xaxis_title='Date', yaxis_title='Amount ($)')
            st.plotly_chart(fig, use_container_width=True)
