"""
 Criando Dicionários
  Um dicionário é um conjunto NÃO-ORDENADO de pares chave:valor, onde as CHAVES são
  ÚNICAS em uma data instância do dicionário. Dicionários são delimitados por chaves: {},
  e contém uma lista de pares chave:valor separada por vírgulas.
"""

pessoa = {"nome": "Matheus", "idade": 22}

pessoa = dict(nome="Matheus", idade=22)

pessoa["celular"] = "3333-4444" # {"nome": "Matheus", "idade": 28, "celular": "3333-4444"}

# Acessando os dados de um dicionário

dados = {"nome": "Matheus", "idade": 22, "celular": "3333-4444"}

dados["nome"] # "Matheus"
dados["idade"] # 22
dados["celular"] # "3333-4444"

dados["nome"] = "Lais"
dados["idade"] = 20
dados["celular"] = "2222-3333"

dados # {"nome": "Lais", "idade": 20, "celular": "2222-3333"}