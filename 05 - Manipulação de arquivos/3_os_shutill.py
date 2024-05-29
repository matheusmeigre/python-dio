import os
import shutil
from pathlib import Path

ROOT_PATH = Path(__file__).parent

# os.mkdir(ROOT_PATH / 'novo-diretorio')

#file = open(ROOT_PATH / "novo.txt", "w")
#file.close()

#os.rename(ROOT_PATH / "novo.txt", ROOT_PATH / "alterado.txt")

# os.remove(ROOT_PATH / "alterado.txt")

shutil.move(ROOT_PATH / "teste.txt", ROOT_PATH / "novo-diretorio" / "teste.txt")


