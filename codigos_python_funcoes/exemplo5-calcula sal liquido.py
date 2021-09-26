
def calcula_salario_liquido(salario_bruto):

    liquido = salario_bruto - (salario_bruto * 0.15)

    return liquido


for c in range(3):
    
    salario = float(input("Informe seu salario bruto: "))

    liquido = calcula_salario_liquido(salario)

    print(liquido)



    
