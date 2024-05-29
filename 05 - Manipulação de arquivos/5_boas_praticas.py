from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    with open(ROOT_PATH / "lorem.txt", "r") as file:
        print(file.read())
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")


try:
    with open(ROOT_PATH / "novo-arquivo-texto.txt", "w", encoding="utf-8") as file:
        file.write("Aprendendo a manipular arquivos em Python")
except IOError as exc:
    print(f"Erro ao abrir o arquivo {exc}")