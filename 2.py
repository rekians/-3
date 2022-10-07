a = int(input('введите первый катет:'))
b = int(input('введите второй катет:'))
S = (a * b)/2
from math import sqrt
P = sqrt(a*a + b*b) + a + b
print("площадь =", S)
print("периметр =", P)