from abc import ABC, abstractmethod
from random import randrange, choice
from sir_gutos_tower.utils.fatores_batalha.calculador_de_dano import calcular_precisao


class Lutavel(ABC):
    PROTEGIDO_COM_ESCUDO_GUSTAV = 7

    @abstractmethod
    def lutar(self, ataque_escolhido, aliados, inimigo):
        pass

    @abstractmethod
    def retornar_ataques(self):
        pass

    @abstractmethod
    def receber_dano(self, dano):
        pass

    def escolher_dialogo_ataque(self, textos):
        try:
            return choice(textos)
        except IndexError:
            return ''

    def tentar_atacar(self, margem_erro_ataque):
        precisao_ataque = calcular_precisao(self.precisao, margem_erro_ataque)
        tentativa = randrange(margem_erro_ataque)

        return precisao_ataque[tentativa]
