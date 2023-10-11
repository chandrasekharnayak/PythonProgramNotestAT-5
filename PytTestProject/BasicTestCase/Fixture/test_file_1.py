import pytest

@pytest.fixture
def numbers_setup(request):

    #Setup Code :- Create a list of numbers for testing
    numbers = [1,2,3,4,5,6,7,8,9,10]
    print(numbers)


    yield numbers

    numbers.clear()
    print(numbers)
    print('Teardown:- Cleaning up resourses after the text')


def test_even_odd_numbers(numbers_setup):
    numbers = numbers_setup

    result = [i%2==0 for i in numbers]

    expected_result = [False,True,False,True,False,True,False,True,False,True]
    assert result == expected_result


