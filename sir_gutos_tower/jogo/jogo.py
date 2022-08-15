from utils.exceptions.exceptions import FimDeJogoError
from jogo.tomador_decisoes import TomadorDecisoes

class Jogo:

    def __init__(self, jogador, pov):
        self.jogador = jogador
        self.pov = pov
        self.historia = None
        self.tomador_decisoes = TomadorDecisoes(jogador)


    def iniciar_historia(self):
        intro = self.pov['intro']
        self.historia = intro['historia']

        try:
            while True:
                self.historia = self.rodar_historia()

                if type(self.historia) != dict:
                    proximo_ato = self.historia
                    novo_ato = self.pov[proximo_ato]

                    self.historia = novo_ato['historia']
        except FimDeJogoError:
            print('Fim de Jogo')
        except (KeyError, NotImplementedError):
            print('Ocorreu um erro inesperado')


    def rodar_historia(self):
        self.contar()

        try:
            decisoes = self.historia['decisoes']
        except KeyError:
            return self.lidar_com_a_falta_de_decisoes()

        self.tomador_decisoes.novas_decisoes(decisoes)
        self.tomador_decisoes.imprimir_decisoes()
        return self.tomador_decisoes.tomar_decisao()


    def contar(self):
        texto = self.historia['texto']

        print()
        for linha in texto:
            print(linha)


    def lidar_com_a_falta_de_decisoes(self):
        fim = self.verificar_se_fim_de_jogo()
        if fim:
            self.fim_de_jogo()

        proximo_ato = self.verificar_se_existe_proximo_ato()
        if proximo_ato:
            return proximo_ato

        raise NotImplementedError


    def verificar_se_fim_de_jogo(self):
        try:
            return self.historia['fim']
        except KeyError:
            return False


    def fim_de_jogo(self):
        print(self.historia['morte'])
        raise FimDeJogoError


    def verificar_se_existe_proximo_ato(self):
        try:
            return self.historia['proximo']
        except KeyError:
            return False



