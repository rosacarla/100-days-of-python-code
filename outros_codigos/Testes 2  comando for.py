#Exemplo de cálculo com modulo factorial
print("Exemplo 9 - módulo factorial do Guanabara\n")
from math import factorial
n = int(input("Digite um número para calcular seu Fatorial: \n"))
f = factorial(n)
print("\nO fatorial de {} é {}.".format(n, f))

#Exemplo de cálculo tradicional do fatorial
print("\n\nExemplo 10 - fatorial tradicional do Guanabara\n")
n = int(input("Digite um número para calcular seu Fatorial: \n"))
c = n
f = 1
print("Calculando {}! = ".format(c), end=" ")
while c > 0:
    print("{}".format(c), end=" ")
    print(" x " if c > 1 else " = ",end=" ")
    f *= c
    c -= 1
print("{}".format(f))

#Exemplo com for para cálculo de fatorial
print("\n\nExemplo 11 - cálculo de fatorial (livro)")
numero = int(input("\nDigite um número para calcular o fatorial: "))
c = numero
f = 1
for termo in range(1, (c+1)):
      f *= termo

print("\nO fatorial de " + str(c) + "! é : " + str(f))

#Exemplo com for para somar 2 listas de valores numéricos
print("\n\nExemplo 12 - soma dos valores de 2 listas")
A = [2,3,4]
B = [7,-3,2]

C = []

for indice in range(3):
    C.append(A[indice] + B[indice])

print("\nA soma das listas ",A," e ",B," é : ",C)

#Exemplo com for para determinar númros primos
print("\n\nExemplo 13 - encontrar nros primos")
numPrimos = []

for numero in range(20):
    div = 0
    for divisor in range(1, numero + 1):
        if (numero % divisor) == 0:
            div += 1
    if div == 2:
        numPrimos.append(numero)

print("\nOs números primos de 0 até 20 são: {}.".format(numPrimos))

#Exercicio comando for - 1
print("\n\nExercício 1\n")
varA = 3
varB = 0
for num in range(varA):
    varB += num ** 2
print(varB)

#Exercício comando for - 3 
print("\n\nExercício 3\n")
dados = [[1,2,3],[4,5,6],[7,8,9]]
for coluna in dados:
    print(coluna)

print("\n\nExercício 3 corrigido")
dados = [[1,2,3],[4,5,6],[7,8,9]]

for linha in dados:
    for coluna in linha:
        print(coluna)

#Exercício comando for - 4
print("\n\nExercício 4= 1 linha com 0")
tabela = []
contador = 0
for i in range(3):
    for j in range(3):
        tabela.append(contador)
        contador = contador + 1
print()
print(tabela)

print("\n\nExercício 4= 1 linha zerada")
tabela = []
contador = 0
for linha in tabela:
    for j in linha:
        tabela.append(contador)
        contador *= 1
print()
print(tabela)

print("\n\nExercício 4= 1 linha sem nº 1")
tabela = []
contador = 1
for linha in range(3):
    for coluna in range(3):
        contador += 1
        tabela.append(contador)
        
print()
print(tabela)

print("\n\nExercício 4 (D)= 3 linhas com 3 colunas ")
tabela = []
contador = 1
for i in range(3):
    linha = []
    for j in range(3):
        linha.append(contador)
        contador += 1
    tabela.append(linha)
        
print()
print(tabela)

print("\n\nExercício 4= ")
tabela = []
contador= 1
for linha in tabela:
    for coluna in linha:
        tabela.append(contador)
        contador+= 1
        
print()
print(tabela)

#Exercício comando for - 5
print("\n\nExercício 5 = tabuada do 1 a 10")
for numerador in range(10):
    print("Tabuada do número {}\n".format(numerador+1))
    for multiplicador in range(10):
        print((numerador+1)*(multiplicador+1))


        

    




















