#Codigo: Funcoes
#Autora: Carla Edila Silveira
#Finalidade: criar funcoes para reaproveitar código  - curso Python Quick Start
#Data: 21/09/2021

#criacao de funcao
def saudacoes():    #define a funcao saudacoes 
  name = input("Por favor, digite seu nome: ")  #corpo da funcao
  periodo = input("Por favor, digite o período do dia (manha/tarde/noite): ")  #corpo da funcao
  print("Boa " + periodo + ", " + name + "!")  #corpo da funcao

saudacoes()   #chama o bloco de codigo que compoe a funcao saudacoes

saudacoes()

saudacoes()

saudacoes()

#funcoes pre configuradas do Python
print("Olá, mundo!") #PRINT imprime uma string ou texto

print(2000 + 21) #imprime o resultado do calculo

nome = input("What is your name? ")   #INPUT pede para usuario informar dado que sera recebido pela variavel
cor = input("What is your favorite color? ") #resposta sera digitada pelo usuario e armazenada na variavel

print(nome)  #uso das variaveis em diferentes formas
print(cor)
print("Hi " + nome + "! " + cor + " is a great color!") #impresao de strings concatenadas

# EXERCICIO
# Para criar um código reutilizável que multiplique 4 números, podemos
# criar uma função # de multiplicação que aceite 4 parâmetros numéricos

def multiplicaQuatro(a, b, c, d): # definida funcao
  prod = a * b * c * d
  return prod

multi4 = multiplicaQuatro(2, 4, 6, 8)  # variavel recebe valor resultante do calculo feito pela funcao
print("A multiplicação entre 2, 4, 6 e 8 resulta em: ", multi4)  # imprime o valor da variavel

# fim do codigo
