#Exemplo de calculadora simples
controle = 1
while True:
    print("Mini Calculadora")
    print("1-Somar dois números")
    print("2-Subtrair dois números")
    print("3-Multiplicar dois números")
    print("4-Dividir dois números")
    print("5-Fatorial de um número")
    print("6-Potência entre dois números")
    print("7-Sair")
    controle = int(input("Escolha uma opção: "))
    if (controle == 7):
        break
    print("-------------------------------", end="\n")
    # Teste das opções
    if controle == 1:
        num_01 = float(input("Digite um número: "))
        num_02 = float(input("Digite outro número: "))
        print("\nA soma de",num_01,"e",num_02, "é", num_01+num_02)
        print("--------------------------------", end= "\n")

    elif controle == 2:
        num_01 = float(input("Digite um número: "))
        num_02 = float(input("Digite outro número: "))
        print("\nA subtração de",num_01,"e",num_02, "é", num_01-num_02)
        print("--------------------------------", end= "\n")
    elif controle == 3:
        num_01 = float(input("Digite um número: "))
        num_02 = float(input("Digite outro número: "))
        print("\nA multiplicação de",num_01,"e",num_02, "é", num_01*num_02)
        print("--------------------------------", end= "\n")
    elif controle == 4:
        num_01 = float(input("Digite um número: "))
        num_02 = float(input("Digite outro número: "))
        if num_02 == 0:
            print("Não é possível fazer divisão por zero.")
            print("-------------------------------", end="\n")
        else:
            print("\nA divisão de",num_01,"e",num_02,"é",num_01/num_02)
            print("-------------------------------", end="\n")
    elif controle == 5:
        num_01 = float(input("Digite um número: "))
        fatorial = 1
        contador = num_01
        while contador>1:
            fatorial*=contador
            contador-=1
        print("\nO fatorial de",num_01,"é",fatorial)
        print("-------------------------------", end="\n")
    elif controle == 6:
        num_01 = float(input("Digite um número: "))
        num_02 = float(input("Digite outro número: "))
        print("\n",num_01,"elevado a",num_02,"é",num_01**num_02)
        print("-------------------------------", end="\n")

print("----------------------------------", end="\nFim da Calculadora! :D")


        
                             
    
                       
                       
        
        
    
    
    
        
