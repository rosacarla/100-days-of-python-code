#Soma de valores aleatórios (neutralizar com elemento neutro da soma ou 0)
print("Digite uma sequência de valores terminada por zero.")
soma = 0

valor = 1
while valor != 0:
    valor = int(input("Digite um valor a ser somado: "))
    soma = soma + valor

print("A soma dos valores digitados é: ", soma)
#Desafio - pede a quantidade de nros da sequencia e limita com o último 


#Produto de nros (neutralizar com elemento neutro da multiplicação ou 1) 
tamanho = int(input("Digite o tamanho da sequência de números: "))

produto = 1
i = 0

while i < tamanho:
    valor = int(input("Digite um valor a ser multiplicado: "))
    produto = produto * valor
    i = i + 1

print("O produto dos valores digitados é: ", produto)
#Programa para calcular soma dos dígitos de nro inteiro (exemplo 6532)
#Lembrar do resto da divisão inteira por 10 para tirar um dígito com while
x = 6532
x % 10 (resta 2)
x // 10 (mostra 653)
