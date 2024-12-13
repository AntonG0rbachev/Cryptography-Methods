import time


def gcdex(a, b):
    if b == 0:
        return a, 1, 0
    else:
        d, x, y = gcdex(b, a % b)
    return d, y, x - y * (a // b)

def porjadok(a, b, p):
#находит перебором количество всех точек: все конечные точки кривой y^2=x^3+ax+b в поле GF(p) + одна бесконечная
    s=1 #всегда есть одна точка -бесконечная, Е=О
    for x in range(p): #перебераем х от 0 до <p, то есть до p-1
        y2 = (pow(x, 3) + a * x + b) % p
        for y in range(0, p):
            if (pow(y, 2) % p) == y2:
                s += 1
    return s

def porjadoktime(a, b, p):
#находит перебором количество всех точек: все конечные точки кривой y^2=x^3+ax+b в поле GF(p) + одна бесконечная
#эта версия команды дополнительно считает время выполнения команды
    now1 = time.time() #запоминаем время начала работы
    s=porjadok(a, b, p)
    now2 = time.time()
    delta = now2 - now1
    print(f'Порядок кривой y^2 = x^3 + {a}x + {b} (mod {p}) равен {s}.' 
        f'Время выполнения: {delta} сек')

def proba(a,b,p):
    """
    перебирает все конечные точки кривой y^2=x^3+ax+b в поле GF(p)
    если точка лежит на кривой, то функция возвращает эту точку и заканчивает работу
    """
    for x in range(1,p):
        y2=(pow(x,3)+a*x+b)%p
        for y in range(0,p):
            if (pow(y,2)%p)==y2:
                return x,y

def obr(a, b):
    """
    Находит а^(-1) mod b, то есть такое с, что ac=1(mod b)
    """
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

print(gcdex(2*864,2539))

n = 11
x1 = 5
y1 = 94
a = 1
default = 1451
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

p3 = summ((74, 28), (2, 64))
print(f'3P = 2P + P = {p3}')

p7 = summ((161 ,71), p3)
print(f'7P = 4P + 3P = {p7}')

p23 = summ((116 ,29), p7)
print(f'23P = 16P + 7P = {p23}')

p151 = summ((210 ,8), p23)
print(f'151P = 128P + 23P = {p151}')


print(f'proba: {proba(1, 0, 2539)}')
print(f'porjadok: {porjadok(1, 0, 2539)}')
porjadoktime(1, 0, 2539)

p20 = summ((2257 ,210), (628 ,2255))
print(f'20P = 16P + 4P = {p20}')

p508 = summ((2221 ,614), (628 ,2255))
p508 = summ(p508, (2257 ,210))
p508 = summ(p508, (1743 ,2324))
p508 = summ(p508, (617 ,2425))
p508 = summ(p508, (2274 ,375))
p508 = summ(p508, (700 ,2124))

print(f'508P = 256P + 128P + 64P + 32P + 16P + 8P + 4P = {p508}')

p1270 = summ((628 ,2255), (2201 ,29))
p1270 = summ(p1270, (2257 ,210))
p1270 = summ(p1270, (1743 ,2324))
p1270 = summ(p1270, (617 ,2425))
p1270 = summ(p1270, (2274 ,375))
p1270 = summ(p1270, (1526 ,2109))
print(f'1270𝑃 = 1024P + 128P + 64P + 32P + 16P + 4P + 2P = {p1270}')

p10 = summ((2221 ,614), (2201 ,29))
print(f'10P = 8P + 2P = {p10}')

p254 = summ((628 ,2255), (2201 ,29))
p254 = summ(p254, (2221 ,614))
p254 = summ(p254, (2257 ,210))
p254 = summ(p254, (1743 ,2324))
p254 = summ(p254, (617 ,2425))
p254 = summ(p254, (2274 ,375))
print(f'254P = 128P + 64P + 32P + 16P + 8P + 4P + 2P = {p254}')

p635 = summ((2221 ,614), p3)
p635 = summ(p635, (2257 ,210))
p635 = summ(p635, (1743 ,2324))
p635 = summ(p635, (617 ,2425))
p635 = summ(p635, (832 ,647))
print(f'635P = 512P + 64P + 32P + 16P + 8P + 3P = {p635}')