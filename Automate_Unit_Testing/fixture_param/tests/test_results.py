def test_result1(xyfunc):
    result = round(xyfunc)
    assert result <= 1000
    #assert 0
    
def test_result2(xyfunc):
    result = round(xyfunc)
    assert result >= 0
    #assert 0