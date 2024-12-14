

def lfsr(reg, pol_bits):
    new_bit = 0
    for bit in pol_bits:
        new_bit = new_bit ^ reg[-bit]

    return [new_bit] + reg[:-1]


def generate_sequence(reg, pol_bits, length):
    seq = [reg]
    for _ in range(length):
        val = lfsr(seq[-1], pol_bits)
        seq.append(val)

    return seq


if __name__ == "__main__":
    print(generate_sequence([1, 0, 0, 1], [1, 3], 13))
