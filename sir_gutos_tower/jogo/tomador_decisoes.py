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

            if energia == -1:
                energia = '?'
            return f'(-{energia} E)'
        except KeyError:
            return ''


    def tomar_decisao(self):
        while True:
            if self.eh_decisao_obrigatoria():
                escolha_usuario = TomadorDecisoes.DECISAO_OBRIGATORIA
            else:
                escolha_usuario = input('\nO que você vai fazer? ')

            if escolha_usuario == self.VER_ATRIBUTOS:
                print()
                print(self.jogador)

            elif escolha_usuario in self.decisoes:
                decisao_detalhes = self.decisoes[escolha_usuario]

                energia = decisao_detalhes['energia']
                self.gastar_energia_do_jogador(energia)

                return decisao_detalhes['historia']

            else:
                print('Decisão inválida. Escolha novamente')


    def gastar_energia_do_jogador(self, energia):
        if energia != -1:
            self.jogador.executar_acao(energia)


    def eh_decisao_obrigatoria(self):
        return TomadorDecisoes.DECISAO_OBRIGATORIA in self.decisoes
