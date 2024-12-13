import random
from sympy import gcd, mod_inverse


def generate_prime_candidate(length):
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
    bits = 8 
    public_key, private_key = generate_keypair(bits)

    print("Public Key:", public_key)
    print("Private Key:", private_key)

    message = "Hello"
    print("Original Message:", message)

    encrypted_msg = encrypt(public_key, message)
    print("Encrypted Message:", encrypted_msg)

    decrypted_msg = decrypt(private_key, encrypted_msg)
    print("Decrypted Message:", decrypted_msg)