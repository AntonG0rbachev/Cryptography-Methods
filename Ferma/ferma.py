"""
Простой и эффективный метод факторизации чисел, основанный на идее,
что любое нечетное составное число N можно представить как разность квадратов
    N = x^2 − y^2 = (x − y)(x + y)
"""
import time
import math
import sys

from QuickPow.quick_pow import quick_pow


def is_square(n):
    root = int(math.sqrt(n))
    return quick_pow(root, 2) == n


def ferma(n):
    """
    Алгоритм Ферма используется для разложения числа N на два множителя.

    ! Метод Ферма способен раскладывать на множители только нечетные составные числа,
    ! но его эффективность зависит от определённых свойств этих чисел

    1. Начинаем с минимального значения x, где
    x = ceil(sqrt(N)) (округляем вверх квадратный корень N).
    2. Вычисляем y^2 = x^2 − N.
    3. Проверяем, является ли y^2 точным квадратом:
        а) Если да, то y = sqrt(y) и N = (x - y)(x + y) - множители найдены
        б) Если нет, увеличиваем x на 1 и повторяем шаги.
    4. Останавливаемся, когда множители найдены.
    """
    begin = time.time()
    if n % 2 == 0:
        return 2, n // 2

    x = math.ceil(math.sqrt(n))
    y = x * x - n

    while not is_square(y):
        x += 1
        y = x * x - n
        print(time.time() - begin)

    y = int(math.sqrt(y))

    print(time.time() - begin)
    return x - y, x + y


if __name__ == '__main__':
    args = sys.argv

    defaults = {
        'number': 343307067711615047372182962356629442952289267108875003956201,
    }
    parts: tuple = ()
    start = time.time()

    if len(args) <= 1:
        number = defaults['number']
        parts = ferma(number)

    elif args[-2] == '-n' or '--number':
        number = int(args[-1]) if args[-1] is not None else defaults['number']
        parts = ferma(number)

    else:
        raise Exception('There are no needed arguments')

    print(f"Число {number} раскладывается на множители: {parts[0]} и {parts[1]}")
    print(f"Время выполнения: {time.time() - start} секунд")
