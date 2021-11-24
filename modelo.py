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

    def __str__(self):
        return f'{self._nome} - {self.duracao} min - {self._likes}'


class Serie(Programa):

    def __init__(self, nome, ano, temporadas):
        super().__init__(nome, ano)
        self.temporadas = temporadas

    def __str__(self):
        return f'{self._nome} - {self.temporadas} temporadas - {self._likes}'


class Playlist:
    def __init__(self, nome, programa):
        self._nome = nome
        self._programa = programa

    def __getitem__(self, item):
        return self._programa[item]

    @property
    def listagem(self):
        return self._programa

    @property
    def tamanho(self):
        return len(self._programa)


vingadores = Filmes('vingadores ultimato', 2018, 120)
missao_resgate = Filmes('missão resgate', 2021, 109)
resident_evil = Filmes('bem vindo a raccoon city', 2021, 107)

vingadores.recebe_likes()
vingadores.recebe_likes()
vingadores.recebe_likes()
vingadores.recebe_likes()
missao_resgate.recebe_likes()
missao_resgate.recebe_likes()
resident_evil.recebe_likes()
resident_evil.recebe_likes()
resident_evil.recebe_likes()

peaky_blinders = Serie('peaky blinders', 2014, 5)
twot = Serie('The Wheel Of Time', 2021, 1)
tdw = Serie('the walking dead', 2010, 10)

peaky_blinders.recebe_likes()
peaky_blinders.recebe_likes()
tdw.recebe_likes()
tdw.recebe_likes()
tdw.recebe_likes()
tdw.recebe_likes()
tdw.recebe_likes()
twot.recebe_likes()
twot.recebe_likes()
twot.recebe_likes()

lista = [vingadores, missao_resgate, resident_evil, peaky_blinders, tdw, twot]
minha_playlist = Playlist('Minha Play', lista)

print(minha_playlist[0])
for programas in minha_playlist:
    print(programas)
