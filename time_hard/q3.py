"""
Создайте программу, которая анализирует временную и пространственную сложности алгоритма поиска минимального элемента
в массиве. Программа должна генерировать массив чисел, выполнять поиск минимального элемента и выводить информацию о
времени выполнения и использованной памяти.
"""

import random
import time
import tracemalloc
import sys


def find_minimum_element(arr):
    """ Функция для поиска минимального элемента в массиве """
    return min(arr)


def generate_random_array(size):
    """ Генерация массива случайных чисел заданного размера """
    return [random.randint(0, 10000) for _ in range(size)]


def analyze_algorithm():
    """ Анализ временной и пространственной сложности алгоритма поиска минимального элемента """
    array_size = int(input("Введите размер массива: "))
    arr = generate_random_array(array_size)

    # Измерение времени выполнения
    start_time = time.time()
    min_element = find_minimum_element(arr)
    elapsed_time = time.time() - start_time

    # Измерение использования памяти
    tracemalloc.start()
    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Минимальный элемент в массиве: {min_element}")
    print(f"Время выполнения поиска: {elapsed_time:.6f} секунд.")
    print(f"Пиковое использование памяти: {peak / 1024:.2f} KB")


if __name__ == "__main__":
    analyze_algorithm()
