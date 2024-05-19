"""
Напишите программу, которая использует алгоритм оптимизации (например, генетический алгоритм или алгоритм имитации
отжига) для нахождения оптимального расписания занятий в учебном заведении. Программа должна учитывать различные
ограничения и критерии оптимизации.
"""

import random

class Schedule:
    def __init__(self):
        self.classes = []  # Список занятий с информацией о времени и месте проведения

    def fitness(self):
        # Оценка расписания: меньше конфликтов и простоев — лучше
        return -self.count_conflicts()

    def count_conflicts(self):
        # Подсчёт количества конфликтов (например, два занятия одновременно в одной аудитории)
        return len(self.classes)  # Заглушка для простоты

    def mutate(self):
        # Случайная мутация расписания
        if self.classes:
            self.classes[random.randint(0, len(self.classes) - 1)] = None  # Пример мутации

def crossover(schedule1, schedule2):
    # Кроссовер: создание нового расписания на основе двух существующих
    new_schedule = Schedule()
    split = len(schedule1.classes) // 2
    new_schedule.classes = schedule1.classes[:split] + schedule2.classes[split:]
    return new_schedule

def genetic_algorithm(population_size=100, generations=50):
    population = [Schedule() for _ in range(population_size)]

    for generation in range(generations):
        population.sort(key=lambda x: x.fitness(), reverse=True)
        next_generation = population[:2]  # Элитизм: два лучших расписания переходят в новое поколение

        while len(next_generation) < population_size:
            # Селекция
            parent1, parent2 = random.sample(population[:50], 2)  # Турнирная селекция из лучших 50%
            # Кроссовер
            child = crossover(parent1, parent2)
            # Мутация
            child.mutate()
            next_generation.append(child)

        population = next_generation
        print(f"Поколение {generation}, лучшее значение функции приспособленности: {population[0].fitness()}")


genetic_algorithm()
