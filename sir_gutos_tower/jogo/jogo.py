from .historia import Historia
from .personagens.heroi import Heroi
from .decisores.decisao import Decisao
from ..utils.exceptions.exceptions import FimDeJogoError
from .combate import Combate
from .personagens.monstro import Monstro


class Jogo:

    def __init__(self, jogador: Heroi, pov: dict):
        self.jogador = jogador
        self.pov = pov
        self.historia = Historia(pov)

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

        self.jogador.novas_decisoes(self.historia.decisoes)
        self.jogador.imprimir_decisoes()

        decisao_escolhida = self.jogador.tomar_decisao()
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

    def lidar_com_decisao(self, decisao: Decisao):
        return self.historia.retornar_historia_por_decisao(decisao)
