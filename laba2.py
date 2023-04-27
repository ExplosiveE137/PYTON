from elg import *
from RRSA import *
from Shel import *
from Vernam import *


def vib(n):
    if n == 1:
        Shel()
    if n == 2:
        elg()
    if n == 3:
        Ver()
    if n == 4:
        RRSA()


print("Выберите алгоритм шифрования")
print("1 - Шифр Шамира")
print("2 - Шифр Эль-Гамаля")
print("3 - Шифр Вернама")
print("4 - Шифр RSA")
print("0 - выход")
n = int(input())
while n != 0:
    vib(n)
    n = int(input())

