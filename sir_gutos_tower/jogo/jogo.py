
from .historia import Historia
from ..utils.exceptions.exceptions import FimDeJogoError
from .decisores.decisor_historia import DecisorHistoria
from .combate import Combate
from .personagens.monstro import Monstro


class Jogo:

    def __init__(self, jogador, pov):
        self.jogador = jogador
        self.pov = pov
        self.historia = Historia(pov)
        self.tomador_decisoes = DecisorHistoria()

    def iniciar_historia(self):
        self.historia.iniciar()

        try:
            while True:
                novo_passo = self.rodar_historia()
                self.historia.passo = novo_passo
        except FimDeJogoError:
            print('\nFim de Jogo')
        # except (KeyError, NotImplementedError):
        #     print('Ocorreu um erro inesperado')
        except KeyboardInterrupt:
            print('\n\nSaindo...')

    def rodar_historia(self):
        self.contar()

        # caso não haja decisões então provavelmente é outra funcionalidade do jogo
        if not self.historia.decisoes:
            return self.lidar_com_a_falta_de_decisoes()
        decisoes_opcoes = self.historia.decisoes

        self.tomador_decisoes.novas_decisoes(decisoes_opcoes)
        self.tomador_decisoes.imprimir_decisoes()

        codigo_decisao = self.tomador_decisoes.tomar_decisao(self.jogador)
        decisao_escolhida = decisoes_opcoes[codigo_decisao]
        return self.lidar_com_decisao(decisao_escolhida)

    def contar(self):
        print()
        for linha in self.historia.texto:
            print(linha)

    def lidar_com_a_falta_de_decisoes(self):
        if self.historia.fim:
            return self.fim_de_jogo()

        if self.historia.combate:
            return self.iniciar_combate()

        if self.historia.proximo_ato:
            return self.carregar_proximo_ato()

        raise NotImplementedError

    def fim_de_jogo(self) -> None:
        try:
            print(self.historia.morte)
        finally:
            raise FimDeJogoError

    def iniciar_combate(self):
        detalhes = self.historia.combate
        combate = Combate()

        combate.adicionar_heroi(self.jogador)
        for ini in detalhes['inimigos']:
            combate.adicionar_monstro(
                Monstro(
                    ini['nome'],
                    ini['vida'],
                    ini['ataque'],
                    ini['defesa'],
                    ini['critico'],
                    ini['precisao']
                )
            )
        ganhou = combate.comecar()
        if ganhou:
            pass
        else:
            return detalhes['perdeu']

    def carregar_proximo_ato(self):
        self.historia.ir_para_proximo_ato()
        return self.historia.passo

    def lidar_com_decisao(self, detalhes):
        self.jogador.executar_acao(detalhes)

        return detalhes['historia']
