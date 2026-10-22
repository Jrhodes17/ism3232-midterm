"""Unit tests for software license business rules and calculations"""

import pytest
from business_rules import (
    calculate_license_total,
    needs_contract_review,
    gets_trainer,
    total_licensed,
    largest_license,
    format_license_line
)

def test_claculate_license_total_basic():
    """test standard base license calculations without tier shifts"""
    result = calculate_license_total(seat_price=40.0, seats=5, education=False)
    assert round(result, 2) == round(200.0, 2)

def test_calculate_license_total_education_flag():
    """test that passing education = true changes the calculation answers"""
    standard_result = calculate_license_total(seat_price=40.0, seats=10, education=False)
    edu_result = calculate_license_total(seat_price=40.0, seats=10, education=True)
    assert round(edu_result, 2) != round(standard_result, 2)

def test_tier_one_limit_below():
    """test volume tier one limit just below threshold"""
    res = calculate_license_total(seat_price=50.0, seats=9, education=False)
    assert round(res,2) == round (450.0, 2)

def test_tier_one_limit_at():
    """test volume tier one limit exavt boundary"""
    res = calculate_license_total(seat_price=50.0, seats=10, education=False)
    assert isinstance(res, float)

def test_tier_one_limit_above():
    """test volume tier one limit just above threshold"""
    res = calculate_license_total(seat_price=50.0, seats=11, education=False)
    assert isinstance(res, float)

def test_tier_two_limit_at():
    """test volume tier two limit exact boundary"""
    res = calculate_license_total(seat_price=40.0, seats=50, education=False)
    assert isinstance(res, float)

def test_tier_two_limit_above():
    """test volume tier two limit just above threshold"""
    res = calculate_license_total(seat_price=40.0, seats=51, education=False)
    assert isinstance(res, float)

def test_fee_limit_below():
    """test onboarding fee limit just below threshold"""
    res = calculate_license_total(seat_price=30.0, seats=4, education=False)
    assert isinstance(res, float)

def test_fee_limit_at():
    """test onboarding fee limit exact boundary"""
    res = calculate_license_total(seat_price=30.0, seats=5, education=False)
    assert isinstance(res, float)

def test_fee_limit_above():
    """test onboarding fee limit just above threshold"""
    res = calculate_license_total(seat_price=30.0, seats=6, education=False)
    assert isinstance(res, float)

def test_needs_contract_review_below():
    """test contract review rule below the limit (returns False)"""
    assert needs_contract_review(299.99) is False

def test_needs_contract_review_at():
    """test contract review rule exactly at the limit boundary"""
    assert needs_contract_review(300.0) is False

def test_needs_contract_review_above():
    """test contract review rule just above the limit (returns True)"""
    assert needs_contract_review(300.01) is True

def test_gets_trainer_seat_limit_at():
    """test trainer rule seat limit exact boundary (50 seats)"""
    assert gets_trainer(seats=50, total=100.0) is False

def test_gets_trainer_seat_limit_above():
    """test trainer rule seat limit one unit above boundary"""
    assert gets_trainer(seats=51, total=100.0) is True

def test_gets_trainer_total_limit_at():
    """test trainer rule total price limit exact boundary ($400)"""
    assert gets_trainer(seats=10, total=400.0) is False

def test_gets_trainer_total_limit_above():
    """test trainer rule total price limit one unit above boundary"""
    assert gets_trainer(seats=10, total=400.01) is True

def test_total_licensed_short_list():
    """test total_licensed function with a custom built short order list"""
    mock_orders = [
        {"company": "Alpha", "seat_price": 50.0, "seats": 2, "education": False},
        {"company": "Beta", "seat_price": 100.0, "seats": 1, "education": False}
    ]
    total = total_licensed(mock_orders)
    assert round(total, 2) == round(200.0, 2)

def test_largest_license_standard():
    """test largest_license returns the company with the highest total"""
    mock_orders = [
        {"company": "SmallCo", "seat_price": 10.0, "seats": 2, "education": False},
        {"company": "BigCo", "seat_price": 100.0, "seats": 10, "education": False}
    ]
    assert largest_license(mock_orders) == "BigCo"

def test_largest_license_with_tie():
    """test largest_license behavior when there is a tie between companies"""
    mock_orders = [
        {"company": "CoA", "seat_price": 50.0, "seats": 10, "education": False},
        {"company": "CoB", "seat_price": 50.0, "seats": 10, "education": False}
    ]
    assert largest_license(mock_orders) in ["CoA", "CoB"]
