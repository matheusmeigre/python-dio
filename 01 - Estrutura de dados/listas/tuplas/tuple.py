"""
Tuplas são estruturas de dados muito parecidas com as listas, a principal diferença é que
TUPLAS são IMUTÁVEIS enquanto LISTAS são MUTÁVEIS. Podemos criar tuplas através da classe
`tuple`, ou colocando valores separados por vírgulas de parenteses.
"""

frutas = ["laranja", "pera", "uva",]
letras = tuple("python")
numeros = tuple([1,2,3,4])
pais = ("Brasil",)

# Métodos da classe tuple .count()
cores = ("vermelho", "azul", "verde", "azul",)

resultado_vermelho = cores.count("vermelho")
print(f"Vermelho: {resultado_vermelho}")

resultado_azul = cores.count("azul")
print(f"Azul: {resultado_azul}")

resultado_verde = cores.count("verde")
print(f"Verde: {resultado_verde}")


# .index()

nomes = ("Matheus", "Marcos", "Julio", "Roberta", "Venicio",)

print("\nIndex method class down")

print(nomes.index("Matheus"))
print(nomes.index("Marcos"))
print(nomes.index("Julio"))
print(nomes.index("Roberta"))
print(nomes.index("Venicio"))


# .len()
print("\nLen method class down")

familia = ("Matheus", "Marcos", "Julio", "Roberta", "Venicio",)
print(len(familia))

