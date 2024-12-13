import random

from QuickPow.quick_pow import quick_pow


def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def hack_rsa(message, encrypted_message, N):
    private_key = 1
    iteration = 0
    while pow(encrypted_message, private_key, N) != message and iteration < 10000000:
        private_key += 1
        iteration += 1

    return private_key if iteration <= 10000000 else None


def extended_euclid(a, b):
    if b == 0:
        return a, 1, 0
    gcd, x1, y1 = extended_euclid(b, a % b)
    x = y1
    y = x1 - (a // b) * y1
    return gcd, x, y


def inverse(e, phi):
    gcd, x, y = extended_euclid(e, phi)
    if gcd != 1:
        return None
    return x % phi


if __name__ == '__main__':
    p = 1597
    q = 9091

    #p = 23961059477384564131190343336702055777048173521159
    #q = 95476111652833454996668837990853931697025543134309

    n = p * q
    print(f'p = {p}, q = {q}')
    print(f'n = {n}')

    # Приватный ключ: (n, d)
    # Публичный ключ: (n, e)

    phi = (p - 1) * (q - 1)
    print(f'phi = {phi}')

    # Подбор e
    # e: gcd(e, phi(n)) = 1
    e = random.randint(2, n)

    while gcd(e, phi) != 1:
        e = random.randint(2, n)

    print(f'e = {e}')

    # Подбор d
    # d: (e * d) % phi(n) = 1

    d = inverse(e, phi)
    print(f'd = {d}')

    print(f'Приватный ключ (n, d): {n, d}')
    print(f'Публичный ключ (n, e): {n, e}')

    print(f'Количество ключей шифрования: {gcd(q - 1, p - 1)}')

    print('\n\nШифрование числа')

    m = 48
    c = quick_pow(m, e, n)
    decrypted_m = quick_pow(c, d, n)

    # Взлом
    private_key = hack_rsa(m, c, n)

    print(f'Исходное число: m = {m}\nЗашифрованное: c = {c}\nРасшифрованное: decrypted_m = {decrypted_m}')

    if not private_key:
        print(f'\nНе получилось взломать!!')
    else:
        print(f'\nУспешный взлом, найденный ключ: {private_key}')
        print(f'Зашифрованное сообщение: {c}; Взломанное: {quick_pow(c, private_key, n)}')

    print('\n\n')
    print(f'Шифрование слова')

    message = 'Чернов'
    message_codes = [ord(letter) for letter in message]
    encrypted_codes = [quick_pow(m, e, n) for m in message_codes]
    decrypted_codes = [quick_pow(c, d, n) for c in encrypted_codes]

    print(f'Исходное сообщение: {message}')
    print(f'Перевод исходного сообщения в числа: {message_codes}')
    print(f'Зашифрованное сообщение: {encrypted_codes}')
    print(f'Расшифрование сообщения: {decrypted_codes}')
