from playwright.sync_api import expect

class FloatExpect:
  def __init__(self, _int: float) -> None:
    self.verifyFloat(_int)
    self._int = float(_int)

  def verifyFloat(self, _int: float):
    if not isinstance(_int, (int, float)):
      try:
        float(_int)
      except Exception:
        raise TypeError(f"Expected integer but got {type(_int)}")

  def toEqual(self, expected: float):
    self.verifyFloat(expected)
    assert self._int == float(expected)

  def toBeBiggerThan(self, expected: float):
    self.verifyFloat(expected)
    assert self._int > float(expected)

  def toBeSmallerThan(self, expected: float):
    self.verifyFloat(expected)
    assert self._int < float(expected)

class StrExpect:
  def __init__(self, _string: str) -> None:
    self.verifyStr(_string)
    self._string = _string

  def verifyStr(self, _string: str):
    if not isinstance(_string, str):
      raise TypeError(f"Expected string but got {type(_string)}")

  def contains(self, expected: str):
    self.verifyStr(expected)
    assert self._string.__contains__(expected)

  def toEqual(self, expected: str):
    self.verifyStr(expected)
    assert self._string == expected

  def toStartWith(self, expected: str):
    self.verifyStr(expected)
    assert self._string.startswith(expected)

  def toEndWith(self, expected: str):
    self.verifyStr(expected)
    assert self._string.endswith(expected)

class ListExpect:
  def __init__(self, _list: list) -> None:
    self.verifyList(_list)
    self._list = _list

  def verifyList(self, _list: list):
    if not isinstance(_list, list):
      raise TypeError(f"Expected list but got {type(_list)}")

  def toHaveLengthOf(self, expected: list):
    self.verifyList(expected)
    assert len(self._list) == expected

class Expect():
  ui = expect
  str: StrExpect = StrExpect
  num: FloatExpect = FloatExpect
  lst: ListExpect = ListExpect
  # def __init__(self):