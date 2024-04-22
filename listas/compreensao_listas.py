""" List comprehension oferece uma sintaxe mais curta quando você deseja criar uma nova lista
com base nos valores de uma lista existente (filtro) ou gerar uma nova lista.
"""

# Filtro 1
numeros = [1,30,21,2,9,65,34]
pares = []
for numero in numeros:
    if numero % 2 == 0:
        pares.append(numero)
        print(numero)


# Filtro 2 
numeros = [1,30,21,2,9,65,34]
pares = [numero for numero in numeros if numero % 2 == 0]
print(pares)