import pytest


@pytest.fixture(scope='function')
def multiply_fixture():
    num1 = 10
    num2 = 20
    result = num2*num1
    return result

def test_multiply_opeartion(multiply_fixture):
    assert multiply_fixture == 200