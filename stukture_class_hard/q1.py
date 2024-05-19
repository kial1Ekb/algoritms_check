"""
Напишите программу на выбранном вами языке программирования, которая решает задачу коммивояжера для небольшого набора
городов. Программа должна определить оптимальный маршрут, учитывая временную сложность алгоритма и класс сложности,
к которому он относится.
"""

import itertools
import sys


def calculate_total_distance(route, distance_matrix):
    """ Функция для расчёта общего расстояния маршрута """
    total_dist = 0
    number_of_cities = len(route)
    for i in range(number_of_cities):
        total_dist += distance_matrix[route[i - 1]][route[i]]
    return total_dist


def traveling_salesman(distance_matrix):
    """ Решение задачи коммивояжёра методом полного перебора """
    cities = range(len(distance_matrix))
    shortest_route = None
    min_distance = sys.maxsize

    for route in itertools.permutations(cities):
        current_distance = calculate_total_distance(route, distance_matrix)
        if current_distance < min_distance:
            min_distance = current_distance
            shortest_route = route

    return shortest_route, min_distance


def main():
    distance_matrix = [
        [0, 10, 15, 20],
        [10, 0, 35, 25],
        [15, 35, 0, 30],
        [20, 25, 30, 0]
    ]

    # Находим оптимальный маршрут и его длину
    route, distance = traveling_salesman(distance_matrix)
    print("Оптимальный маршрут:", route)
    print("Длина маршрута:", distance)


if __name__ == "__main__":
    main()
