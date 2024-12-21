"""
Этот алгоритм используется для решения задачи дискретного логарифма, например:
g^x == h (mod p)
Цель - найти такое х, что g^x mod p == h
"""
from QuickPow.quick_pow import quick_pow


def baby_step_giant_step(n, p, g, a):
    """
    Вычисляет дискретный логарифм x в уравнении g^x ≡ h (mod p)
    методом 'шаг великана, шаг карлика'.
    n - порядок группы
    p - модуль
    g - основание
    h - значение
    """
    m = int(p ** 0.5) + 1
    print(f'm = sqrt({p}) + 1 = {m}')
    b = quick_pow(g, m, p)
    print(f'b = {g}^{m}(mod {p}) = {b}')

    giant_steps = {}

    for i in range(1, m + 1):
        giant_steps[quick_pow(b, i, p)] = i

    print(giant_steps)

    for j in range(1, m + 1):
        v = a * quick_pow(g, j, p) % p

        if v in giant_steps:
            i = giant_steps[v]
            return (m * i - j) % n

    return None


if __name__ == '__main__':
    p = 251
    n = 250
    g = 11
    a = 172

    print(baby_step_giant_step(n, p, g, a))


