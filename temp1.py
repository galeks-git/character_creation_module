
from math import sqrt


def calc(your_number):
    """Вычисляет квадратный корень."""
    if your_number <= 0:
        return
    print(f'Мы вычислили квадратный корень из введённого вами числа. '
          f'Это будет:{sqrt(your_number)}')


message = '''Добро пожаловать в самую лучшую программу для вычисления
             квадратного корня из заданного числа'''
print(message)
calc(25.5)
