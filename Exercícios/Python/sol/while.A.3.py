# A.3. Cree un programa que reciba un número y devuelva los números primos entre 1 y dicho número. Por ejemplo, para la entrada 20 debe devolver la lista con los números 2, 3, 5, 7, 11, 13, 17, 19

from math import sqrt

n = int(input("Número: "))
candidato = 2

while candidato <= n:

    divisor = 2
    isPrimo = True

    while divisor <= sqrt(candidato):
        if candidato%divisor == 0:
            isPrimo = False
            break
        divisor += 1

    if isPrimo:
        print(candidato)

    candidato += 1
