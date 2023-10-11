# from TREENETRA_AT_5.PytTestProject.BasicTestCase.calculator import add_numbers
#
# def test_add_numbers():
#     result = add_numbers(2,3)
#     assert result == 5
#
#     result = add_numbers(-1,1)
#     assert result == 0
#
#     result = add_numbers(0,0)
#     assert result == 1


#Validate login page with Selenium Pytest

from TREENETRA_AT_5.PytTestProject.BasicTestCase.decore_cal import add

def test_decore():
    result = add(10,20)
    assert result == (200,30)

    result = add(-10,-20)
    assert result==(200,-30)

    result = add(-10,20)
    assert result==(-200,10)

    result = add(-10,0)
    assert result == (-10,-10)















