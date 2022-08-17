from sir_gutos_tower.utils.exceptions.exceptions import NaoAcertouAtaqueError
from .calculador_de_dano import calcular_dano
from .lutavel import Lutavel


class Monstro(Lutavel):

    def __init__(self, nome, vida, ataque, defesa, critico, precisao):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.critico = critico
        self.precisao = precisao


    def retornar_ataques(self):
        return {
            '1': {
                'nome': 'Atacar', 'acao': {
                    'ataque': self.atacar,
                    'texto': [
                        '{monstro} atacou {jogador}'
                    ]
                }
            },
            '2': {
                'nome': 'Defender', 'acao': {
                    'ataque': self.defender,
                    'texto': [

                    ]
                }
            }
        }


    def atacar(self, heroi):
        acertou = self.tentar_atacar(margem_erro_ataque=12)
        if acertou:
            return calcular_dano(self.ataque, heroi.defesa)
        else:
            raise NaoAcertouAtaqueError


    def defender(self):
        pass


    def receber_dano(self, dano):
        self.vida -= dano
