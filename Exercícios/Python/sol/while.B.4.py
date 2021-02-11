# B.4. Cree un programa que imprima una pirámide vacía de la altura ingresada por el usuario. Por ejemplo:
#
# Para altura 6:
# ```
#      *
#     * *
#    *   *
#   *     *
#  *       *
# ***********
# ```


n = int(input("Número: "))

if n > 0:
    print((n-1)*" ", end="")
    print("*")

piso = 2
while piso < n:
    print((n-piso)*" ", end="")
    print("*", end="")
    print((2*piso-3)*" ", end="")
    print("*")
    piso += 1

if n > 1:
    print((2*n-1)*"*")
