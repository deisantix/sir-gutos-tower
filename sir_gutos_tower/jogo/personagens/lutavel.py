from abc import ABC, abstractmethod
from random import randrange
from sir_gutos_tower.jogo.personagens.calculador_de_dano import calcular_precisao


class Lutavel(ABC):

    @abstractmethod
    def retornar_ataques(self):
        pass

    @abstractmethod
    def receber_dano(self, dano):
        pass

    def tentar_atacar(self, margem_erro_ataque):
        precisao_ataque = calcular_precisao(self.precisao, margem_erro_ataque)
        tentativa = randrange(margem_erro_ataque)

        return precisao_ataque[tentativa]
