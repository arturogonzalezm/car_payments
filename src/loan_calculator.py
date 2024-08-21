<<<<<<< HEAD
=======
"""
The calculate_balances method returns a pandas DataFrame created from the monthly_balances list.
This DataFrame provides a detailed breakdown of the loan repayment schedule, including the principal paid, interest paid, admin fee, total payment, and remaining contract balance for each month.
"""

>>>>>>> 75ed1aee9a960782c7edb80f147d90878fe12d60
import pandas as pd


class LoanCalculator:
    """Handles the calculation of loan repayments."""

    def calculate_monthly_repayment(self, principal, monthly_interest_rate, loan_term_months):
<<<<<<< HEAD
=======
        """
        Calculates the monthly repayment for the loan.
        :param principal: The principal of the loan.
        :type principal: float
        :param monthly_interest_rate: The monthly interest rate.
        :type monthly_interest_rate: float
        :param loan_term_months: The loan term (months).
        :type loan_term_months: int
        :return: The monthly repayment.
        :rtype: float
        """
>>>>>>> 75ed1aee9a960782c7edb80f147d90878fe12d60
        return principal * (monthly_interest_rate * (1 + monthly_interest_rate) ** loan_term_months) / \
            ((1 + monthly_interest_rate) ** loan_term_months - 1)

    def calculate_balances(self, car_price, monthly_interest_rate, loan_term_months, monthly_admin_fee, start_date):
<<<<<<< HEAD
=======
        """
        Calculates the monthly balances for the loan.
        :param car_price: The price of the car.
        :type car_price: float
        :param monthly_interest_rate: The monthly interest rate.
        :type monthly_interest_rate: float
        :param loan_term_months: The loan term (months).
        :type loan_term_months: int
        :param monthly_admin_fee: The monthly admin fee.
        :type monthly_admin_fee: int
        :param start_date: The start date of the loan.
        :type start_date: pandas.Timestamp
        :return: The monthly balances.
        :rtype: pandas.DataFrame
        """
>>>>>>> 75ed1aee9a960782c7edb80f147d90878fe12d60
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
