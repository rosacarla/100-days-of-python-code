#criar função tabuada

def tabuada (n):
    for c in range (1,11):
        print("{} x {} = {}".format(n, c, n * c))

n = int(input("Informe N: "))

# Chamada da função
tabuada(n)




