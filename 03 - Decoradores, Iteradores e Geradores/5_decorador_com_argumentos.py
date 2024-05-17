def meu_decorador(funcao):
    def envelope(*args, **kwargs):
        print("Faz algo antes de executar a funcao")
        funcao(*args, **kwargs)
        print("Faz algo depois de executar a funcao")


    return envelope


@meu_decorador
def ola_mundo(nome):
    print(f"Olá, mundo {nome}!")

ola_mundo('Davi')