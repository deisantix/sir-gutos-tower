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


    def lutar(self, ataque_escolhido, aliados, inimigo):
        ataques = self.retornar_ataques()

        dialogo_inimigo = ''
        if ataque_escolhido == '1':
            dialogo_inimigo = self.atacar(inimigo)

        return [
            self.escolher_dialogo_ataque(ataques[ataque_escolhido]),
            dialogo_inimigo
        ]


    def retornar_ataques(self):
        return {
            '1': {
                'nome': 'Atacar',
                'texto': [
                    '{monstro} atacou {jogador}'
                ]
            },
            '2': {
                'nome': 'Defender',
                'texto': []
            }
        }


    def atacar(self, heroi):
        acertou = self.tentar_atacar(margem_erro_ataque=12)
        if acertou:
            dano = calcular_dano(self.ataque, heroi.defesa)
            return heroi.receber_dano(dano)
        else:
            raise NaoAcertouAtaqueError


    def defender(self):
        pass


    def receber_dano(self, dano):
        self.vida -= dano
