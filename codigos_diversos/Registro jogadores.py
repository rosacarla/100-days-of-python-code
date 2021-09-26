#Cadastrar nome de jogadores e dividi-los em 2 equipes (par/impar)
# automaticamente com função "dividir_times()"

def dividir_times(inscritos):
    time1 = []
    time2 = []

    for c in range(6):
        # Se for posição PAR    
        if c % 2 == 0:
            time1.append(inscritos[c])
        else:
            time2.append(inscritos[c])

    return time1,time2
        

#######################################
# AQUI ACABA A FUNÇÃO
#######################################

inscritos = []
for c in range(6):
    nome = input("Nome do jogador {}: ".format(c+1))
    inscritos.append(nome)

print("=== INSCRITOS ===")

for nome in inscritos:
    print(" - ", nome)

#Chama a funçao dividir_times
# E passa parametros de inscritos

time1, time2 = dividir_times(inscritos)

print("=== TIME 1 ===")
for nome in time1:
    print(" - ", nome)

print("=== TIME 2 ===")
for nome in time2:
    print(" - ", nome)

lista = ["Oni", "Fer", "Dio", "Mel", "Wel", "Gold"]

time1, time2 = dividir_times(lista)

print(time1)
print(time2)
    


