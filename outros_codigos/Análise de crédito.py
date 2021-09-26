#CURSO: TECNOLOGIA EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
#DISCIPLINA: RACIOCÍNIO COMPUTACIONAL
#PROFESSOR: LUCAS EMANUEL SILVA E OKIVEIRA
#ESTUDANTE: CARLA EDILA S R SILVEIRA
#ATIVIDADE PRÁTICA (ATP)
#SISTEMA DE LOJA

#MENSAGEM INICIAL E OFERTA DA ANÁLISE DE CRÉDITO
print("\nBem vindo à Loja VideBrasil!\nVocê fala com Carla Rosa.")
print("\n\nPara análise de crédito, por gentileza, informe seus dados.")
cargo= input("Profissão: ")
salario = float(input("Salário - (separe centavos com ponto): R$ "))
ano_nasc = int(input("Ano de nascimento (com 4 dígitos): "))
print("\nConfira os dados digitados.")
print("\nProfissão: ",cargo)
print("Salário - R$: {0:.2f}".format(salario))
print("Ano de nascimento:",ano_nasc)

#CÁLCULOS: LIMITE DE CRÉDITO E NEGOCIAÇÃO
idade = int(2020-ano_nasc)
limiteC= float(salario*(idade/1000)+100)
print("\nVocê completa",idade,"anos em 2020. Parabéns!\n")
print("Aproveite o crédito para compras de R$ {0:.2f}".format(limiteC))
produtoA = input("Digite o nome do produto escolhido: ")
precoA = float(input("Digite o preço do produto(separe centavos com ponto): R$ "))
PRE60 = float(limiteC*60/100)
PRE90 = float(limiteC*90/100)

#CONDIÇÃO DE VENDA ATÉ 60% DO LIMITE 
if precoA <= PRE60:  
    print("Liberado!")    
#CONDIÇÕES DO DESCONTO (caracteres do seu nome completo e idade do cliente)
nome_todo = "Carla Edila Santos da Rosa Silveira"
nome_todo = float(len(nome_todo))
#Cálculo do desconto (equivale a caracteres do seu primeiro nome)
PRE05 = float(precoA*95/100)  
if nome_todo <= precoA <= idade:
    print("Você receberá 5% de desconto.")
    print("Com desconto,",produtoA,"custará R$ {:.2f}".format(PRE05))
#CONDIÇÃO DE VENDA ENTRE 60% E 90% DO LIMITE
elif PRE90 > precoA > PRE60:
    print("Liberado ao parcelar em 2 vezes.")
#CONDIÇÃO DE VENDA ENTRE 90% E 100% DO LIMITE
elif PRE90 < precoA <= limiteC:
    print("Liberado ao parcelar em 3 ou mais vezes.")
else:
    precoA > limiteC
    print("Bloqueado.")

    

        



