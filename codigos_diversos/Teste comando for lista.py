#Exemplo comando for
print("Exemplo 1 - impressão de lista\n")
lista = [10,11,12,13,14,15]
for valor in lista:
    print(valor)

#Exemplos com for e range
print("\n\nExemplo 2 - lista até 4\n")
for valor in range(5):
    print(valor)

print("\n\nExemplo 3 - lista em intervalo\n")
for valor in range(4,8):
    print(valor)

#Exemplo com for para string
print("\n\nExemplo 4 - lista de caracteres\n")
texto = "Python"
for caracter in texto:
    print(caracter)

#Exemplo variável contadora de caracteres de frase
print("\n\nExemplo 5 - contagem de caracteres\n")
frase = "A ligeira raposa marrom ataca o cão preguiçoso."
qtdeLetras = 0
for letra in frase:
    qtdeLetras += 1

print("A frase (",frase,") possui "+str(qtdeLetras)+" letras.\n")

#Exemplo variável acumuladora de valores númericos
print("\n\nExemplo 6 - cálculo de média\n")
dados = [1,3,5,8,10,2]

soma = 0
qtde = 0

for valor in dados:
    soma += valor
    qtde += 1

print("Dados = [1,3,5,8,10,2]")
print("\nSoma = ",soma)
print("\nQtde = ",qtde)

media = soma/qtde

print("\nMédia = {:.2f}".format(media))

#Exemplo variável acumuladora de valores numéricos
print("\n\nExemplo 7 - soma nros pares até 10")
soma = 0

for numero in range(10):
    if (numero%2) == 0:
        soma += numero
        
print("\nA soma é igual a ",soma,".")

#Exemplo variável contadora de valores numéricos
print("\n\nExemplo 8 - contar múltiplos de 3(Z) nos primeiros 20 de N\n")
noVerificados = 0
noMultiplos = 0
soma = 0

for numero in range(20):
    noVerificados += 1
    if (numero%3) == 0:
        noMultiplos+= 1
        soma += numero

print("\nNros verificados: ",noVerificados)
print("\nMúltiplos de 3: ",noMultiplos)
print("\nSoma: ",soma)















             

    
