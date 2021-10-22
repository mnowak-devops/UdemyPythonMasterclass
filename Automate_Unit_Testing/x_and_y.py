import pandas
import pytest
import math
from unittest import mock

#Defining the function with 3 parameters
@pytest.fixture
def xyfunc():
    #Loading the Excel (r"C:\Udemy_Python_Masterclass\Automate_Unit_Testing\values.xlsx") values into a Pandas DataFrame
    df = pandas.read_excel(r"C:\Udemy_Python_Masterclass\Automate_Unit_Testing\values.xlsx")

    #The value of x
    x = float(df["Price"][0])

    #The value of y
    with mock.patch('builtins.input', return_value = 10):
        y = float(input("Enter the value of y: "))

    return math.pow(x / y, 2)

def test_result(xyfunc):
    result = round(xyfunc)
    assert result == 894