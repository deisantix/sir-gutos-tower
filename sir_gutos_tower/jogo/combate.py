from random import choice

from ..utils.exceptions.exceptions import AdversarioProtegidoError, JaEstaNaFestaError, NaoAcertouAtaqueError
from ..jogo.tomador_decisoes import TomadorDecisoes

class Combate:

    def __init__(self):
        self.herois = []
        self.monstros = []
        self.tomador_decisoes = None


    def adicionarHeroi(self, heroi):
        for heroiNaFesta in self.herois:
            if heroi == heroiNaFesta:
                raise JaEstaNaFestaError

        if heroi.eh_jogador:
            self.tomador_decisoes = TomadorDecisoes(heroi, 'acao')
        self.herois.append(heroi)


    def adicionarMonstro(self, monstro):
        for monstroNaFesta in self.monstros:
            if monstro == monstroNaFesta:
                raise JaEstaNaFestaError

        self.monstros.append(monstro)


    def comecar(self):
        lutando = True

        while lutando:
            print()
            for monstro in self.monstros:
                print(monstro.nome, str(monstro.vida) + ' HP')

            self.rodar_vez_dos_herois()
            self.rodar_vez_dos_inimigos()


    def rodar_vez_dos_herois(self):
        monstro = self.monstros[0]

        for heroi in self.herois:
            ataques = heroi.retornar_ataques()

            if heroi.eh_jogador:
                self.tomador_decisoes.novas_decisoes(ataques)

                self.tomador_decisoes.imprimir_decisoes()
                acao = self.tomador_decisoes.tomar_decisao()

                try:
                    if acao['tipo'] == 'ativo':
                        dano = acao['ataque'](monstro)
                        monstro.receber_dano(dano)
                    else:
                        acao['ataque']()

                    dialogo = self.tratar_dialogo_ataque_antes_de_imprimir(
                        acao['texto'], heroi, monstro)
                    self.imprimir_dialogo(dialogo)
                except NaoAcertouAtaqueError:
                    print('\nVocê errou')


    def rodar_vez_dos_inimigos(self):
        for inimigo in self.monstros:
            heroi_a_atacar = choice(self.herois)
            ataques = inimigo.retornar_ataques()

            lista_ataques = list(ataques.keys())
            ataque_escolhido = choice(lista_ataques)
            acao_monstro = ataques[ataque_escolhido]['acao']

            try:
                dano = acao_monstro['ataque'](heroi_a_atacar)
                dialogo_monstro = self.tratar_dialogo_ataque_antes_de_imprimir(
                    acao_monstro['texto'], heroi_a_atacar, inimigo)
                self.imprimir_dialogo(dialogo_monstro)

                heroi_a_atacar.receber_dano(dano)
                self.anunciar_dano(heroi_a_atacar, dano)
            except TypeError:
                print(f'\n{inimigo.nome} errou')
            except NaoAcertouAtaqueError:
                print(f'\n{inimigo.nome} errou')
            except AdversarioProtegidoError:
                dialogo_protegido = self.tratar_dialogo_ataque_antes_de_imprimir(
                    'Porém {jogador} se defendeu', heroi_a_atacar, inimigo
                )
                self.imprimir_dialogo(dialogo_protegido)


    def tratar_dialogo_ataque_antes_de_imprimir(self, textos_acao, heroi, monstro):
        dialogo = self.escolher_texto(textos_acao)
        dialogo = self.reescrever_placeholders_de_dialogo_ataque(dialogo, heroi, monstro)
        return dialogo


    def escolher_texto(self, textos_acao):
        if type(textos_acao) == list:
            return choice(textos_acao)
        else:
            return textos_acao


    def reescrever_placeholders_de_dialogo_ataque(self, dialogo, heroi, monstro):
        pov = self.decidir_pov_heroi(heroi)
        pov = self.minimizar_palavra_voce_caso_nao_no_inicio_da_frase(pov, dialogo)

        dialogo = dialogo.replace('{jogador}', pov)
        dialogo = dialogo.replace('{monstro}', monstro.nome)

        return dialogo


    def minimizar_palavra_voce_caso_nao_no_inicio_da_frase(self, pov, dialogo):
        if pov == 'Você' and not dialogo.startswith('{jogador}'):
            pov = pov.lower()
        return pov


    def imprimir_dialogo(self, dialogo):
        print()
        print(dialogo)


    def anunciar_dano(self, heroi, dano):
        pov = self.decidir_pov_heroi(heroi)
        print(f'{pov} perdeu {dano} de vida')


    def decidir_pov_heroi(self, heroi):
        pov = heroi.nome
        if heroi.eh_jogador:
            pov = 'Você'
        return pov
