def has_curve_point(point, a, b, p=2017):
    x, y = point
    y2 = pow(y, 2) % p
    curve = (pow(x, 3) + a * x + b) % p
    if y2 == curve:
        return True
    return False


points = [
    (15, 163),
    (16, 586),
    (23, 1800),
    (108, 100)
]

for p in points:
    if has_curve_point(p, 27, 12):
        print(p)
