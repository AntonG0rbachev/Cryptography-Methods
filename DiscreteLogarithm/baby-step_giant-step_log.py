"""
Этот алгоритм используется для решения задачи дискретного логарифма, например:
g^x == h (mod p)
Цель - найти такое х, что g^x mod p == h
"""
import sys

from QuickPow.quick_pow import quick_pow


def baby_step_giant_step(n, p, g, h):
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
        v = h * quick_pow(g, j, p) % p

        if v in giant_steps:
            i = giant_steps[v]
            return (m * i - j) % n

    return None


if __name__ == '__main__':
    args = sys.argv

    defaults = {
        'p': 251,
        'n': 250,
        'g': 11,
        'h': 58,
    }
    p, n, g, h = None, None, None, None

    if len(args) <= 1:
        p = defaults['p']
        n = defaults['n']
        g = defaults['g']
        h = defaults['h']

    else:
        args = args[1::]
        args_map = dict()
        if len(args) % 2 != 0:
            raise Exception("there's not enough argument")
        for i in range(0, len(args) - 1, 2):
            args_map[args[i]] = args[i + 1]
        p = float(args_map['-p']) if '-p' in args_map.keys() else defaults['p']
        n = float(args_map['-n']) if '-n' in args_map.keys() else p - 1 if '-p' in args_map.keys() else defaults['n']
        g = float(args_map['-g']) if '-g' in args_map.keys() else defaults['g']
        h = float(args_map['-h']) if '-h' in args_map.keys() else defaults['h']

    print(baby_step_giant_step(n, p, g, h))


