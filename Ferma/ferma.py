import time
import math


def is_square(n):
    root = int(math.sqrt(n))
    return root ** 2 == n


def ferma(n):
    if n % 2 == 0:
        return 2, n // 2

    x = math.isqrt(n) + 1
    y = x * x - n

    while not is_square(y):
        x += 1
        y = x * x - n

    y = int(math.sqrt(y))
    return x - y, x + y


if __name__ == '__main__':
    number = 12
    start = time.time()
    parts = ferma(number)
    print(f"Число {number} раскладывается на множители: {parts[0]} и {parts[1]}")
    print(f"Время выполнения: {time.time() - start} секунд")
