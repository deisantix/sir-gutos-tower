class Item:

    def __init__(self, id, nome, descricao):
        self.id = id
        self.nome = nome
        self.descricao = descricao


    def usar(self, usuario):
        pass


    def __str__(self):
        return self.nome

