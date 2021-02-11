# B.2. Cree un programa que imprima un triángulo invertido de la altura ingresada por el usuario. Por ejemplo:
#
# Para altura 6:
# ```
# ******
#  *****
#   ****
#    ***
#     **
#      *
# ```

n = int(input("Número: "))
piso = n

while piso > 0:
    print((n-piso)*" ", end="")
    print(piso*"*")
    piso -= 1
