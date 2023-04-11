#! python3

import task3

def test1():
    assert task3.hypotenuse(6,8) == 10

def test2():
    assert task3.hypotenuse(5,12) == 13

if __name__ == "__main__":
  test1()
  test2()