# Площадь квадрата

from math import ceil


def square(a):
    s = a * a
    return s


a = float(input("Введите длину стороны: "))
result = square(a)
final_result = ceil(result)
print("Площадь квадрата с округлением: ", final_result)
