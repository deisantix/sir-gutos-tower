from .lutavel import Lutavel
from .heroi import Heroi
from sir_gutos_tower.config.var import ATAQUE_ESPECIAL, GASTO_MISTERIOSO
from sir_gutos_tower.utils.exceptions.exceptions import InventarioVazioError, NaoAcertouAtaqueError, \
    AdversarioProtegidoError
from sir_gutos_tower.jogo.inventario.inventario import Inventario

from sir_gutos_tower.utils.fatores_batalha.calculador_de_dano import calcular_dano


class Feiticeiro(Heroi, Lutavel):

    def __init__(self, nome='Gustav', eh_jogador=False):
        super().__init__()

        self.nome = nome
        self.eh_jogador = eh_jogador

        self.mensagem_protegido = ''
        self.protegido = 0
        self.contagem_rodadas = 0
        self.acoes_previas = [None, None, None]

        self.aliados = None
        self.inimigo_rodada = None
        self.onde_procurar_dialogo = 'texto'

        self.init_atributos()
        self.acoes = self.retornar_ataques()
        self.inventario = Inventario()

    def init_atributos(self):
        self.vida = 50
        self.ataque = 5
        self.defesa = 10
        self.magia = 35
        self.energia = 210
        self.critico = 15
        self.precisao = 10
        self.esta_esgotado = False

    def retornar_ataques(self):
        return {
            '1': {
                'decisao': 'Usar magia',
                'energia': 8,
                'tipo': 'magia',
                'acao': self.usar_magia,
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
                'acao': self.ativar_escudo,
                'texto': [
                    '{jogador} cria um escudo protetor para seus companheiros.\nVocês estão protegidos por duas rodadas.'
                ],
                'texto_sozinho': [
                    'Você cria um escudo protetor a sua volta.\nVocê está protegido por duas rodadas.'
                ]
            },
            '3': {
                'decisao': 'Atacar com cajado',
                'energia': 2,
                'tipo': 'ataque',
                'acao': self.atacar_com_cajado,
                'texto': [
                    '{jogador} ataca com seu cajado, mas não parece fazer muita diferença',
                    '{jogador} acerta o monstro com uma cajadada, mas não parece ser muito eficiente',
                    '{jogador} usa toda força que tem com seu cajado. Não é muita.'
                ]
            },
            '4': {
                'decisao': 'Curar festa',
                'energia': ATAQUE_ESPECIAL,
                'tipo': 'especial',
                'acao': self.usar_especial,
                'texto': [

                ]
            },
        }

    def lutar(self, decisao, herois, inimigo):
        self.aliados = herois
        self.inimigo_rodada = inimigo
        ataque_escolhido = self.acoes[decisao]

        self.executar_acao(ataque_escolhido)
        self.adicionar_acoes_previas(ataque_escolhido['tipo'])

        dialogos = []
        mensagem_escudo_desativado = self.administrar_defesa()
        if mensagem_escudo_desativado:
            dialogos.append(mensagem_escudo_desativado)

        dialogo_inimigo = self.definir_ataque(ataque_escolhido)
        dialogos.append(
            self.escolher_dialogo_ataque(ataque_escolhido[self.onde_procurar_dialogo]))
        if dialogo_inimigo:
            dialogos.append(dialogo_inimigo)

        return dialogos

    def executar_acao(self, decisao):
        self.administrar_energia(decisao)

    def administrar_energia(self, decisao):
        energia_gasta = decisao['energia']
        if energia_gasta != GASTO_MISTERIOSO:
            self.gastar_energia(energia_gasta)

    def gastar_energia(self, energia_gasta):
        self.energia -= energia_gasta

    def adicionar_acoes_previas(self, acao):
        if len(self.acoes_previas) == 3:
            self.acoes_previas.pop(0)
        self.acoes_previas.append(acao)

    def administrar_defesa(self):
        if self.protegido == Lutavel.PROTEGIDO_COM_ESCUDO_GUSTAV:
            if self.contagem_rodadas == 1:
                self.contagem_rodadas = 0
                self.desfazer_defesas()

                if self.eh_jogador:
                    return 'Seu escudo se desfaz'
                else:
                    return 'O escudo de {jogador} se desfaz'
            else:
                self.contagem_rodadas += 1

    def desfazer_defesas(self):
        self.protegido = 0

    def definir_ataque(self, ataque_escolhido):
        self.onde_procurar_dialogo = 'texto'
        if ataque_escolhido['tipo'] == 'defesa' and not len(self.aliados):
            self.onde_procurar_dialogo = 'texto_sozinho'

        return ataque_escolhido['acao']()

    def usar_magia(self):
        acertou = self.tentar_atacar(margem_erro_ataque=12)
        if acertou:
            dano = calcular_dano(self.magia, self.inimigo_rodada.defesa)

            try:
                return self.inimigo_rodada.receber_dano(dano)
            except AdversarioProtegidoError as protegido:
                return str(protegido)
        else:
            raise NaoAcertouAtaqueError

    def ativar_escudo(self):
        for aliado in self.aliados:
            aliado.proteger(Lutavel.PROTEGIDO_COM_ESCUDO_GUSTAV)

        if len(self.aliados) > 1:
            self.mensagem_protegido = 'Porém o escudo protege vocês'
        else:
            self.mensagem_protegido = 'Porém o escudo lhe protege'

    def proteger(self, modo):
        self.protegido = modo

    def atacar_com_cajado(self):
        acertou = self.tentar_atacar(margem_erro_ataque=30)
        if acertou:
            dano = calcular_dano(self.ataque, self.inimigo_rodada.defesa)

            try:
                return self.inimigo_rodada.receber_dano(dano)
            except AdversarioProtegidoError as protegido:
                return str(protegido)
        else:
            raise NaoAcertouAtaqueError

    def usar_especial(self):
        pass

    def receber_dano(self, dano):
        if (self.protegido == Lutavel.PROTEGIDO_COM_ESCUDO_GUSTAV):
            raise AdversarioProtegidoError(self.mensagem_protegido)
        else:
            self.vida -= dano
            if self.vida <= 0:
                self.esta_esgotado = True

            return '{jogador} recebe ' + str(dano) + ' de dano'

    def pegar_item(self, novo_item):
        self.inventario.adicionar_item(novo_item)

    def usar_item(self):
        try:
            item_retirado = self.inventario.retirar_item()
            if item_retirado:
                item_retirado.usar(self)
        except InventarioVazioError as vazio:
            print(vazio)

    def imprimir_atributos(self):
        print()
        print(self)

    def __str__(self):
        atributos = (
            f"{'Vida:':<8} {self.vida}\n"
            f"{'Ataque:': <8} {self.ataque}\n"
            f"{'Defesa:':<8} {self.defesa}\n"
            f"{'Magia:':<8} {self.magia}\n"
            f"{'Energia:':<8} {self.energia}"
        )
        return atributos
