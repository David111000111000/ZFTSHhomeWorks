# Алфавит
alphabet = "АБВГДЕЖЗИЙКЛМНОПРСТУФХЦЧШЩЪЫЬЭЮЯ"

# Функция, которая возвращает порядковый номер буквы в алфавите
def get_letter_number(letter):
  """
  Возвращает порядковый номер буквы в алфавите.

  Args:
    letter: Буква.

  Returns:
    Порядковый номер буквы.
  """

  return alphabet.find(letter) + 1

# Номер слова
number = 41161

# Получение слова
word = ""
for i in range(6):
  word += alphabet[get_letter_number(number % 10)]
  number //= 10

# Вывод слова
print(word)
