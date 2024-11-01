#Exemplo sequencia de Fibonacci
print("\n\nExemplo 14 - gerar sequência de Fibonacci com menu")
controle = 1 #variavel de controle da repetição
#Laço de controle do menu interativo
while controle == 1:
    num = int(input("Digite quantos elementos você quer imprimir: "))
    a, b = 0, 1
    cont = 2  #variável contadora
    print("Sequencia de Fibonacci")
    print(a, b, end=" ")  #Imprime os dois primeiros valores
    #Laço de repetição para calcular a sequência
    while cont<num:
        a, b = b, a+b   #atualiza os valores da sequencia
        print (b, end=" ")   #Imprime o valor atual da sequencia
        cont+=1  #Incrementa a variável contadora
    print()   #quebra de linha
    #Menu interativo para repetir o cálculo da sequencia
    controle = int(input("Digite 1 para continuar ou 0 para parar: "))

#Exemplo sequencia de Fibonacci com for
print("\n\nExemplo 15 - gerar sequência de Fibonacci")
def fibonacci(qtde):

    fib = []
    fib.append(0)
    fib.append(1)

    for indice in range(2,qtde):
        fib.append(fib[indice-1] + fib[indice-2]
            
fibonacci(8)
        

    
