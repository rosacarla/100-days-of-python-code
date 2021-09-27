#CURSO: TECNOLOGIA EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
#DISCIPLINA: PROGRAMAÇÃO ORIENTADA A OBJETOS
#PROFESSOR: LUCAS EMANUEL  
#ESTUDANTE: CARLA EDILA SILVEIRA
#DESAFIO 1 - SEMANA 1: CÁLCULO DA CONTA DE ENERGIA 
#DATA: 15/05/2020

#Revisão de expressões e atribuições (operadores e precedências)
#Declaração de variáveis para cálculo de consumo mensal em kWh

print("========================================\n".center(80))
print("SIMULADOR DE CONTA MENSAL DE ENERGIA\n".center(80))
print("========================================\n\n".center(80))
      


def simulador_conta(conta_mensal):
    conta_mensal = watts * horas * tarifa
    return conta_mensal

aparelhos = []
watts = []
horas = []
soma = 0
tarifa = float(input("Qual o valor atual da tarifa de energia? ")
               
for c in range(4):
    aparelhos = input("Informe nome do aparelho {}: ".format(c+1))
    aparelhos.append(aparelhos)
    watts = int(input("Potencia em watts {}: ".format(c+1))
    watts.append(watts)
    horas = int(input("Consumo diário em horas {}: ".format(c+1))
    horas.append(horas)
    watts = soma + watts
    horas = soma + horas * 30
    conta_mensal = simulador_conta(conta_mensal)    
                       
print("\n\n==== Confira a simulação de sua conta mensal. =====\n".center(80))
print("\t",aparelhos,"\t",watts,"\t",horas,"\n".center(80))
print("\nO valor simulado da conta de energia é: R$ {:.2f}.".format(conta_mensal)





