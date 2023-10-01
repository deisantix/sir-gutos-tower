
from collections.abc import Iterable
from .historia import Historia
from ..utils.exceptions.exceptions import FimDeJogoError
from .tomador_decisoes.decisor_historia import DecisorHistoria
from .combate import Combate
from .personagens.monstro import Monstro
from ..config.var import GASTO_MISTERIOSO


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
                if self.historia.proximo_ato:
                    self.historia.ir_para_proximo_ato()

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
        return self.lidar_com_decisao(decisoes_opcoes[codigo_decisao])

    def contar(self):
        print()
        for linha in self.historia.texto:
            print(linha)

    def lidar_com_a_falta_de_decisoes(self):
        fim = self.verificar_se_fim_de_jogo()
        if fim:
            self.fim_de_jogo()

        proximo_ato = self.verificar_se_existe_proximo_ato()
        if proximo_ato:
            return proximo_ato

        combate = self.verificar_se_entrou_em_combate()
        if combate:
            return self.iniciar_combate()

        raise NotImplementedError

    def verificar_se_fim_de_jogo(self):
        return self.verificar_funcionalidade_do_jogo('fim')

    def fim_de_jogo(self):
        try:
            print(self.historia['morte'])
        finally:
            raise FimDeJogoError

    def verificar_se_existe_proximo_ato(self):
        return self.verificar_funcionalidade_do_jogo('proximo')

    def verificar_se_entrou_em_combate(self):
        return self.verificar_funcionalidade_do_jogo('combate')

    def iniciar_combate(self):
        detalhes = self.historia['combate']
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

    def verificar_funcionalidade_do_jogo(self, funcionalidade: str) -> Iterable | bool:
        try:
            return self.historia[funcionalidade]
        except KeyError:
            return False

    def lidar_com_decisao(self, detalhes):
        self.jogador.executar_acao(detalhes)
        return detalhes['historia']
