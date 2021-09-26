
class Automovel:

    cor = ""
    marca = ""
    qtdegasolina = 45

    def __init__(self, c, m):
        self.cor = c
        self.marca = m

    def abastecerCarro(qtdeLitros):

        qtdegasolina = qtdegasolina + qtdeLitros


uno = Automovel("Verde","Fiat")
print(uno)

hondafit = Automovel("Preta", "Honda")
print(hondafit)
