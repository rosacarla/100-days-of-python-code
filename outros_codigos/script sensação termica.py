#MEDIDOR DE SENSAÇÃO TERMICA

from decimal import Decimal

temp = Decimal(input("Digite a temperatura atual (com ponto no lugar de vírgula): "))

#Condição abaixo de 7 graus
if temp< 7:
    print("Congelando!")

#Condição de 7 até 9,9 graus
elif 7 <= temp< 10:
    print("Frio!")
#Condição de 26 até 34,9 graus
elif 26 <= temp< 35:
    print("Ótimo!")
#Condição a partir de 35 graus
elif temp>= 35:
    print("Calor!")

#Condição de 10 até 25,9 graus
else:
    print("Fresco!\nFim.")
    


              
    
              
