"""
Разработайте программу, которая оценивает пространственную сложность алгоритма быстрой сортировки. Программа должна
создавать массив данных, сортировать его методом быстрой сортировки и измерять объем используемой памяти в процессе
выполнения алгоритма.
"""

import random
import tracemalloc
import sys


def quicksort(arr):
    """ Рекурсивная функция быстрой сортировки """
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)


def generate_random_array(size):
    """ Генерация массива случайных чисел заданного размера """
    return [random.randint(0, 10000) for _ in range(size)]


def measure_memory_usage():
    """ Измерение памяти, используемой для сортировки массива """
    array_size = int(input("Введите размер массива: "))
    arr = generate_random_array(array_size)

    # Начало отслеживания использования памяти
    tracemalloc.start()

    snapshot1 = tracemalloc.take_snapshot()
    sorted_arr = quicksort(arr)
    snapshot2 = tracemalloc.take_snapshot()

    # Остановка отслеживания и анализ результатов
    memory_diff = snapshot2.compare_to(snapshot1, 'lineno')

    for stat in memory_diff[:10]:  # Показать первые 10 результатов
        print(stat)

    current, peak = tracemalloc.get_traced_memory()
    tracemalloc.stop()

    print(f"Текущее использование памяти: {current / 1024:.2f} KB")
    print(f"Пиковое использование памяти: {peak / 1024:.2f} KB")


if __name__ == "__main__":
    measure_memory_usage()
