#These tests are meant for checking the results of performing the calculations using each value in the DataFrame ("Price" column) and the same y value (10)
import sys
import pytest
from unittest import mock
from calculator import calculator

#Marking test functions
#more info: https://docs.pytest.org/en/latest/skipping.html#skip-and-xfail-dealing-with-tests-that-cannot-succeed
class TestClass(object):
    @pytest.mark.mytest
    def test_index0(self):
        with mock.patch('builtins.input', return_value = 10):
            assert calculator(r"C:\Udemy_Python_Masterclass\Automate_Unit_Testing\values.xlsx", 0) == 894

    @pytest.mark.mytest
    def test_index1(self):
        with mock.patch('builtins.input', return_value = 10):
            assert calculator(r"C:\Udemy_Python_Masterclass\Automate_Unit_Testing\values.xlsx", 1) == 3648

    @pytest.mark.mytest
    def test_index2(self):
        with mock.patch('builtins.input', return_value = 10):
            assert calculator(r"C:\Udemy_Python_Masterclass\Automate_Unit_Testing\values.xlsx", 2) == 207

    def test_lowervalue(self):
        with mock.patch('builtins.input', return_value = 10):
            assert calculator(r"C:\Udemy_Python_Masterclass\Automate_Unit_Testing\values.xlsx", 3) == 497

    def test_highervalue(self):
        with mock.patch('builtins.input', return_value = 10):
            assert calculator(r"C:\Udemy_Python_Masterclass\Automate_Unit_Testing\values.xlsx", 4) == 2025

#Running tests by marks
#run with: pytest -v --disable-warning -m mytest
#or:       pytest -v --disable-warning -m "not mytest"

#Running tests by names (or partial names)py
#run with: pytest -v --disable-warning -k lower
#or:       pytest -v --disable-warning -m "not lower"