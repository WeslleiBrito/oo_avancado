class Filmes:

    def __init__(self, nome, ano, duracao):
        self.__nome = nome.title()
        self.ano = ano
        self.duracao = duracao
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome

    def recebe_likes(self):
        self.__likes += 1


class Serie:

    def __init__(self, nome, ano, temporadas):
        self.__nome = nome.title()
        self.ano = ano
        self.temporadas = temporadas
        self.__likes = 0

    @property
    def likes(self):
        return self.__likes

    @property
    def nome(self):
        return self.__nome

    @nome.setter
    def nome(self, nome):
        self.__nome = nome.title()

    def recebe_likes(self):
        self.__likes += 1


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

