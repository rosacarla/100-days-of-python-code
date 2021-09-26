#CURSO: TECNOLOGIA EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
#DISCIPLINA: RACIOCÍNIO COMPUTACIONAL
#PROFESSOR: LUCAS EMANUEL SILVA E OLIVEIRA
#ESTUDANTE: CARLA EDILA S R SILVEIRA
#ATIVIDADE PRÁTICA (ATP)
#DATA DE ENTREGA: 03.05.2020

#SISTEMA DA LOJA VIDEBRASIL

import time
#Importa módulo "time" da biblioteca para implementar pausas.

#BLOCO 1: INTERAÇÃO INICIAL E ANÁLISE DE CRÉDITO
####FUNÇÃO A - calcular limite de crédito####
def obter_limite(): #Cálculo inclui variáveis salário e idade do usuário
    limiteC = float(salario*(idade/1000)+100)
    return limiteC
for a in range(1):
    print("\nBem vindo à Loja VideBrasil!\nVocê fala com Carla Rosa.")
    for i in range(1, 2): #Pausa de 1 seg antes de pedir dados para análise
        time.sleep(1)
        print("Para análise de crédito, por gentileza, informe seus dados.")
    cargo= input("\nProfissão: ")
    salario = float(input("Salário (separe centavos com ponto): R$ "))
    ano_nasc = int(input("Ano de nascimento (com 4 dígitos): "))
    idade = int(2020-ano_nasc) #Cálculo aproximado da idade do usuário
    limiteC = obter_limite()
    for i in range(1, 2): #Pausa de 1 seg antes de mostrar dados digitados
        time.sleep(1)
        print("Confira os dados digitados.")
        print("\nProfissão: ",cargo)
        print("Salário - R$: {0:.2f}".format(salario))
        print("Ano de nascimento:",ano_nasc)
    for i in range(1, 2): #Pausa de 1 seg antes de mostrar dados calculados.
        time.sleep(1)
        print("\nVocê completa",idade,"anos em 2020. Parabéns!\n")
        print("Aproveite seu crédito para compras no valor de R$ {0:.2f}".format(limiteC))
####Final da FUNÇÃO A ####

#BLOCO 2: SIMULAÇÃO DE USO DO LIMITE DE CRÉDITO
####FUNÇÃO B - calcular venda com limite de crédito####
def verificar_produto(limiteC): #Analisa a venda conforme condições de uso do limite.
    limiteC = limiteC - gasto_total
    return limiteC
soma = 0
itens = int(input("\nQuantos produtos pretende levar? ")) #Entrada das repetições para o laço
for b in range(itens):
    produtoA = input("\nDigite o nome do produto escolhido: ")
    precoA = float(input("Digite o preço do produto(separe centavos com ponto): R$ "))
    PRE60 = float(limiteC*60/100) #Fórmula para condição de venda
    PRE90 = float(limiteC*90/100) #Fórmula para condição de venda
    nome_todo = "Carla Edila Santos da Rosa Silveira" #Va
    nome_todo = float(len(nome_todo))
    if precoA <= PRE60 or nome_todo < precoA < float(idade): #Condição de venda até 60% do limite.
        print("\nLiberado!")
        print("\nVocê receberá 5 % de desconto.")#Para preço entre nº de caracteres do meu nome todo e idade.
        precoA = float(precoA*95/100)#Desconto equivalente ao nº de caracteres do meu 1º nome.
        print("Com desconto, seu produto custará R$ {:.2f}".format(precoA))
    elif PRE90 > precoA > PRE60: #Condição de venda desde 60% até 90% do limite.
        print("\nLiberado ao parcelar em 2 vezes.")
    elif PRE90 < precoA <= limiteC: #Condição de venda desde 90% até 100% do limite.
        print("\nLiberado ao parcelar em 3 ou mais vezes.")
    elif precoA > limiteC: #Condição de venda acima do limite resulta em bloqueio.
        print("\nBloqueado.")
    gasto_total = soma + precoA
    limiteC = verificar_produto(limiteC)
print("\nSeu saldo atualizado é: R$ {:.2f}.".format(limiteC))
####Final da FUNÇÃO B ####

#FIM DO SISTEMA          




