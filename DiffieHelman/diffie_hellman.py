import random
import sys

from Ferma.ferma import ferma
from MilerRabin.miller_rabin import generate_prime
from QuickPow.quick_pow import quick_pow


def diffie_hellman(p, g):
    """
    Алгоритм Диффи–Хеллмана
    p - большое простое число
    g - генератор
    криптографический протокол, используемый для безопасного обмена ключами
    между двумя сторонами через открытый канал.
    Алгоритм:
    1. Публичные параметры. Стороны договариваются об общем большом простом числе
    p и генераторе g, который является первообразным корнем по модулю p.
    2. Генерация закрытых ключей. Алиса выбирает случайное число a (секретный ключ Алисы).
    Боб выбирает случайное число b (секретный ключ Боба).
    3. Обмен публичными ключами. Алиса вычисляет A=g^a mod p и отправляет его Бобу.
    Боб вычисляет B=g^b mod p и отправляет его Алисе.
    4. Генерация общего секрета. Алиса вычисляет s=B^a mod p,
    используя полученное значение B и свой секретный ключ a.
    Боб вычисляет s=A^b mod p, используя полученное значение
    A и свой секретный ключ  b.
    Обе стороны получают одно и то же значение s.
    """
    a = random.randint(1, p - 1)
    A = pow(g, a, p)

    b = random.randint(1, p - 1)
    B = pow(g, b, p)

    secret_alice = pow(B, a, p)
    secret_bob = pow(A, b, p)

    assert secret_alice == secret_bob, "Ошибка: общий секрет не совпадает!"
    return secret_alice


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
    args = sys.argv

    defaults = {
        'counts': 10,
    }
    p, g, a, b, A, B, alice_secret, bob_secret = None, None, None, None, None, None, None, None

    if len(args) <= 1:
        p = generate_prime(defaults['counts'])
        g = find_g(p)
        a, A, b, B, alice_secret, bob_secret = diffie_hellman(p, g)

    print(f"Простое число (p): {p}")
    print(f"Основание (g): {g}")
    print(f"Секрет Алисы (a): {a}")
    print(f"Секрет Боба (b): {b}")
    print(f"Открытый ключ Алисы (A): {A}")
    print(f"Открытый ключ Боба (B): {B}")
    print(f"Общий ключ, вычисленный Алисой: {K_alice}")
    print(f"Общий ключ, вычисленный Бобом: {K_bob}")