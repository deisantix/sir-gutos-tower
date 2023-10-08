from abc import ABC, abstractmethod
from .decisao import Decisao


class TomadorDecisoes(ABC):

    DECISAO_INVALIDA = Decisao('151', 'Decisão Inválida. Escolha novamente.')
    CANCELAR = 'C'
    SIM = 'S'
    NAO = 'N'

    def __init__(self):
        self.decisoes = []

    @abstractmethod
    def imprimir_decisoes(self) -> None:
        pass

    def novas_decisoes(self, decisoes: dict):
        self.resetar_decisoes()

        for decisao in decisoes:
            descricao = decisoes[decisao]['decisao']
            energia = decisoes[decisao]['energia']

            self.decisoes.append(Decisao(decisao, descricao, energia))

    def resetar_decisoes(self):
        self.decisoes = []

    def tomar_decisao(self, texto_pergunta="O que você vai fazer?") -> Decisao:
        escolha_usuario = self.perguntar_ao_usuario(texto_pergunta)

        resposta_valida = self.decisao_valida(escolha_usuario)
        if resposta_valida:
            return resposta_valida
        else:
            return TomadorDecisoes.DECISAO_INVALIDA

    def perguntar_ao_usuario(self, texto_pergunta: str):
        if self.eh_decisao_obrigatoria():
            return Decisao.DECISAO_OBRIGATORIA
        else:
            return input(f'\n{texto_pergunta} ').upper()

    def eh_decisao_obrigatoria(self):
        return self.decisoes[0].decisao_obrigatoria

    def decisao_valida(self, decisao, escolhas=None) -> Decisao | bool:
        try:
            if not escolhas:
                escolhas = self.decisoes
            return [e for e in escolhas if e.codigo == decisao][0]
        except IndexError:
            return False

    # def fazer_escolha_sim_ou_nao(self, texto_pergunta="Tem certeza?"):
    #     while True:
    #         decisao_sn = self.perguntar_ao_usuario(f'{texto_pergunta}({self.SIM}/{self.NAO})')
    #
    #         resposta_valida = self.verificar_se_resposta_valida(decisao_sn, [self.SIM, self.NAO])
    #         if resposta_valida:
    #             return decisao_sn
