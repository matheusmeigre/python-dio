class Bicicleta:
    def __init__(self, cor, modelo, ano, valor):
        self.cor = cor
        self.modelo = modelo
        self.ano = ano
        self.valor = valor

    def buzinar(self):
        print("BI-BI-BI!!!")


    def parar(self):
        print("Freio acionado, você parou!")

 
    def correr(self):
        print("Sigam-me os bons, iremos atingir alta velocidade!")


    def __str__(self):
        return f"{self.__class__.__name__}: {', '.join([f'{chave}={valor}' for chave, valor in self.__dict__.items()])}"


monark_nova = Bicicleta("vermelha", "bmx aro 20", 2020, 2000)
gios_usada = Bicicleta("verde", "ultra aro 26", 2019, 700)

monark_nova.buzinar()  # Bicicleta.buzinar(monark_nova)

print(monark_nova.cor)

