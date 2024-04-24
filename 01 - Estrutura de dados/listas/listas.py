"""
Fatiamento de strings
 É uma tecnica utilizada para retornar substrings(partes da string original), informando
 INICIO(START), FIM(STOP) e [PASSO(STEP)]
 Exemplo:
 lista[inicio:fim:step]
"""
lista = ["p","y","t","h","o","n"]

lista[2:] # ["t", "h", "o", "n"]
lista[:2] # ["p", "y"]
lista[1:3] # ["y", "t"]
lista[0:3:2] # ["p", "t"]
lista[::] # ["p", "y", "t", "h", "o", "n"]
lista[::-1] # ["n", "o", "h", "t", "y", "p"]