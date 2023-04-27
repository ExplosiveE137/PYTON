def gcd(n, m):
    if m == 0:
        return 0
    else:
        return gcd(m, n % m)


def task(n, m):
    return gcd(n, m) == 1