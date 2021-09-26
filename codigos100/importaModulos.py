# Codigo: Importa Modulos
# Autora: Carla Edila Silveira
# Finalidade: definir funcoes - curso Python Quick Start
# Data: 21/09/2021

# MODULO  calendario do Python
import calendar  # importa modulo de calendario

cal = calendar.month(2021, 9)  # variavel recebe dados do calendario desejado
print(cal)  # imprime o calendario atribuido a variavel

# importar modulo de matematica do Python
import math  # importa modulo de matematica

result = math.sqrt(49)  # atribui funcao raiz quadrada a variavel
print("A raiz quadrada de 49 é igual a ", result) #imprime o resultado


# MODULO Random
import random #importa modulo random
number = random.randint(1, 100)  #gera aleatoriamente 1 nro inteiro entre os 2 inputs
print(number) #imprime o nro inteiro aleatorio

# escolha aleatoria de item em uma lista
movies = ["Aladim", "Oblivium", "Pocahontas", "The Lion King", "E o vento levou", "ET",
          "Spider-Man", "Men in Black", "Avengers", "Rio", "Karate Kid"]
  # escolher um item aleatorio de uma sequencia ou, por ex., lista de filmes

watch = random.choice(movies)  # variavel para receber a escolha aleatoria do item pela funcao choice
print("Sua coleção de filmes é a seguinte: ", movies)
print("Escolhi este filme para você assistir hoje: ", watch)  # imprime item escolhido


# reordenacao aleatoria de itens de uma lista
deck = ['Ace', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Jack', 'Queen', 'King']
print("Suas cartas de baralho: ",deck)  # imprime a lista na mesma ordem de criação
random.shuffle(deck)  # funcao reordena os itens da lista aleatoriamente
print("Embaralhei suas cartas: ",deck)   # imprime lista rearranjada pela funcao


# MODULO Pow
# Documentacao: Retorna x elevado à potência y. Os casos excepcionais seguem
# o Anexo ‘F’ da norma C99, tanto quanto possível. Em particular, pow(1.0, x)
# e pow(x, 0.0) sempre retornam 1.0, mesmo quando x é um zero ou um NaN. Se
# ambos x e y são finitos, x é negativo, e y não é um inteiro, então pow(x, y)
# é indefinido e levanta "ValueError".

pot = math.pow(2, 10)  # variavel recebe funcao que calcula o resultado de 2 elevado a 10a potencia
print("O resultado de 2 elevado à decima potencia é: ", pot)  # imprime o resultado da potenciacao

# fim do codigo
