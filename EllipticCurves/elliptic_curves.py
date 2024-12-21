import time


def gcdex(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcdex(b, a % b)
    return d, y, x - y * (a // b)


def porjadok(a, b, p):
    s = 1
    for x in range(p):
        y2 = (pow(x, 3) + a * x + b) % p
        for y in range(0, p):
            if (pow(y, 2) % p) == y2:
                s += 1
    return s


def porjadoktime(a, b, p):
    now1 = time.time()
    s = porjadok(a, b, p)
    now2 = time.time()
    delta = now2 - now1
    print(
        f'Порядок кривой y^2 = x^3 + {a}x + {b} (mod {p}) равен {s}.\n'
        f'Время выполнения: {delta} сек'
    )


def proba(a, b, p):
    for x in range(1, p):
        y2 = (pow(x, 3) + a * x + b) % p
        for y in range(0, p):
            if (pow(y, 2) % p) == y2:
                return x, y


def obr(a, b):
    g = gcdex(a, b)
    if g[0] == 1:
        return g[1] % b
    else:
        return 0


def summ(first, second):
    k = ((second[1] - first[1]) * obr((second[0] - first[0]), default)) % default
    x = (k * k - (first[0] + second[0])) % default
    y = (k * (first[0] - x) - first[1]) % default
    return x, y


p = 419
a = 1
b = 0
default = p

# Найдём точку P
P = proba(a, b, p)
print(f"Точка P: {P}")

# Порядок кривой
porjadoktime(a, b, p)

# Вычисление 151P
n = 7
x1, y1 = P
array = [[x1, y1]]

for i in range(n):
    k = (3 * x1 * x1 + a) * gcdex(2 * y1, default)[1] % default
    x = (k * k - 2 * x1) % default
    y = (k * (x1 - x) - y1) % default
    print(f'{2 ** (i + 1)}P = ({x} ,{y})')
    x1 = x
    y1 = y
    array.append([x1, y1])

print(array)
