from abc import ABC, abstractmethod

class Heroi(ABC):

    @abstractmethod
    def init_atributos(self):
        pass

    @abstractmethod
    def executar_acao(self, energia_gasta):
        pass

    @abstractmethod
    def __str__(self):
        pass
