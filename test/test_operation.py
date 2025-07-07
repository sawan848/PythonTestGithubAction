from src.math_operation import add,sub



def test_add():
    assert add(2,3)==5
    assert add(2,1)==3
    assert add(5,3)==8
    assert add(4,3)==7



def test_sub():    
    assert sub(5,3)==2
    assert sub(3,1)==2
    assert sub(4,2)==2
    
