import json

from sir_gutos_tower.jogo.jogo import Jogo
from sir_gutos_tower.jogo.personagens.feiticeiro import Feiticeiro

from sir_gutos_tower.config.files import POV_WITCHER
from sir_gutos_tower.config.properties import PERSONAGEM
from sir_gutos_tower.config.var import FEITICEIRO, CAVALEIRO, ARQUEIRO


def main():
    if PERSONAGEM == FEITICEIRO:
        caminho_pov = POV_WITCHER
        jogador = Feiticeiro(nome='Ethaniel', eh_jogador=True)

    elif PERSONAGEM == CAVALEIRO:
        print('cavaleiro')
        return

    elif PERSONAGEM == ARQUEIRO:
        print('arqueiro')
        return

    with open(caminho_pov, 'r') as arquivo_para_ler:
        pov = json.load(arquivo_para_ler)

    jogo = Jogo(jogador, pov)
    jogo.iniciar_historia()


if __name__ == '__main__':
    main()
