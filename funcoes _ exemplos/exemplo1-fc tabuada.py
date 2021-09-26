# 1) Defina um programa em Python onde o usuário informará um valor N inteiro.
# O programa deve mostrar a tabuada do valor N.
# Quando seu programa estiver pronto:
# a) coloque apenas o trecho que faz a impressão da tabuada em uma função
# b) a entrada de dados deve ficar FORA da função.
# c) chame a função da tabuada 3 vezes passando 3 valores quaisquer por parâmetro


#Ex.:

 #   3 x 1 = 3
 #   3 x 2 = 6
 #   3 x 3 = 9
 #   ...
 #   3 x 10 = 30

def tabuada(n):

    for c in range(1,11):

        print("{} x {} = {}".format(n, c, n * c))
    

n = int(input("Informe N: "))

# Chamada a função
tabuada(n)

tabuada(2)
tabuada(6)
tabuada(8)



