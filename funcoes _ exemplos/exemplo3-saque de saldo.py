def sacar(saldo):

    montante = float(input("Quanto deseja sacar? "))

    saldo = saldo - montante

    return saldo

    



saldo = float(input("Informe o saldo total: "))

qtde = int(input("Quantos saques vc deseja? "))

for c in range(qtde):
    saldo = sacar(saldo)


print("Saldo final: ", saldo)







