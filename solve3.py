# Десятичное число
number = -4249

# Основание шестнадцатеричной системы счисления
base = 16

# Дополнительный код
complement = 0xFFFF - number

# Запись дополнительного кода в ячейку памяти
memory_cell = complement.to_bytes(2, byteorder="big")

# Вывод значения ячейки памяти
print(memory_cell)
