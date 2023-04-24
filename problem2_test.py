#! python3

import problem2

def test1():
    assert problem2.triangle(12,5,13) == 2
    assert problem2.triangle(3,3,4) == 3
    #is the second one supposed to be wrong??? 
    #im not sure if im supposed to change it or if it's supposed to dectect an error

def test2():
    assert problem2.triangle(-2,1,5) == 0
    assert problem2.triangle(1,1,5) == 0
    assert problem2.triangle(-2,6,6) == 0
    
if __name__ == "__main__":
  test1()
  test2()