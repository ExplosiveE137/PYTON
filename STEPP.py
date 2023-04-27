import math


def step(x, p, a):
    k = int(math.log2(x))
    i = int(0)
    y = int(1)
    while i <= k:
        if x % 2 != 0:
            d = int(2 ** i)
            b = int(1)
            while d > 0:
                b = (b % p * a % p) % p
                d -= 1
            y = (y % p * b % p) % p
        x = x // 2
        i += 1
    return y

