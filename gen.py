import random


def rand_key(p):
    key1 = []

    for i in range(p):
        key1.append(int(random.randint(0, 1)))
    return key1
