import math

def decimal_to_binary(decimal_number, precision):
  """
  Переводит десятичное число в двоичную систему счисления.

  Args:
    decimal_number: Десятичное число.
    precision: Точность.

  Returns:
    Двоичное число.
  """

  binary_number = 0
  for i in range(precision):
    binary_number += decimal_number / 2 ** i
    decimal_number %= 2 ** i

  return binary_number


decimal_number = 154.56
precision = 3

binary_number = decimal_to_binary(decimal_number, precision)

print(binary_number)
