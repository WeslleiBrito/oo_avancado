class Filmes:

    def __init__(self, nome, ano, duracao):
        self.nome = nome.capitalize()
        self.ano = ano
        self.duracao = duracao


class Serie:

    def __init__(self, nome, ano, temporadas):
        self.nome = nome
        self.ano = ano
        self.temporadas = temporadas


vingadores = Filmes('vingadores', 2018, 120)
print(vingadores.nome)
