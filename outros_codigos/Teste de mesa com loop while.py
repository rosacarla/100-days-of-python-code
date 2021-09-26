#Exemplo teste de mesa com o laço de repetição while
cont = 1 #Inicialização da variável contadora
soma = 0 #Inicialização da variável acumuladora
print("Interação do while\tCondição testada\tcont\tsoma")
while cont<=10:
    soma +=cont  #Atualiza variável acumuladora
    status = cont<=10  #Status da condição do laço while
    print (str(cont)+"a vez\t\t\t"+str(status)+"\t\t\t"+str(cont)+"\t"+str(soma))
    cont +=1  #Incrementa a variável contadora

status = cont<=10
print("Fim do while\t\t"+str(status)+"\t\t\t"+str(cont)+"\t"+str(soma))
