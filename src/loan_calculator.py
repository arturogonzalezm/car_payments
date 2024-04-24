import pandas as pd


class LoanCalculator:
    """Handles the calculation of loan repayments."""

    def calculate_monthly_repayment(self, principal, monthly_interest_rate, loan_term_months):
        return principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term_months) / \
            ((1 + monthly_interest_rate) ** loan_term_months - 1)

    def calculate_balances(self, car_price, monthly_interest_rate, loan_term_months, monthly_admin_fee, start_date):
        monthly_repayment = self.calculate_monthly_repayment(car_price, monthly_interest_rate, loan_term_months)
        contract_balance = car_price
        monthly_balances = []
        for month in range(loan_term_months):
            interest_for_month = contract_balance * monthly_interest_rate
            principal_paid = monthly_repayment - interest_for_month
            contract_balance -= principal_paid
            total_repayment_with_fee = monthly_repayment + monthly_admin_fee
            monthly_balances.append({
                "Month": month + 1,
                "Date": (start_date + pd.DateOffset(months=month)).strftime('%d/%m/%Y'),
                "Monthly Repayment": monthly_repayment,
                "Principal Paid": principal_paid,
                "Interest Paid": interest_for_month,
                "Admin Fee": monthly_admin_fee,
                "Total Payment": total_repayment_with_fee,
                "Contract Balance": contract_balance
            })
        return pd.DataFrame(monthly_balances)
