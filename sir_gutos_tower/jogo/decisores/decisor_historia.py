from .tomador_decisoes import TomadorDecisoes
from ...utils.decisores.exibicao import definir_gasto_energia


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

                gasto_energia = definir_gasto_energia(decisao_detalhes)
                print(f'{decisao}) {decisao_detalhes["decisao"]} {gasto_energia}')

    def tomar_decisao(self, jogador):
        while True:
            escolha_usuario = super().tomar_decisao()

            if escolha_usuario == self.VER_ATRIBUTOS:
                jogador.imprimir_atributos()
            else:
                return escolha_usuario
