"""
Напишите программу на выбранном вами языке программирования, которая применяет аппроксимационный алгоритм для
нахождения приближенного решения задачи о рюкзаке. Программа должна оптимизировать заполнение рюкзака с учетом веса и
стоимости предметов.
"""

def knapsack(capacity, weights, values):
    """ Жадный алгоритм для задачи о рюкзаке. """
    # Сортировка предметов по убыванию ценности за единицу веса
    items = sorted(zip(values, weights), key=lambda x: x[0]/x[1], reverse=True)
    total_value = 0
    total_weight = 0

    for value, weight in items:
        if total_weight + weight <= capacity:
            # Добавляем полностью, если предмет помещается в рюкзак
            total_value += value
            total_weight += weight
        else:
            # Добавляем часть предмета, если он не помещается полностью
            remain = capacity - total_weight
            total_value += value * (remain / weight)
            break

    return total_value

def main():
    values = [60, 100, 120]
    weights = [10, 20, 30]
    capacity = 50

    max_value = knapsack(capacity, weights, values)
    print(f"Максимально возможная стоимость: {max_value}")

if __name__ == "__main__":
    main()
