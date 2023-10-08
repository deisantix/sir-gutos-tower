from abc import ABC, abstractmethod
from ..decisores.decisor_historia import DecisorHistoria


class Heroi(ABC):

    def __init__(self):
        self.decisor = DecisorHistoria()

    @abstractmethod
    def init_atributos(self):
        pass

    @abstractmethod
    def executar_acao(self, energia_gasta):
        pass

    @abstractmethod
    def imprimir_atributos(self):
        pass

    @abstractmethod
    def __str__(self):
        pass

    def novas_decisoes(self, novas_decisoes):
        self.decisor.novas_decisoes(novas_decisoes)

    def imprimir_decisoes(self):
        self.decisor.imprimir_decisoes()

    def tomar_decisao(self):
        while True:
            escolha = self.decisor.tomar_decisao()
            if escolha == self.decisor.ver_atributos:
                self.imprimir_atributos()
            elif escolha == DecisorHistoria.DECISAO_INVALIDA:
                print(escolha)
            else:
                return escolha
