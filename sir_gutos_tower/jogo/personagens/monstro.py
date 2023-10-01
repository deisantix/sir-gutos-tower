from sir_gutos_tower.utils.exceptions.exceptions import AdversarioProtegidoError, InimigoSemPontosDeVidaError, \
    NaoAcertouAtaqueError
from ..calculador_de_dano import calcular_dano
from .lutavel import Lutavel


class Monstro(Lutavel):

    def __init__(self, nome, vida, ataque, defesa, critico, precisao):
        self.nome = nome
        self.vida = vida
        self.ataque = ataque
        self.defesa = defesa
        self.critico = critico
        self.precisao = precisao

        self.protegido = False
        self.acoes_previas = [None, None, None]

    def lutar(self, ataque_escolhido, aliados, inimigo):
        ataques = self.retornar_ataques()

        self.adicionar_acoes_previas(ataques[ataque_escolhido]['tipo'])

        dialogo_inimigo = ''
        if ataque_escolhido == '1':
            dialogo_inimigo = self.atacar(inimigo)
        elif ataque_escolhido == '2':
            self.defender()

        dialogos = []
        dialogos.append(self.escolher_dialogo_ataque(ataques[ataque_escolhido]['texto']))
        if dialogo_inimigo:
            dialogos.append(dialogo_inimigo)

        return dialogos

    def retornar_ataques(self):
        return {
            '1': {
                'nome': 'Atacar',
                'tipo': 'ataque',
                'texto': [
                    '{monstro} ataca {jogador}'
                ]
            },
            '2': {
                'nome': 'Defender',
                'tipo': 'defesa',
                'texto': [
                    '{monstro} entra em alerta'
                ]
            }
        }

    def atacar(self, heroi):
        acertou = self.tentar_atacar(margem_erro_ataque=12)
        if acertou:
            dano = calcular_dano(self.ataque, heroi.defesa)

            try:
                return heroi.receber_dano(dano)
            except AdversarioProtegidoError as protegido:
                return str(protegido)
        else:
            raise NaoAcertouAtaqueError

    def defender(self):
        self.protegido = True

    def receber_dano(self, dano):
        if self.protegido:
            self.desfazer_defesas()
            raise AdversarioProtegidoError('Porém {monstro} se defende')
        else:
            self.vida -= dano
            if self.vida <= 0:
                raise InimigoSemPontosDeVidaError

    def desfazer_defesas(self):
        self.protegido = False

    def adicionar_acoes_previas(self, acao):
        if len(self.acoes_previas) == 3:
            self.acoes_previas.pop(0)
        self.acoes_previas.append(acao)
