import json

from jogo.jogo import Jogo
from jogo.personagens.feiticeiro import Feiticeiro
from utils.exceptions.exceptions import FimDeJogoError

from config.files import POV_WITCHER
from config.properties import PERSONAGEM
from config.var import FEITICEIRO, CAVALEIRO, ARQUEIRO

def main():
    if PERSONAGEM == FEITICEIRO:
        caminho_pov = POV_WITCHER
        jogador = Feiticeiro()

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
