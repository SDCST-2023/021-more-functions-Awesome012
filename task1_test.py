#! python3

import task1

def test1():
  assert task1.btcTocad(1) == 45000

def test2():
    assert task1.btcTocad(0.5) == 22500

if __name__ == "__main__":
  test1()
  test2()