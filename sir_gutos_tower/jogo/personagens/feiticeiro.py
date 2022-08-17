from .lutavel import Lutavel
from .heroi import Heroi
from sir_gutos_tower.config.var import ATAQUE_ESPECIAL
from sir_gutos_tower.utils.exceptions.exceptions import NaoAcertouAtaqueError, AdversarioProtegidoError

from .calculador_de_dano import calcular_dano


class Feiticeiro(Heroi, Lutavel):

    def __init__(self, nome='Gustav', eh_jogador=False):
        self.nome = nome
        self.eh_jogador = eh_jogador
        self.protegido = False

        self.init_atributos()


    def init_atributos(self):
        self.vida = 50
        self.ataque = 5
        self.defesa = 10
        self.magia = 35
        self.energia = 210
        self.critico = 15
        self.precisao = 10


    def executar_acao(self, energia_gasta):
        self.energia -= energia_gasta


    def retornar_ataques(self):
        return {
            '1': {
                'decisao': 'Usar magia', 'energia': 8, 'acao': {
                    'ataque': self.usar_magia,
                    'tipo': 'ativo',
                    'texto': [
                        '{jogador} queima o monstro com fogo mágico',
                        '{jogador} joga o monstro no ar, fazendo ele cair com força no chão',
                        '{jogador} ataca {monstro} com magia',
                        '{jogador} ativa seus poderes elétrico em {monstro}',
                        '{jogador} invoca búfalos fantasma que atropelam {monstro}'
                    ]
                }
            },
            '2': {
                'decisao': 'Ativar escudo', 'energia': 6, 'acao': {
                    'ataque': self.ativar_escudo,
                    'tipo': 'passivo',
                    'texto': [
                        'Você cria um escudo protetor para você e seus companheiros.',
                        'Vocês estão protegidos por duas rodadas.'
                    ]
                }
            },
            '3': {
                'decisao': 'Atacar com cajado', 'energia': 2, 'acao': {
                    'ataque': self.atacar_com_cajado,
                    'tipo': 'ativo',
                    'texto': [

                    ]
                }
            },
            '4': {
                'decisao': 'Curar festa', 'energia': ATAQUE_ESPECIAL, 'acao': {
                    'ataque': self.usar_especial,
                    'texto': [

                    ]
                }
            },
        }


    def usar_magia(self, inimigo):
        acertou = self.tentar_atacar(margem_erro_ataque=15)
        if acertou:
            return calcular_dano(self.magia, inimigo.defesa)
        else:
            raise NaoAcertouAtaqueError


    def ativar_escudo(self):
        self.protegido = True


    def atacar_com_cajado(self):
        pass


    def usar_especial(self):
        pass


    def receber_dano(self, dano):
        if (self.protegido):
            raise AdversarioProtegidoError
        else:
            self.vida -= dano


    def __str__(self):
        atributos = (
            f"{'Vida:':<8} {self.vida}\n"
            f"{'Ataque:': <8} {self.ataque}\n"
            f"{'Defesa:':<8} {self.defesa}\n"
            f"{'Magia:':<8} {self.magia}\n"
            f"{'Energia:':<8} {self.energia}"
        )
        return atributos
