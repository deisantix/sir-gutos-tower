from .tomador_decisoes import TomadorDecisoes
from sir_gutos_tower.config import var


class DecisorHistoria(TomadorDecisoes):

    def __init__(self):
        super().__init__()
        self.VER_ATRIBUTOS = None

    def novas_decisoes(self, decisoes):
        super().novas_decisoes(decisoes)

        quantas_decisoes = len(self.decisoes)
        self.VER_ATRIBUTOS = str(quantas_decisoes + 1)
        self.decisoes[self.VER_ATRIBUTOS] = {"decisao": "Ver atributos"}

    def imprimir_decisoes(self):
        if not self.eh_decisao_obrigatoria():
            print()

            for decisao in self.decisoes:
                decisao_detalhes = self.decisoes[decisao]

                gasto_energia = self.definir_gasto_de_energia(decisao_detalhes)
                print(f'{decisao}) {decisao_detalhes["decisao"]} {gasto_energia}')

    def definir_gasto_de_energia(self, detalhes):
        try:
            energia = detalhes['energia']

            if energia == var.GASTO_MISTERIOSO:
                energia = '?'
            elif energia == var.ATAQUE_ESPECIAL:
                return '(-AE)'

            return f'(-{energia} E)'
        except KeyError:
            return ''

    def tomar_decisao(self, jogador):
        while True:
            escolha_usuario = super().tomar_decisao()

            if escolha_usuario == self.VER_ATRIBUTOS:
                jogador.imprimir_atributos()
            else:
                return escolha_usuario
