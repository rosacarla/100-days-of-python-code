# Escreva um algoritmo que receba cinco números do usuário e imprima a metade de cada número.
# Mostre a soma de todas metades ao final.

soma = 0

qtde = int(input("Quantos numeros vc ira informar? "))

for c in range(qtde):

    n = float(input("Informe N: "))

    metade = n / 2

    print(metade)

    soma = soma + metade

print("Soma: ", soma)
