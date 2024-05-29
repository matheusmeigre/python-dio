import csv
from pathlib import Path

ROOT_PATH = Path(__file__).parent

#try:
#    with open(ROOT_PATH / "usuarios.csv", "w", newline='', encoding="utf-8") as file:
#        escritor = csv.writer(file)
#        escritor.writerow(["id", "Nome"])
#        escritor.writerow(["1", "Maria"])
#        escritor.writerow(["2", "Joao"])
#except IOError as exc:
#    print(f"Erro ao criar o arquivo. {exc}")

# Modelo de leitura com o reader sem a identação do DictReader
try:
    with open(ROOT_PATH / "usuarios.csv", "r", newline='', encoding="utf-8") as file:
        leitor = csv.reader(file)
        for row in leitor:
            print(row)
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")
    

# Modelo de leitura com o DictReader que utiliza melhor da leitura com identação
try:
    with open(ROOT_PATH / "usuarios.csv", "r", newline='', ) as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            print(f"ID: {row['id']}")
            print(f"Nome: {row['Nome']}")
except IOError as exc:
    print(f"Erro ao criar o arquivo. {exc}")