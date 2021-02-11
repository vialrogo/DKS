# B.1. Cree un programa que imprima un triángulo de la altura ingresada por el usuario. Por ejemplo:
# 
# Para altura 6:
# ```
# *
# **
# ***
# ****
# *****
# ******
# ```


n = int(input("Número: "))
piso = 1

while piso <= n:
    print(piso*"*")
    piso += 1


# # Usando while anidados
# while piso <= n:
#     estrela = 1
#     while estrela <= piso:
#        print("*", end='')
#        estrela += 1
#     print()
#     piso += 1
