MAIOR_IDADE = 18
IDADE_ESPECIAL = 17

idade = int(input("Informe sua idade:"))

if idade >= 18:
    print("Maior de idade, acesso completo liberado.")

else:
    print("Menor de idade, acesso bloqueado para as aulas de rua.")

if idade == IDADE_ESPECIAL:
    print("Acesso liberado para aulas teóricas.")

elif idade <= IDADE_ESPECIAL:
    print("Não atinge idade para aulas teóricas, acesso negado.")