from sir_gutos_tower.utils.exceptions.exceptions import InventarioVazioError
from .tomador_decisoes import TomadorDecisoes


class DecisorInventario(TomadorDecisoes):

    def __init__(self):
        super().__init__()
        self.FECHAR_INVENTARIO = TomadorDecisoes.CANCELAR


    def novas_decisoes(self, decisoes):
        super().novas_decisoes(decisoes)
        if len(self.decisoes):
            self.decisoes = self.reorganizar_itens()


    def reorganizar_itens(self):
        novo_armazenamento = dict()
        i = 1
        for item in self.decisoes:
            novo_armazenamento[str(i)] = item
            i += 1
        novo_armazenamento[self.FECHAR_INVENTARIO] = 'Cancelar'
        return novo_armazenamento


    def imprimir_decisoes(self):
        print()
        if not len(self.decisoes):
            raise InventarioVazioError('Seu inventário está vazio...')

        for i in self.decisoes.keys():
            item = self.decisoes[i]
            try:
                print(f'{i}) {item}: {item.descricao}')
            except AttributeError:
                print(f'{i}) {item}')


    def tomar_decisao(self):
        while True:
            escolha_usuario = super().tomar_decisao('Escolha o item:')

            if escolha_usuario == self.FECHAR_INVENTARIO:
                return False
            else:
                return self.decisoes[escolha_usuario]

    def fazer_escolha_sim_ou_nao(self, texto_pergunta="Tem certeza?"):
        return super().fazer_escolha_sim_ou_nao('Deseja usar esse item? ')



