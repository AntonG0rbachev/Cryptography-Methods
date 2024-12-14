"""
Простой и эффективный метод факторизации чисел, основанный на идее,
что любое нечетное составное число N можно представить как разность квадратов
    N = x^2 − y^2 = (x − y)(x + y)
"""

import time
import math


def is_square(n):
    root = int(math.sqrt(n))
    return root ** 2 == n


def ferma(n):
    """
    Алгоритм Ферма используется для разложения числа N на два множителя.
    1. Начинаем с минимального значения x, где
    x = ceil(sqrt(N)) (округляем вверх квадратный корень N).
    2. Вычисляем y^2 = x^2 − N.
    3. Проверяем, является ли y^2 точным квадратом:
        а) Если да, то y = sqrt(y) и N = (x - y)(x + y) - множители найдены
        б) Если нет, увеличиваем x на 1 и повторяем шаги.
    4. Останавливаемся, когда множители найдены.
    """
    x = math.ceil(math.sqrt(n))
    while True:
        y_square = x * x - n
        y = int(math.sqrt(y_square))
        if y * y == y_square:
            p1 = x - y
            p2 = x + y
            return p1, p2
        x += 1


if __name__ == '__main__':
    number = 12
    start = time.time()
    parts = ferma(number)
    print(f"Число {number} раскладывается на множители: {parts[0]} и {parts[1]}")
    print(f"Время выполнения: {time.time() - start} секунд")
