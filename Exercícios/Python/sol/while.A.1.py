# A.1. Cree un programa que reciba un número e imprime su factorial.

n = int(input("Número: "))
factorial = 1

while n > 0:
    factorial *= n
    n -= 1

print(factorial)
