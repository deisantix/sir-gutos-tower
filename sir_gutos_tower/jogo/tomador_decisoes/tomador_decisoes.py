from abc import ABC, abstractmethod


class TomadorDecisoes(ABC):

    DECISAO_OBRIGATORIA = '0'
    CANCELAR = 'C'
    SIM = 'S'
    NAO = 'N'

    def __init__(self):
        self.decisoes = None


    def novas_decisoes(self, decisoes):
        self.decisoes = decisoes


    @abstractmethod
    def imprimir_decisoes(self):
        pass


    def tomar_decisao(self, texto_pergunta="O que você vai fazer?"):
        while True:
            escolha_usuario = self.perguntar_ao_usuario(texto_pergunta)

            resposta_valida = self.verificar_se_resposta_valida(escolha_usuario, self.decisoes)
            if resposta_valida:
                return escolha_usuario


    def perguntar_ao_usuario(self, texto_pergunta):
        if self.eh_decisao_obrigatoria():
            return TomadorDecisoes.DECISAO_OBRIGATORIA
        else:
            return input(f'\n{texto_pergunta} ').upper()


    def eh_decisao_obrigatoria(self):
        return TomadorDecisoes.DECISAO_OBRIGATORIA in self.decisoes


    def verificar_se_resposta_valida(self, escolha_usuario, conteiner_escolhas):
        if escolha_usuario in conteiner_escolhas:
            return True
        else:
            print('Decisão inválida. Escolha novamente')
            return False


    def fazer_escolha_sim_ou_nao(self, texto_pergunta="Tem certeza?"):
        while True:
            decisao_sn = self.perguntar_ao_usuario(f'{texto_pergunta}({self.SIM}/{self.NAO})')

            resposta_valida = self.verificar_se_resposta_valida(decisao_sn, [self.SIM, self.NAO])
            if resposta_valida:
                return decisao_sn


