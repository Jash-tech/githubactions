from src.math_operation import add,sub

def test_add():
    assert add(2,3)==5
    assert add(3,3)==6
    assert add(7,3)==10

def test_sub():
    assert sub(2,3)==-1
    assert sub(3,3)==0
    assert sub(7,3)==4