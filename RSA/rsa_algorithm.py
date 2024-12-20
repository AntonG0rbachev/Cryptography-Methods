"""
Алгоритм RSA (Rivest-Shamir-Adleman) — это асимметричный криптографический алгоритм,
используемый для шифрования, расшифрования и цифровой подписи.
Он основан на сложности факторизации больших чисел, что обеспечивает высокую степень безопасности.

- Обеспечивает передачу данных через открытый канал,
где один ключ используется для шифрования, а другой — для расшифрования.
- Обеспечивает аутентификацию отправителя и проверку целостности сообщения.

Безопасность RSA основана на том, что:
1. Легко перемножить два больших простых числа p и q, чтобы получить n = p ⋅ q
2. Сложно разложить n на множители p и q, если n достаточно велико.
Это позволяет создать два связанных ключа:
- Открытый ключ (e,n) — используется для шифрования.
- Закрытый ключ (d,n) — используется для расшифрования.
"""
import random
import sys

from sympy import gcd, mod_inverse


def generate_prime_candidate(length):
    """
    создаёт случайное нечётное число заданной длины в битах,
    которое является кандидатом в простые числа
    """
    p = random.getrandbits(length)
    return p | (1 << length - 1) | 1


def is_prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d * d <= n and n % d != 0:
        d += 2
    return d * d > n


def generate_prime_number(length):
    p = 4
    while not is_prime(p):
        p = generate_prime_candidate(length)
    return p


def generate_keypair(bits):
    p = generate_prime_number(bits)
    q = generate_prime_number(bits)
    
    n = p * q

    # Вычисляем функцию эйлера
    phi = (p - 1) * (q - 1)

    e = random.randrange(2, phi)
    
    g = gcd(e, phi)
    while g != 1:
        e = random.randrange(2, phi)
        g = gcd(e, phi)

    d = mod_inverse(e, phi)

    return (e, n), (d, n)


def encrypt(public_key, plaintext):
    e, n = public_key
    cipher_text = [pow(ord(char), e, n) for char in plaintext]
    return cipher_text


def decrypt(private_key, cipher_text):
    d, n = private_key
    plain_text = ''.join([chr(pow(char, d, n)) for char in cipher_text])
    return plain_text


if __name__ == '__main__':
    args = sys.argv

    defaults = {
        'bits': 8,
        'message': 'Hello World'
    }
    bits = None
    message = None

    if len(args) <= 1:
        bits = defaults['bits']
        message = defaults['message']
    else:
        args = args[1::]
        args_map = dict()
        if len(args) % 2 != 0:
            raise Exception("there's not enough argument")
        for i in range(0, len(args) - 1, 2):
            args_map[args[i]] = args[i + 1]
        bits = float(args_map['-b']) if '-b' in args_map.keys() else defaults['bits']
        message = args_map['-m'] if '-m' in args_map.keys() else defaults['message']

    public_key, private_key = generate_keypair(bits)

    print("Публичный ключ:", public_key)
    print("\nПриватный ключ:", private_key)
    print("\nИсходное сообщение:", message)

    encrypted_msg = encrypt(public_key, message)
    print("\nЗашифрованное сообщение:", encrypted_msg)

    decrypted_msg = decrypt(private_key, encrypted_msg)
    print("\nРасшифрованное сообщение:", decrypted_msg)
