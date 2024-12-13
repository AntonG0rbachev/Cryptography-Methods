def quick_pow(base, exp, mod):
    result = 1
    base %= mod
    while exp > 0:
        if exp % 2 == 1:
            result = (result * base) % mod
        base = (base * base) % mod
        exp //= 2
    return result

if __name__ == '__main__':
    print(quick_pow(
        3212312312337846567834734567864357863457863451232342344,
        618970019642690137449562110,
        123123123)
    )