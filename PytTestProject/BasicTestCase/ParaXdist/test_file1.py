import pytest
import time


def test_one():
    time.sleep(2)
    assert 1+1 ==2

def test_two():
    time.sleep(2)
    assert 2*2 == 4

def test_three():
    time.sleep(2)
    assert 3**2 == 9

def test_four():
    time.sleep(2)
    assert 3//3 == 1.0

#pytest-xdist
#pytest -n 3 file_name
#regression testing


#python
#selenium
#Pytest
#GIT
#Mongo
#SQL
#Unix
#manul

#exception selenium
#Jenkins + Pytest
#docker env
# Project