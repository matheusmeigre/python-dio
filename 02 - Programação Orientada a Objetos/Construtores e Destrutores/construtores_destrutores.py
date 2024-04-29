class Cachorro:
    def __init__(self, nome, cor, acordado=True):
        self.nome = nome
        self.cor = cor
        self.acordado = acordado

    def __del__(self):
        print("Removendo a instância da classe")

    def latir(self):
        print("Auau")

    def dormir(self):
        self.acordado = False
        print("Zzzz...")

    def criar_cachorro():
        c = Cachorro("Zeus", "Branco e preto", False)
        print(c.nome)

c = Cachorro("Pandora", "Branco e preto")
c.latir()

del c