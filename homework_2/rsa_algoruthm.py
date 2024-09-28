import random
from sympy import gcd, mod_inverse

def generate_prime_candidate(length):
    p = random.getrandbits(length)
    return p | (1 << length - 1) | 1

def is_prime(n, k=128):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0:
        return False

    r, d = 0, n - 1
    while d % 2 == 0:
        d //= 2
        r += 1

    for _ in range(k):
        a = random.randint(2, n - 2)
        x = pow(a, d, n)
        if x == 1 or x == n - 1:
            continue
        for _ in range(r - 1):
            x = pow(x, 2, n)
            if x == n - 1:
                break
        else:
            return False
    return True

def generate_prime_number(length):
    p = 4
    while not is_prime(p, 128):
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

# Пример использования
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