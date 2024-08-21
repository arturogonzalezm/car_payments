import pytest
from unittest.mock import patch
from pandas import Timestamp
from src.loan_calculator import LoanCalculator


def test_monthly_repayment_calculates_correctly():
    calculator = LoanCalculator()
    result = calculator.calculate_monthly_repayment(10000, 0.01, 12)
    assert round(result, 2) == 879.16


def test_balances_calculate_correctly():
    calculator = LoanCalculator()
    result = calculator.calculate_balances(10000, 0.01, 12, 50, Timestamp("2022-01-01"))
    assert len(result) == 12
    assert round(result["Monthly Repayment"].iloc[0], 2) == 888.49
    assert round(result["Principal Paid"].iloc[0], 2) == 788.49
    assert round(result["Interest Paid"].iloc[0], 2) == 100.00
    assert result["Admin Fee"].iloc[0] == 50
    assert round(result["Total Payment"].iloc[0], 2) == 938.49
    assert round(result["Contract Balance"].iloc[0], 2) == 9211.51


def test_balances_calculate_correctly_with_zero_admin_fee():
    calculator = LoanCalculator()
    result = calculator.calculate_balances(10000, 0.01, 12, 0, Timestamp("2022-01-01"))
    assert len(result) == 12
    assert round(result["Monthly Repayment"].iloc[0], 2) == 888.49
    assert round(result["Principal Paid"].iloc[0], 2) == 788.49
    assert round(result["Interest Paid"].iloc[0], 2) == 100.00
    assert result["Admin Fee"].iloc[0] == 0
    assert round(result["Total Payment"].iloc[0], 2) == 888.49
    assert round(result["Contract Balance"].iloc[0], 2) == 9211.51
