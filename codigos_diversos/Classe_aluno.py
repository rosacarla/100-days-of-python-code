#Exemplo de código do exercício 5 - classe Aluno
# Define a classe Aluno com métodos para calcular a média das notas.
class Aluno:
    def __init__(self,n1,n2,n3,n4):
        self.__notas = [n1, n2, n3, n4]
    def fecha_media(self):
        soma = 0
        media = 0
        i = 0
        while (i<4):
            soma += self.__notas[i]
            i += 1
            media = soma /4
            return media
a = Aluno(5, 6, 7, 8)
m = a.fecha_media()
print(m)



        
            
    
