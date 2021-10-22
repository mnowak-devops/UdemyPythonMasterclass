#These tests are meant for checking if certain conditions raise certain exceptions
import pytest
from unittest import mock
from calculator import calculator

class TestClass(object):
    def test_FileNotFoundError(self):
        with mock.patch('builtins.input', return_value = 10), pytest.raises(FileNotFoundError):
            calculator(r"C:\Udemy_Python_Masterclass\Automate_Unit_Testing\value.xlsx", 0)

    def test_KeyError(self):
        with mock.patch('builtins.input', return_value = 10), pytest.raises(KeyError):
            calculator(r"C:\Udemy_Python_Masterclass\Automate_Unit_Testing\values.xlsx", 7)

    def test_ZeroDivisionError(self):
        with mock.patch('builtins.input', return_value = 0), pytest.raises(ZeroDivisionError):
            calculator(r"C:\Udemy_Python_Masterclass\Automate_Unit_Testing\values.xlsx", 0)

#run with: D:\testing>pytest -rv --disable-warnings test_exceptions.py