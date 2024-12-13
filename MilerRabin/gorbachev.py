import random
import datetime


def nod(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def choose_e(e, fi):
    k = 0
    while k < 1000:
        e = random.randint(100, 1000)
        if nod(e, fi) == 1:
            return e
    return False


def choose_d(e, fi):
    d = 1
    while (e * d) % fi != 1:
        d += 1
    return d


p = 1621
q = 4483
n = p * q
fi = (p - 1) * (q - 1)
e = choose_e(0, fi)
print(f'e is {e}')
d = choose_d(e, fi)
print(f'd is {d}')
m = (int(input('Input m: ')))

c = pow(m, e, n)
print(f'c if {c}')
decr = pow(c, d, n)
print(f'decrypted is {decr}')
keys = nod(p - 1, q - 1)
print(keys)

surname = 'Gorbachev'

codes = [(ord(ch) - 64) for ch in surname]
print(codes)
encrypted_word = [pow(m, e, n) for m in codes]
print(f'encrypted is {encrypted_word}')
decrypted_word = [pow(c, d, n) for c in encrypted_word]
print(f'decrypted is {decrypted_word}')
print(''.join([chr(char + 64) for char in decrypted_word]))

start_key = 2
while pow(encrypted_word[0], start_key, n) != decrypted_word[0]:
    start_key += 1
print(start_key)


def miller_rabin(n, k=5):
    """
    Тест Миллера-Рабина для проверки числа на простоту.
    n - проверяемое число
    k - количество раундов теста (точность проверки)
    БЕЗ БЫСТРОГО ВОЗВЕДЕНИЯ В СЕПЕНЬ
    """
    n = n - 1
    s = 0
    t = n
    while t % 2 == 0:
        s += 1
        t /= 2
    for _ in range(k):
        a = random.randint(2, n)
        x = pow(a, int(t), n + 1)
        if x == 1 or x == n:
            continue
        for j in range(s - 1):
            x = pow(x, 2, n + 1)
            if x == 1:
                return False
            if x == n:
                break
        return False
    return True


if __name__ == '__main__':
    start = datetime.datetime.now()
    default_simple = [3, 5, 7, 9, 11, 13, 17, 19]
    k = int(input("Введите длину: "))
    a = random.randint(2 ** (k - 1), 2 ** k)
    if a % 2 == 0:
        a += 1

    flag = False
    step = 1
    while not flag:
        for simple in default_simple:
            if a % simple == 0:
                flag = False
                step += 1
                a += 2
                break
        flag = miller_rabin(a, 5)
        if not flag:
            a += 2
            step += 1

    print(f"Simple is {a}, шаг is {step}, time is {datetime.datetime.now() - start}")
