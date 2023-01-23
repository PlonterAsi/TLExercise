import pytest
from maxSingle import maxSingleDigit


def test_max_single():
  x = [-5, 94, 1001, -100, 76, 1, 0, 503]
  assert maxSingleDigit(x) == 1

def test_max_single_1():
  x = [5, 9, 201, -15, 6, 1, 0]
  assert maxSingleDigit(x) == 9

def test_max_single_2():
  x = [0, 10, 100, 1000, 8]
  assert maxSingleDigit(x) == 8

def test_max_single_3():
  x = [1, 2, 33, 44, 55 ,66 ,77, 88, 10, 9]
  assert maxSingleDigit(x) == 9

def test_max_single_4():
  x = [-1, -2, -3, -4, -5, -6, -7, -10, -8, -9]
  assert maxSingleDigit(x) == -1
