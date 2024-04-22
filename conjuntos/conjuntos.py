"""
Sets(conjuntos)
 Um set é uma coleção que não possui objetos repetidos, usamos sets para representar conjuntos
 matemáticos ou eliminar itens duplicados de um iterável.
"""

numeros = set([1,2,3,1,3,4])
print(numeros)

letras = set("abacaxi")
print(letras)

carros = set(("gol", "celta", "palio", "gol", "voyage"))
print(carros)

linguagens = {"python", "java", "python"}
print(linguagens)


# Acessando os valores
print(f"\nAcessando os valores")
numeros = {1,2,3,4}
numeros = list(numeros)
print(numeros[0])