#Codigo: Definir Funcoes
#Autora: Carla Edila Silveira
#Finalidade: definir funcoes - curso Python Quick Start
#Data: 21/09/2021

# Usa-se o comando "def" seguido do "nome da função", entre parênteses pode conter
# o "nome da entrada", fecha-se a linha com ":". Na linha abaixo, usa-se indentação
# (1 Tab) para escrever o código que compõe o corpo do função. Deste modo:
#
# def funcaoNome(inputNome):
#    corpo

#funcao somar 5
def somarCinco(x):  #definida funcao que soma 5 a um numero indicado
    print(5 + x)  #imprime o resultado do calculo


somarCinco(30)  #chama a funcao com indicacao do nro 30

somarCinco(62.5)  #funcao reconhece nro decimal


#funcao greeting
def greeting():   #define funcao sem parametro para saudacao
    print("Hey there!")  #imprime a mensagem de saudacao


greeting()  #chama a funcao


#funcao greet
def greet(name):  #define funcao com parametro especificado
    print("Hi "+ name + "!")


greet("Joshua")  #chama a funcao com a passagem do parametro


#funcao square
x = 0
def square(x):  #define funcao para elevar nro ao quadrado
    return x * x


result = square(5)  #variavel recebe a funcao com parametro passado
print(result)  #imprime o valor atribuido a variavel

anotherOne = square(result)  #variavel nova recebe funcao que tem uma variavel como parametro
print(anotherOne)  #imprime produto da multiplicacao do nro por ele mesmo


#funcao soma de quadrados
x = 0
y = 0

def somadeQuadrados(x, y):  #define funcao para somar quadrados de 2 numeros
    quadrado1 = x * x
    quadrado2 = y * y
    return quadrado1 + quadrado2


resultado = somadeQuadrados(2, 3)
print(resultado)


#funcao Is it raining
def is_it_raining():  #define funcao que pergunta se está chovendo
    raining = input("Is it raining today? ")
    return raining


monday_rain = is_it_raining()
print(monday_rain)

tuesday_rain = is_it_raining()
print(tuesday_rain)

#fim do codigo