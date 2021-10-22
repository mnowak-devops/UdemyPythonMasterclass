def test_result1(xyfunc):
    result = round(xyfunc)
    #print(id(xyfunc))
    assert result == 894
    
def test_result2(xyfunc):
    result = round(xyfunc, 1)
    #print(id(xyfunc))
    assert result == 894.0
    
def test_result3(xyfunc):
    result = round(xyfunc, 2)
    #print(id(xyfunc))
    assert result == 894.01