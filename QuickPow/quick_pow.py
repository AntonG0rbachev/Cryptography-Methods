import sys


def quick_pow(base, exp, mod=None):
    """
    это метод, позволяющий вычислять a^b mod m (или просто a^b)
    за логарифмическое число операций по b
    1. Представляем число b в двоичном виде.
    2. Инициализируем результат res=1.
    3. Для каждой единицы в двоичной записи b,
    перемножаем результат на соответствующую степень a.
    4. Каждый раз, когда мы переходим к следующему биту,
    текущее основание a возводится в квадрат.
    5. Если модуль m задан, то вычисления выполняются по модулю m
    для предотвращения переполнения.
    """
    result = 1

    if mod:
        base %= mod

    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod if mod else (result * base)
        base = (base * base) % mod if mod else (base * base)
        exp //= 2

    return result


if __name__ == '__main__':
    args = sys.argv

    defaults = {
        'base': 3212312312337846567834734567864357863457863451232342344,
        'exp': 618970019642690137449562110,
        'mod': 123123123,
    }

    if len(args) <= 1:
        print(
            quick_pow(
                defaults['base'],
                defaults['exp'],
                defaults['mod']
            )
        )
    else:
        args = args[1::]
        args_map = dict()
        if len(args) % 2 != 0:
            raise Exception("there's not enough argument")
        for i in range(0, len(args) - 1, 2):
            args_map[args[i]] = args[i + 1]
        base = float(args_map['-b']) if '-b' in args_map.keys() else defaults['base']
        exp = float(args_map['-e']) if '-e' in args_map.keys() else defaults['exp']
        mod = float(args_map['-m']) if '-m' in args_map.keys() else defaults['mod']
        print(
            quick_pow(
                base,
                exp,
                mod,
            )
        )
