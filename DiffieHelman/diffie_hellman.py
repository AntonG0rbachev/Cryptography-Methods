import random
import sys

from Ferma.ferma import ferma
from MilerRabin.miller_rabin import generate_prime
from QuickPow.quick_pow import quick_pow

from sympy import isprime


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


def find_generator(p):
    """
    Находит генератор g для простого числа p.
    """
    if not isprime(p):
        raise ValueError("p должно быть простым числом.")

    factors = factorize(p - 1)
    for g in range(2, p):
        valid = True
        for q in factors:
            if pow(g, (p - 1) // q, p) == 1:
                valid = False
                break
        if valid:
            return g
    return None


if __name__ == '__main__':
    args = sys.argv

    defaults = {
        'counts': 10,
    }
    counts = None
    p = None
    g = None
    a = None
    b = None
    A = None
    B = None
    alice_key = None
    bob_key = None

    if len(args) <= 1:
        counts = defaults['counts']

    elif args[-2] == '-c' or '--counts':
        counts = int(args[-1]) if args[-1] else defaults['counts']

    else:
        raise Exception('There are no needed arguments')

    p = generate_prime(counts)
    g = find_generator(p)
    a, A, b, B, alice_key, bob_key = diffie_hellman(p, g)
    print(f"Простое число (p): {p}")
    print(f"Основание (g): {g}")
    print(f"Секрет Алисы (a): {a}")
    print(f"Секрет Боба (b): {b}")
    print(f"Открытый ключ Алисы (A): {A}")
    print(f"Открытый ключ Боба (B): {B}")
    print(f"Общий ключ, вычисленный Алисой: {alice_key}")
    print(f"Общий ключ, вычисленный Бобом: {bob_key}")
