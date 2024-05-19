"""
Напишите программу, которая на любом языке программирования реализует конечный автомат для проверки строки на
наличие подстроки "ab". При вводе строки программа должна выводить сообщение о наличии или отсутствии данной подстроки.
"""

def has_ab(s):
    # Состояния конечного автомата
    START = 0  # Начальное состояние
    FOUND_A = 1  # Найдена 'a'
    FOUND_AB = 2  # Найдена 'ab'

    state = START

    for char in s:
        if state == START:
            if char == 'a':
                state = FOUND_A
        elif state == FOUND_A:
            if char == 'b':
                state = FOUND_AB
                break
            else:
                state = START  # Возврат к начальному состоянию, если 'b' не следует за 'a'

    return state == FOUND_AB

# Тестирование функции
input_string = input("Введите строку: ")
if has_ab(input_string):
    print("Строка содержит подстроку 'ab'.")
else:
    print("Строка не содержит подстроку 'ab'.")
