"""
Создайте программу, которая моделирует работу алгоритма решения задачи выполнимости булевой формулы (SAT). Программа
должна принимать булеву формулу, проверять ее выполнимость и определять, принадлежит ли задача к классу P, NP, co-NP
или PSPACE.
"""

import itertools


def is_satisfiable(formula, variables):
    """ Проверяет, выполнима ли булева формула. """
    for values in itertools.product([True, False], repeat=len(variables)):
        assignment = dict(zip(variables, values))
        if evaluate(formula, assignment):
            return True, assignment
    return False, None


def evaluate(formula, assignment):
    """ Оценивает формулу, используя заданное назначение значений. """
    # Заменяем переменные на их значения в формуле и выполняем вычисление
    local_formula = formula[:]
    for variable, value in assignment.items():
        local_formula = local_formula.replace(variable, str(value))
    return eval(local_formula)


def main():
    # "(A or not B) and (B or C)"
    formula = input("Введите булеву формулу: ")
    variables = sorted(set(filter(str.isupper, formula)))

    satisfiable, assignment = is_satisfiable(formula, variables)
    if satisfiable:
        print("Формула выполнима. Пример назначения переменных:", assignment)
    else:
        print("Формула не выполнима.")


if __name__ == "__main__":
    main()
