from utils import quick_pow


def baby_step_giant_step(n, p, g, a):
    m = int(p ** 0.5) + 1
    print(f'm = sqrt({p}) + 1 = {m}')
    b = quick_pow(g, m, p)
    print(f'b = {g}^{m}(mod {p}) = {b}')

    u = {}

    for i in range(1, m + 1):
        u[quick_pow(b, i, p)] = i

    print(u)

    for j in range(1, m + 1):
        v = a * quick_pow(g, j, p) % p

        if v in u:
            i = u[v]
            return (m * i - j) % n

    return None

if __name__ == '__main__':
    p = 251
    n = 250
    g = 11
    a = 172

    print(baby_step_giant_step(n, p, g, a))


