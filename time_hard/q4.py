"""
Напишите программу на любом языке программирования, которая проводит анализ временной сложности алгоритма поиска
определенного элемента в двоичном дереве поиска. Программа должна создавать случайное двоичное дерево поиска, выполнять
поиск указанного элемента и измерять время выполнения операции.
"""

import random
import time

class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    """ Вставка ключа в двоичное дерево поиска """
    if root is None:
        return TreeNode(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def search(root, key):
    """ Поиск ключа в двоичном дереве поиска """
    if root is None or root.val == key:
        return root
    if root.val < key:
        return search(root.right, key)
    return search(root.left, key)

def create_random_bst(n):
    """ Создание случайного двоичного дерева поиска """
    root = None
    for _ in range(n):
        key = random.randint(1, 100)
        root = insert(root, key)
    return root

def measure_search_time(root, key):
    """ Измерение времени выполнения поиска элемента """
    start_time = time.time()
    node = search(root, key)
    elapsed_time = time.time() - start_time
    if node:
        print(f"Элемент {key} найден.")
    else:
        print(f"Элемент {key} не найден.")
    print(f"Время поиска: {elapsed_time:.6f} секунд.")

def main():
    n = int(input("Введите количество элементов в дереве: "))
    key = int(input("Введите элемент для поиска: "))
    root = create_random_bst(n)
    measure_search_time(root, key)

if __name__ == "__main__":
    main()



"""
Временная сложность поиска в сбалансированном двоичном дереве поиска составляет 
𝑂(log𝑛)
O(logn), однако в худшем случае (когда дерево вырождается в связный список) она может достигать 
𝑂(𝑛). Создание случайного дерева не гарантирует его сбалансированность, что может отразиться на результатах измерения времени поиска.
"""