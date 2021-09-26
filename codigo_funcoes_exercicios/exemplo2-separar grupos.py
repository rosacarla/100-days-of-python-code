#Uma casa de jogos eletrônicos gostaria de utilizar um programa em que pudessem
#cadastrar o nome dos 6 participantes de uma partida de laser-tag e dividí-los
#em duas equipes automaticamente.

#O programa deve:

# a) armazenar o nome dos inscritos em uma lista
# b) imprimir a lista de inscritos
# c) criar duas novas listas - uma para o time 1 e outra para o time 2
# d) colocar inscritos em posições pares no time 1 e ímpares no time 2
# e) imprimir a divisão dos times

#ATENÇÃO: a divisão dos times deve ser feita por uma função chamada dividir_times()

def dividir_times(inscritos):

    time1 = []
    time2 = []

    for c in range(6):

        # Se for posição PAR
        if c % 2 == 0:
            time1.append(inscritos[c])
        else:
            time2.append(inscritos[c])

    return time1, time2
            

def lerInscritos():

    inscritos = []

    for c in range(6):

        nome = input("Nome do jogador {}: ".format(c))

        inscritos.append(nome)

    return inscritos 


########################################
# AQUI ACABA A FUNÇÃO
########################################

inscritos = lerInscritos()

print("=== INSCRITOS ===")
for nome in inscritos:

    print(" - ", nome)

# Chama a função dividir_times
# E passa por parâmetro a lista de inscritos
time1, time2 = dividir_times(inscritos)

print("--- TIME 1 ---")
for nome in time1:
    print(" - ", nome)

print("--- TIME 2 ---")
for nome in time2:
    print(" - ", nome)


#lista = ["João", "Maria", "Ricardo", "Melissa", "Diego", "Murilo"]

#time1, time2 = dividir_times(lista)

#print(time1)
#print(time2)

