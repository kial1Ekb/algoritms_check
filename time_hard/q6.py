"""
Создайте программу, которая проводит анализ временной и пространственной сложности алгоритма нахождения всех
подстрок в строке. Программа должна принимать строку в качестве ввода, находить все возможные подстроки и выводить
информацию о времени выполнения и использованной памяти.
"""


import time
import tracemalloc


def find_substrings(s):
    """ Функция для нахождения всех подстрок в строке """
    substrings = []
    n = len(s)
    for i in range(n):
        for j in range(i + 1, n + 1):
            substrings.append(s[i:j])
    return substrings


def measure_performance():
    """ Измерение временной и пространственной сложности нахождения всех подстрок """
    input_string = input("Введите строку: ")

    # Начало отслеживания использования памяти
    tracemalloc.start()
    start_time = time.time()

    # Вызов функции для нахождения всех подстрок
    substrings = find_substrings(input_string)

    # Измерение времени и использования памяти
    elapsed_time = time.time() - start_time
    current, peak = tracemalloc.get_traced_memory()

    tracemalloc.stop()

    print(f"Найдено {len(substrings)} подстрок.")
    print(f"Время выполнения: {elapsed_time:.6f} секунд.")
    print(f"Пиковое использование памяти: {peak / 1024:.2f} KB")


if __name__ == "__main__":
    measure_performance()
