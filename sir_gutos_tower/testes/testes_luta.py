from sir_gutos_tower.jogo.combate import Combate
from sir_gutos_tower.jogo.personagens.feiticeiro import Feiticeiro
from sir_gutos_tower.jogo.personagens.monstro import Monstro


def teste_luta():
    feiticeiro = Feiticeiro(nome='Ethaniel', eh_jogador=True)
    feiticeiro_segundo = Feiticeiro()
    monstro = Monstro(nome='Sir Dragon', vida=240, ataque=1, defesa=2, critico=1, precisao=10)

    combate = Combate()

    combate.adicionarHeroi(feiticeiro)
    combate.adicionarMonstro(monstro)

    combate.comecar()

if __name__ == '__main__':
    teste_luta()


