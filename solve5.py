def decimal_to_base(number, base):
  """
  Переводит десятичное число в систему счисления с основанием base.

  Args:
    number: Десятичное число.
    base: Основание системы счисления.

  Returns:
    Число в системе счисления с основанием base.
  """

  result = ""
  while number > 0:
    result = str(number % base) + result
    number //= base
  return result


def convert_to_64_base(number):
  """
  Переводит число из восьмеричной системы счисления в 64-ричную систему счисления.

  Args:
    number: Число в восьмеричной системе счисления.

  Returns:
    Число в 64-ричной системе счисления.
  """

  return decimal_to_base(int(number, 8), 64)


def convert_to_4_base(number):
  """
  Переводит число из шестнадцатеричной системы счисления в четверичную систему счисления.

  Args:
    number: Число в шестнадцатеричной системе счисления.

  Returns:
    Число в четверичной системе счисления.
  """

  return decimal_to_base(int(number, 16), 4)


number_1 = "741341,4251_8"
number_2 = "BD92CFA,8DA23_(16)"

print("Число `{}` в 64-ричной системе счисления равно `{}`.".format(
    number_1, convert_to_64_base(number_1)))
print("Число `{}` в четверичной системе счисления равно `{}`.".format(
    number_2, convert_to_4_base(number_2)))
