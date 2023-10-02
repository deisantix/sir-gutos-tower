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
        for id_item in self.decisoes:
            itens = self.decisoes[id_item]
            novo_armazenamento[str(i)] = {
                "item": itens[0],  # pegando o primeiro da lista apenas para representação
                "quantidade": len(itens)
            }
            i += 1
        novo_armazenamento[self.FECHAR_INVENTARIO] = 'Cancelar'
        return novo_armazenamento

    def imprimir_decisoes(self):
        print()
        if not len(self.decisoes):
            raise InventarioVazioError('Seu inventário está vazio...')

        for i in self.decisoes.keys():
            item_detalhes = self.decisoes[i]

            try:
                item = item_detalhes['item']
                quantidade = item_detalhes['quantidade']

                print(f'{i}) {item.nome:<17} (QTD: {quantidade})')
            except TypeError:
                print(f'{i}) {item_detalhes}')

    def tomar_decisao(self):
        while True:
            escolha_usuario = super().tomar_decisao('Escolha o item:')

            if escolha_usuario == self.FECHAR_INVENTARIO:
                return False
            else:
                return self.decisoes[escolha_usuario]['item']

    def fazer_escolha_sim_ou_nao(self, texto_pergunta="Tem certeza?"):
        return super().fazer_escolha_sim_ou_nao('Deseja usar esse item? ')
