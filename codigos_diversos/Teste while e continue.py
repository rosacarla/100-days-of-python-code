#Exemplo de while e continue
#inicialização da variável contadora
cont = 1
while cont<10:
    cont+=1  #incremento da variável contadora
    #Teste condicional se o número é ímpar
    if(cont%2==1):
        continue   #salta para o próxima execução do loop
    print(cont)    #print somente quando cont é par
print("\n.\n")
#Exemplo de sintaxe do comando while com comando break
cont = 1   #inicialização da variável contadora
while True:
    #mensagem a ser reprtida até que o comando break,
    #dentro do bloco if seja executado
    print (str(cont)+"a execução do while!")
    cont+=1  #Incremento da variável contadora
    #Verifica se a variável contadora é maior do que 3
    if (cont>3):
        break
#Instrução imediatamente após o laço
print("Execução do while acabou.")

    
