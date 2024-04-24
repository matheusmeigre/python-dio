#AND = para ser True todos precisam ser True
#OR = para ser True apenas um precisa ser True

saldo = 500
saque = 200
limite = 100

#Operador Lógico "e"
res = saldo >= saque and saque <= limite
print(res)

#Operador Lógico "ou"
res = saldo >= saque or saque <= limite
print(res)

#Operador Lógico "Negação"
contatos_emergencia = []
res = not 1000 > 1500
print(res)

res = not contatos_emergencia 
print(res)

res = not "saque 1500;"
print(res)

res = not ""
print(res)

#Operador Lógico com "Parênteses"
saldo = 1000
saque = 250
limite = 200
conta_especial = True

exp = saldo >= saque and saque <= limite or conta_especial and saldo >= saldo
print(exp)


exp_2 = (saldo >= saque and saque <= limite) or (conta_especial and saldo >= saldo)
print(exp_2)
