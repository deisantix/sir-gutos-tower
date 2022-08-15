import json

from config.files import POV_WITCHER
from jogo.jogo import rodar_historia
from utils.exceptions.exceptions import FimDeJogoError

def main():
    with open(POV_WITCHER, 'r') as arquivo_para_ler:
        pov = json.load(arquivo_para_ler)

    intro = pov['intro']
    historia = intro['historia']

    try:
        while True:
            historia = rodar_historia(historia)
            if type(historia) != dict:
                novo_ato = pov[historia]
                historia = novo_ato['historia']

    except FimDeJogoError:
        print('Fim de Jogo')
    except (KeyError, NotImplementedError):
        print('Ocorreu um erro inesperado')

if __name__ == '__main__':
    main()
