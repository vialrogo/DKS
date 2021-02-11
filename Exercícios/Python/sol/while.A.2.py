# A.2. Cree un programa que reciba un número y diga si el número es primo o no
from math import sqrt

n = int(input("Número: "))

out = "Primo"
divisor = 2

while divisor <= sqrt(n):
    if n%divisor == 0:
        out = "Não primo"
        break
    divisor += 1

print(out)
