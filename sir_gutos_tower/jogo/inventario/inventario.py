from ..inventario.item import Item
from ..tomador_decisoes.decisor_inventario import DecisorInventario

class Inventario:

    def __init__(self):
        self.armazenamento = []
        self.decisor_inventario = DecisorInventario()


    def adicionar_item(self, novo_item):
        self.armazenamento.append(novo_item)


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
        index_do_item = -1

        for i in range(len(self.armazenamento)):
            if self.armazenamento[i] == item_escolhido:
                index_do_item = i
                break
        self.armazenamento.pop(index_do_item)


    def __str__(self):
        inventario_texto = ''
        for item in self.armazenamento:
             inventario_texto += f'\n{item}: {item.descricao}'
        return inventario_texto

