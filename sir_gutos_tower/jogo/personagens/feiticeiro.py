from random import choice

from .lutavel import Lutavel
from .heroi import Heroi
from sir_gutos_tower.config.var import ATAQUE_ESPECIAL
from sir_gutos_tower.utils.exceptions.exceptions import NaoAcertouAtaqueError, AdversarioProtegidoError

from .calculador_de_dano import calcular_dano


class Feiticeiro(Heroi, Lutavel):

    def __init__(self, nome='Gustav', eh_jogador=False):
        self.nome = nome
        self.eh_jogador = eh_jogador
        self.protegido = 0
        self.mensagem_protegido = ''
        self.acoes_previas = [None, None, None]
        self.contagem_rodadas = 0

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


    def lutar(self, ataque_escolhido, herois, inimigo):
        ataques = self.retornar_ataques()

        energia_gasta = ataques[ataque_escolhido]['energia']
        self.executar_acao(energia_gasta)

        self.adicionar_acoes_previas(ataques[ataque_escolhido]['tipo'])

        dialogos = []
        if self.protegido == Lutavel.PROTEGIDO_COM_ESCUDO_GUSTAV:
            if self.contagem_rodadas == 1:
                if self.eh_jogador:
                    dialogos.append('Seu escudo se desfaz')
                else:
                    dialogos.append('O escudo de {jogador} se desfaz')
                self.contagem_rodadas = 0
                self.desfazer_defesas()
            else:
                self.contagem_rodadas += 1

        onde_procurar_dialogo = 'texto'
        dialogo_inimigo = ''

        if ataque_escolhido == '1':
            dialogo_inimigo = self.usar_magia(inimigo)
        elif ataque_escolhido == '2':
            self.ativar_escudo(herois)
            onde_procurar_dialogo = 'texto_sozinho'



        dialogos.append(
            self.escolher_dialogo_ataque(ataques[ataque_escolhido][onde_procurar_dialogo])
        )
        if dialogo_inimigo:
            dialogos.append(dialogo_inimigo)

        return dialogos


    def retornar_ataques(self):
        return {
            '1': {
                'decisao': 'Usar magia',
                'energia': 8,
                'tipo': 'magia',
                'texto': [
                    '{jogador} queima o monstro com fogo mágico',
                    '{jogador} joga o monstro no ar, fazendo ele cair com força no chão',
                    '{jogador} ataca {monstro} com magia',
                    '{jogador} ativa seus poderes elétrico em {monstro}',
                    '{jogador} invoca búfalos fantasma que atropelam {monstro}'
                ]
            },
            '2': {
                'decisao': 'Ativar escudo',
                'energia': 6,
                'tipo': 'defesa',
                'texto': [
                    'Você cria um escudo protetor para você e seus companheiros.\nVocês estão protegidos por duas rodadas.'
                ],
                'texto_sozinho': [
                    'Você cria um escudo protetor a sua volta.\nVocê está protegido por duas rodadas.'
                ]
            },
            '3': {
                'decisao': 'Atacar com cajado',
                'energia': 2,
                'tipo': 'ataque',
                'texto': [

                ]
            },
            '4': {
                'decisao': 'Curar festa',
                'energia': ATAQUE_ESPECIAL,
                'tipo': 'especial',
                'texto': [

                ]
            },
        }


    def usar_magia(self, inimigo):
        acertou = self.tentar_atacar(margem_erro_ataque=12)
        if acertou:
            dano = calcular_dano(self.magia, inimigo.defesa)

            try:
                return inimigo.receber_dano(dano)
            except AdversarioProtegidoError as protegido:
                return str(protegido)
        else:
            raise NaoAcertouAtaqueError


    def ativar_escudo(self, aliados):
        for aliado in aliados:
            aliado.proteger(Lutavel.PROTEGIDO_COM_ESCUDO_GUSTAV)

        if len(aliados) > 1:
            self.mensagem_protegido = 'Porém o escudo protege vocês'
        else:
            self.mensagem_protegido = 'Porém o escudo lhe protege'


    def proteger(self, modo):
        self.protegido = modo


    def desfazer_defesas(self):
        self.protegido = 0


    def atacar_com_cajado(self):
        pass


    def usar_especial(self):
        pass


    def receber_dano(self, dano):
        if (self.protegido == Lutavel.PROTEGIDO_COM_ESCUDO_GUSTAV):
            raise AdversarioProtegidoError(self.mensagem_protegido)
        else:
            self.vida -= dano
            return '{jogador} perde ' + str(dano) + ' de dano'


    def adicionar_acoes_previas(self, acao):
        if len(self.acoes_previas) == 3:
            self.acoes_previas.pop(0)
        self.acoes_previas.append(acao)


    def __str__(self):
        atributos = (
            f"{'Vida:':<8} {self.vida}\n"
            f"{'Ataque:': <8} {self.ataque}\n"
            f"{'Defesa:':<8} {self.defesa}\n"
            f"{'Magia:':<8} {self.magia}\n"
            f"{'Energia:':<8} {self.energia}"
        )
        return atributos
