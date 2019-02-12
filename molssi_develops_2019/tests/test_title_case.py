"""
Unit and regression test for the molssi_math module
"""

# Import package, test suite, and other packages as needed
import molssi_develops_2019 as md
import pytest
import sys

def test_title_case():
    test_string="This is a string"
    observed = md.title_case(test_string)
    expected = "This Is A String"
    assert observed == expected

def test_empty_string():
    with pytest.raises(IndexError):
        md.title_case("")
