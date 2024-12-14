import random

from ferma import ferma
from miller_rabin import generate_prime
from utils import quick_pow, gcd


def diffie_hellman(p, g):
    """Алгоритм Диффи–Хеллмана"""
    a = random.randint((p - 1) // 10, p - 1)
    b = random.randint((p - 1) // 10, p - 1)

    A = quick_pow(g, a, p)
    B = quick_pow(g, b, p)

    K_alice = quick_pow(B, a, p)
    K_bob = quick_pow(A, b, p)

    return a, A, b, B, K_alice, K_bob


def factorize(n):
    factors = set()

    while n > 1:
        factor1, factor2 = ferma(n)
        factors.add(factor1)
        factors.add(factor2)

        n //= factor1
        n //= factor2

    return factors


def is_generator(g, p, factors):
    for f in factors:
        if quick_pow(g, (p - 1) // f, p) == 1:
            return False
    return True


def find_g(p):
    factors = factorize(p - 1)

    for g in range(2, p - 1):
        if not quick_pow(g, (p - 1), p) == 1:
            continue

        if is_generator(g, p, factors):
            return g

    raise ValueError('Не получилось найти генератор')


if __name__ == '__main__':
    p = generate_prime(10)
    g = find_g(p)
    a, A, b, B, K_alice, K_bob = diffie_hellman(p, g)
    print(f"Простое число (p): {p}")
    print(f"Основание (g): {g}")
    print(f"Секрет Алисы (a): {a}")
    print(f"Секрет Боба (b): {b}")
    print(f"Открытый ключ Алисы (A): {A}")
    print(f"Открытый ключ Боба (B): {B}")
    print(f"Общий ключ, вычисленный Алисой: {K_alice}")
    print(f"Общий ключ, вычисленный Бобом: {K_bob}")