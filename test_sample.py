from sklearn import datasets


def inc(x):
    return x+1 

def test_answer():
    assert inc(4)==5


def answer2_test():
    assert inc(4)==5

'''
def test_answer():
    assert inc(4)==5
'''

'''
class Test1:
    def __init__(self):
        df=0 
    def test_something(self):
        assert 1==2
'''

class Test2:
    def test_something(self):
        assert 2==2


'''



def test_getdata():
    X,y =read_digits() 
    assert len(X)>0 
    assert len(X)==len(y)
  
'''   
