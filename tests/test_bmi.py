import pytest
from src.bmi_calculator import calculate_bmi, bmi_category

def test_calculate_bmi():
    assert round(calculate_bmi(70, 1.75), 2) == 22.86

def test_bmi_category():
    assert bmi_category(17) == "Underweight"
    assert bmi_category(22) == "Normal weight"
    assert bmi_category(27) == "Overweight"
    assert bmi_category(32) == "Obesity"
