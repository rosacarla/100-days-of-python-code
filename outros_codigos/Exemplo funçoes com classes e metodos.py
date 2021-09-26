#Exemplo de código com criação de classe

class AnimalEstimacao():
    def __init__(self, nome, especie, dono):
        self.nome = nome
        self.especie = especie
        self.dono = dono

import animal_estimacao as animal

peludo = animal.AnimalEstimacao("Peludo","cão","Alice")
print("Meu nome é: ",peludo.nome,", eu sou um ", peludo.especie, " e meu dono é:",peludo.dono)
print()

fofinho = animal.AnimalEstimacao("Fofinho","gato","Luís")
print("Meu nome é: ", fofinho.nome,", eu sou um ",fofinho.especie, "e meu dono é: ",fofinho.dono)

class AnimalEstimacao():
    def __init__(self, nome,especie, dono):
        self.nome = nome
        self.especie = especie
        self.dono = dono

    def correr(self):
        print("{0} está correndo".format(self.nome))

    def brincar(self):
        print("{0} está brincando".format(self.nome))

    def comer(self):
        print("{0} está comendo".format(self.nome))

