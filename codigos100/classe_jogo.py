class Jogo:
    def __init__(self, titulo, genero, ano):
        self.titulo = titulo
        self.genero = genero
        self.ano = ano

# Criando uma instância da classe Jogo
meu_jogo = Jogo("The Legend of Zelda", "Aventura", 1986)

# Acessando os atributos
print(f"Título: {meu_jogo.titulo}")
print(f"Gênero: {meu_jogo.genero}")
print(f"Ano: {meu_jogo.ano}")
