from sir_gutos_tower.config import var


class TomadorDecisoes:

    DECISAO_OBRIGATORIA = "0"

    def __init__(self, jogador):
        self.jogador = jogador
        self.decisoes = None

        self.VER_ATRIBUTOS = None


    def novas_decisoes(self, decisoes):
        self.decisoes = decisoes

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


    def tomar_decisao(self):
        while True:
            escolha_usuario = self.perguntar_ao_usuario()
            if escolha_usuario == self.VER_ATRIBUTOS:
                self.imprimir_atributos()

            elif escolha_usuario in self.decisoes:
                return escolha_usuario

            else:
                print('Decisão inválida. Escolha novamente')


    def perguntar_ao_usuario(self):
        if self.eh_decisao_obrigatoria():
            return TomadorDecisoes.DECISAO_OBRIGATORIA
        else:
            return input('\nO que você vai fazer? ')


    def imprimir_atributos(self):
        print()
        print(self.jogador)


    def eh_decisao_obrigatoria(self):
        return TomadorDecisoes.DECISAO_OBRIGATORIA in self.decisoes
