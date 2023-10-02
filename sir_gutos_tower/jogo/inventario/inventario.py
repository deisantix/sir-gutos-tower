from ..inventario.item import Item
from ..decisores.decisor_inventario import DecisorInventario


class Inventario:

    def __init__(self):
        self.armazenamento = dict()
        self.decisor_inventario = DecisorInventario()

    def adicionar_item(self, novo_item):
        id = novo_item.id
        if self.armazenamento.get(id, -1) == -1:
            self.armazenamento[id] = []
        self.armazenamento[id].append(novo_item)

    def retirar_item(self):
        self.abrir_inventario()
        item_escolhido = self.decisor_inventario.tomar_decisao()

        if type(item_escolhido) == Item:
            return self.confirmar_uso_de_item(item_escolhido)

    def abrir_inventario(self):
        self.decisor_inventario.novas_decisoes(self.armazenamento)
        self.decisor_inventario.imprimir_decisoes()

    def confirmar_uso_de_item(self, item_escolhido):
        print(f'\n{item_escolhido}: {item_escolhido.descricao}')
        escolha = self.decisor_inventario.fazer_escolha_sim_ou_nao()

        if escolha == DecisorInventario.SIM:
            self.remover_item_do_inventario(item_escolhido)
            return item_escolhido

    def remover_item_do_inventario(self, item_escolhido):
        lista_itens = self.armazenamento.get(item_escolhido.id)
        lista_itens.pop()

        if not len(lista_itens):
            self.armazenamento.pop(item_escolhido.id)

    def __str__(self):
        inventario_texto = ''
        for item_id in self.armazenamento:
            itens = self.armazenamento[item_id]
            inventario_texto += f'\n{itens[0]} (QTD: {len(itens)})'
        return inventario_texto
