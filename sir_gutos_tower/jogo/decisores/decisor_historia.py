from .tomador_decisoes import TomadorDecisoes
from .decisao import Decisao
from ...utils.decisores.exibicao import definir_gasto_energia


class DecisorHistoria(TomadorDecisoes):

    def __init__(self):
        super().__init__()

        self.ver_atributos = None

    def novas_decisoes(self, decisoes):
        super().novas_decisoes(decisoes)
        if not self.eh_decisao_obrigatoria():
            codigo_ver_atributos = str(len(self.decisoes) + 1)
            self.ver_atributos = Decisao(codigo_ver_atributos, 'Ver Atributos')
            self.decisoes.append(self.ver_atributos)

    def imprimir_decisoes(self):
        if not self.eh_decisao_obrigatoria():
            print()

            for decisao in self.decisoes:
                gasto_energia = definir_gasto_energia(decisao)
                print(f'{decisao.codigo}) {decisao.descricao} {gasto_energia}')

    def tomar_decisao(self, texto_pergunta="O que você vai fazer?"):
        escolha_usuario = super().tomar_decisao(texto_pergunta)
        return escolha_usuario
