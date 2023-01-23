import logging

def maxSingleDigit(int_list: list):
  index = 0
  for i in int_list:
    minus = False
    if i < 0:
      minus = True
      i = i * (-1)
    if len(str(i)) > 1:
      continue
    if minus:
      i = i * (-1)
    if i > int_list[index]:
      index = int_list.index(i)
  logging.info(f"{int_list} => {int_list[index]}")
  return int_list[index]
