def sacar(valor):  # Abertura de bloco do método sacar
    saldo = 500

    if saldo >= valor: # Abertura de bloco do if
        print("valor sacado!")
        print("retire o valor no caixa.")

    print("Obrigado por ser nosso cliente, tenha um bom dia!")


def depositar(valor):   # Abertura de bloco do método depositar
    saldo = 500
    saldo += valor
                        # Fechamento de bloco


sacar(600)
