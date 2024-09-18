from src import calculator
import pytest


@pytest.mark.skip
def test_add():
    assert calculator.add(2,0) == 2
    assert calculator.add(-2,0) == -2
    assert calculator.add(2,-200) == -198
    assert calculator.add(-2,-900) == -902

def test_sub():
    assert calculator.sub(2,0) == 2
    assert calculator.sub(-2,0) == -2
    assert calculator.sub(2,-200) == 202
    assert calculator.sub(-2,-900) == 898

test_data = [(2,0,0),(100,1000,100000),(-20,-90,1800),(-2,0,0),(200,2,400)]
@pytest.mark.parametrize('input1,input2,exp_result',test_data)
def test_mul(input1,input2,exp_result):
    assert calculator.mul(input1,input2) == exp_result
    

def test_div():
    assert calculator.div(2,0) == None
    assert calculator.div(-2,0) == None
    assert calculator.div(200,-200) == -1
    assert calculator.div(-1800,-900) == 2

def test_square_root():
    assert calculator.get_square_root(400) == 20
    assert calculator.get_square_root(100) == 10
    assert calculator.get_square_root(49) == 7
    assert calculator.get_square_root(169) == 13 

day = 29
@pytest.mark.skipif(day  < 28,reason="Day must be more than or equal 28")
def test_bill_notification():
    assert 1 > 0
