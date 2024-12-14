def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def quick_pow(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result


def extended_euclid(a, b):
    x0, x1, y0, y1 = 1, 0, 0, 1

    while b != 0:
        q, a, b = a // b, b, a % b
        x0, x1 = x1, x0 - q * x1
        y0, y1 = y1, y0 - q * y1

    return a, x0, y0


def inverse(e, phi):
    gcd, x, y = extended_euclid(e, phi)
    if gcd != 1:
        return None
    return x % phi
