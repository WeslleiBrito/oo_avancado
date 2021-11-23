class Programa:
    def __init__(self, nome, ano):
        self._nome = nome.title()
        self.ano = ano
        self._likes = 0

    @property
    def likes(self):
        return self._likes

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def recebe_likes(self):
        self._likes += 1


class Filmes(Programa):

    def __init__(self, nome, ano, duracao):
        super().__init__(nome, ano)
        self.duracao = duracao


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas


vingadores = Filmes('vingadores ultimato', 2018, 120)
for c in range(0, 5):
    vingadores.recebe_likes()
print(f'Descrição do filme:\nNome: {vingadores.nome}\nLançamento: {vingadores.ano}\nDuração: {vingadores.duracao}'
      f'\nLikes: {vingadores.likes}')

peaky_blinders = Serie('peaky blinders', 2014, 5)
for c in range(0, 3):
    peaky_blinders.recebe_likes()
print(f'\nDescrição da serie:\nNome: {peaky_blinders.nome}\nLançamento: {peaky_blinders.ano}\nDuração: '
      f'{peaky_blinders.temporadas}\nLikes: {peaky_blinders.likes}')

