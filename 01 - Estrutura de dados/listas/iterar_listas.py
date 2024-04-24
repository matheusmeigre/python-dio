"""
 Percorrendo o array [CARROS] e retornando(print) os valores(carro) dentro dele
"""
carros = ["gol", "celta", "palio"]

for carro in carros:
    print(carro) # >>> gol, celta, palio




"""
 Percorrendo o array[CARROS] e retornando(print) os valores(carro) dentro dele junto
 ao índice(0,1,2,...)
"""
for indice, carro in enumerate(carros):
    print(f"{indice}: {carro}") # >>> 0: gol, 1: celta, 2: palio