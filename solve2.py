# Максимальное десятичное число
max_number = 46

# Основание тринадцатеричной системы счисления
base = 13

# Список десятичных чисел
numbers = []

# Цикл по всем десятичным числам от 1 до max_number
for number in range(1, max_number + 1):
  # Получение тринадцатеричной записи числа
  number_in_base13 = f"{number:02d}"

  # Проверка, что тринадцатеричная запись числа оканчивается цифрой 7
  if number_in_base13[-1] == "7":
    # Добавление числа в список
    numbers.append(number)

# Вывод списка чисел
print(numbers)
