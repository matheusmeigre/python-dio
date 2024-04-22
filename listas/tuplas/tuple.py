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

primeiro_resultado = nomes.index("Matheus")
print(f"Resultado: {primeiro_resultado}")

segundo_resultado = nomes.index("Marcos")
print(f"Resultado: {segundo_resultado}")

terceiro_resultado = nomes.index("Julio")
print(f"Resultado: {terceiro_resultado}")

quarto_resultado = nomes.index("Roberta")
print(f"Resultado: {quarto_resultado}")

quinto_resultado = nomes.index("Venicio")
print(f"Resultado: {quinto_resultado}")

