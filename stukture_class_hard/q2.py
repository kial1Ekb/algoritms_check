"""
Разработайте программу, которая использует алгоритм проверки на простоту числа для определения простых чисел в заданном
диапазоне. Программа должна выводить все найденные простые числа, учитывая класс сложности задачи и временные затраты
на выполнение.
"""

def sieve_of_eratosthenes(max_num):
    """ Функция, реализующая алгоритм 'Решето Эратосфена' для нахождения всех простых чисел до max_num """
    # Инициализация списка для отметки простых и составных чисел
    is_prime = [True] * (max_num + 1)
    p = 2
    while (p * p <= max_num):
        # Если is_prime[p] не изменено, значит p простое
        if (is_prime[p] == True):
            # Обновление всех кратных p, начиная с p^2
            for i in range(p * p, max_num + 1, p):
                is_prime[i] = False
        p += 1
    # Сбор всех простых чисел
    prime_numbers = [p for p in range(2, max_num + 1) if is_prime[p]]
    return prime_numbers

def main():
    max_num = int(input("Введите максимальное число для поиска простых чисел: "))
    prime_numbers = sieve_of_eratosthenes(max_num)
    print(f"Простые числа до {max_num}:", prime_numbers)

if __name__ == "__main__":
    main()
