from pathlib import Path

ROOT_PATH = Path(__file__).parent

try:
    file = open("meu_arquivo.py", "r")
except FileNotFoundError as exc:
   print("Arquivo não encontrado")
   print(exc)

