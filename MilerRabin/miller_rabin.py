import random

from quick_pow import quick_pow


def miller_rabin_test(n, k=5):
    """
        Представить n − 1 в виде 2s·t, где t нечётно, можно сделать последовательным делением n - 1 на 2.
        цикл А: повторить k раз:
        Выбрать случайное целое число a в отрезке [2, n − 2]
        x ← at mod n, вычисляется с помощью алгоритма возведения в степень по модулю
        если x = 1 или x = n − 1, то перейти на следующую итерацию цикла А
        цикл B: повторить s − 1 раз
        x ← x2 mod n
        если x = 1, то вернуть составное
        если x = n − 1, то перейти на следующую итерацию цикла A
        вернуть составное
        вернуть вероятно простое
    """
    if n <= 1 or n % 2 == 0:
        return False

    # Представляем n - 1 как 2^s * d, где d - нечетное
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
    """Генерация простого числа"""
    while True:
        p = generate_number(k)
        if miller_rabin_test(p, 5):
            return p

if __name__ == '__main__':
    k = 10
    prime_number = generate_prime(k)
    print(f"Сгенерированное простое число: {prime_number}")
