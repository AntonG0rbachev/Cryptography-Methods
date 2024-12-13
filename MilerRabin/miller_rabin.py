import random

from QuickPow.quick_pow import quick_pow


def miller_rabin(n, k=5):
    """
    Тест Миллера-Рабина для проверки числа на простоту.
    n - проверяемое число
    k - количество раундов теста (точность проверки)
    С БЫСТРЫМ ВОЗВЕДЕНИЕМ В СТЕПЕНЬ
    Алгоритм
    1. Представить n − 1 в виде 2s·t, где t нечётно,
    можно сделать последовательным делением n - 1 на 2.
    2. цикл А: повторить k раз:
        а) Выбрать случайное целое число a в отрезке [2, n − 2]
        x ← at mod n, вычисляется с помощью алгоритма возведения
        в степень по модулю
        б) если x = 1 или x = n − 1,
        то перейти на следующую итерацию цикла А
    3. цикл B: повторить s − 1 раз
        а) x ← x2 mod n
        б) если x = 1, то вернуть составное
        в) если x = n − 1, то перейти на следующую итерацию цикла A
        г) вернуть составное
        д) вернуть вероятно простое
    """
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    s, d = 0, n - 1
    while d % 2 == 0:
        s += 1
        d //= 2

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = quick_pow(a, d, n)
        if x == 1 or x == n - 1:
            continue

        for _ in range(s - 1):
            x = quick_pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False

    return True


def generate_number(k):
    if k == 1:
        return 1
    if k == 2:
        return 3
    p = random.randint(2 ** (k - 1), 2 ** k - 1)
    return int(f'{bin(p)[:-1]}1', 2)


def generate_prime(k):
    while True:
        p = generate_number(k)
        if miller_rabin(p, 5):
            return p


if __name__ == '__main__':
    k = 10
    prime_number = generate_prime(k)
    print(f"Сгенерированное простое число: {prime_number}")
