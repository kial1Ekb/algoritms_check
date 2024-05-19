"""
Напишите программу на выбранном вами языке программирования для вычисления временной сложности алгоритма сортировки
массива. Программа должна генерировать массив случайных чисел, сортировать его выбранным алгоритмом (например,
сортировка пузырьком или быстрая сортировка) и измерять время выполнения операции сортировки.
"""

import random
import time

def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[len(arr) // 2]
        left = [x for x in arr if x < pivot]
        middle = [x for x in arr if x == pivot]
        right = [x for x in arr if x > pivot]
        return quicksort(left) + middle + quicksort(right)

def generate_random_array(size):
    return [random.randint(0, 10000) for _ in range(size)]

def measure_sort_time(arr):
    start_time = time.time()
    sorted_arr = quicksort(arr)
    elapsed_time = time.time() - start_time
    return elapsed_time

def main():
    array_size = int(input("Введите размер массива: "))
    arr = generate_random_array(array_size)
    time_taken = measure_sort_time(arr)
    print(f"Время, затраченное на сортировку массива размером {array_size}: {time_taken:.6f} секунд.")

if __name__ == "__main__":
    main()
