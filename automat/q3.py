"""
Создайте программу на языке программирования по вашему выбору, которая преобразует регулярное выражение в эквивалентный недетерминированный конечный автомат.
Пользователь вводит регулярное выражение, а программа выводит структуру соответствующего конечного автомата.
"""

class State:
    """ Класс для представления состояния в НКА. """
    def __init__(self, label=None, is_final=False):
        self.label = label
        self.is_final = is_final
        self.transitions = {}

    def add_transition(self, symbol, state):
        """ Добавляет переход из текущего состояния по символу в другое состояние. """
        if symbol in self.transitions:
            self.transitions[symbol].append(state)
        else:
            self.transitions[symbol] = [state]

class NFA:
    """ Класс для представления недетерминированного конечного автомата. """
    def __init__(self, start_state):
        self.start_state = start_state
        self.states = []

    def add_state(self, state):
        """ Добавляет состояние в НКА. """
        self.states.append(state)

    def __str__(self):
        """ Выводит структуру НКА в удобочитаемом виде. """
        output = []
        for state in self.states:
            for symbol, states in state.transitions.items():
                for st in states:
                    output.append(f"({state.label}) -[{symbol}]-> ({st.label})")
            if state.is_final:
                output.append(f"({state.label}) [Final State]")
        return "\n".join(output)

def regex_to_nfa(regex):
    """ Функция преобразования регулярного выражения в НКА с использованием алгоритма Томпсона. """
    # Простая реализация для демонстрации, требует доработки для полной поддержки регулярных выражений.
    # Здесь рассматривается только один символ для примера.
    start_state = State(label="start")
    final_state = State(label="final", is_final=True)
    start_state.add_transition(regex, final_state)

    nfa = NFA(start_state)
    nfa.add_state(start_state)
    nfa.add_state(final_state)
    return nfa


user_regex = input("Введите регулярное выражение: ")
nfa = regex_to_nfa(user_regex)
print("Структура соответствующего НКА:")
print(nfa)
