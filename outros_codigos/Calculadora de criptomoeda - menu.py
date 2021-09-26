#CURSO: TECNOLOGIA EM ANÁLISE E DESENVOLVIMENTO DE SISTEMAS
#DISCIPLINA: RACIOCÍNIO COMPUTACIONAL
#PROFESSORES: LUCAS 
#ESTUDANTE: CARLA EDILA S R SILVEIRA
#DESAFIO 1 - SEMANA 5
#PROGRAMA PARA CONVERSÃO DE CRIPTOMOEDAS OU CALCULADORA COM MENU

controle = 1 #bloco - menu para comunicação com usuário
while True:
    print("CONVERSÃO\n".center(80))
    print("DE CRIPTOMOEDAS\n\n".center(80))
    print("1- Converter Bitcoins em Reais.".center(80))
    print("2- Converter Reais em Bitcoins.".center(80))
    print("3- Sair.\n\n\n".center(80))
    controle = int(input("Escolha uma opção: ".center(80))
    if (controle == 3):
                   break #interrompe o processamento das repetições
                print("===================================\n".center(80))
    # Análise de opções do menu
    if controle == 1: #bloco - conversão de BTC para REAL BR
        Bitcoins = float(input("Valor em BITCOINS - BTC(separe centavos com ponto): "))
        cotacao1_hoje = float(37955.17) #valor conforme bolsas de moedas Morningstar e Coinbase,Inc.
        cambioBTC = float(Bitcoins*cotacao1_hoje)
        print("\nA quantia de {:.6f}".format(Bitcoins)"BTC equivale a R${:.2f}".format(cambioBTC))
        print("============================================+============\n")

    elif controle == 2:  #bloco - conversão de REAL BR para BTC
        Reais = float(input("Valor em REAIS - BRL(separe centavos com ponto): "))
        cotacao2_hoje = float(0.000026) #valor conforme bolsas de moedas Morningstar e Coinbase,Inc.
        cambioBRL = float(Reais*cotacao2_hoje)
        print("\nA quantia de R${:.2f}".format(Reais)"equivale a {:.6f}".format(cambioBRL))
        print("============================================+============\n")
else:
    print("===================================\n".center(80)) #final da calculadora

