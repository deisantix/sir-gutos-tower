from time import sleep
import random
from os import path
import info

doug_atri = {'Nome': 'Doug', 'Vida': 50, 'Ataque': 35, 'Defesa': 110, 'Escudo': 55, 'Han': 70, 'Energia': 30, 'Critico': 10}
noelle_atri = {'Nome': 'Noelle', 'Vida': 75, 'Ataque': 35, 'Defesa': 15, 'Energia': 30, 'Critico': 20}
gustav_atri = {'Nome': 'Gustav', 'Vida': 50, 'Ataque': 5, 'Defesa': 10, 'Magia': 35, 'Energia': 210, 'Critico': 15}

personagem = info.perso_info
atributos = info.attributes.copy()

inventory = None
arquivo = ''
perdeu = False


#    ▄████████    ▄████████  ▄█      ███      ▄█   ▄████████    ▄████████  ▄█     ▄████████  ▄██████▄
#   ███    ███   ███    ███ ███  ▀█████████▄ ███  ███    ███   ███    ███ ███    ███    ███ ███    ███
#   ███    █▀    ███    █▀  ███▌    ▀███▀▀██ ███▌ ███    █▀    ███    █▀  ███▌   ███    ███ ███    ███
#  ▄███▄▄▄      ▄███▄▄▄     ███▌     ███   ▀ ███▌ ███         ▄███▄▄▄     ███▌  ▄███▄▄▄▄██▀ ███    ███
# ▀▀███▀▀▀     ▀▀███▀▀▀     ███▌     ███     ███▌ ███        ▀▀███▀▀▀     ███▌ ▀▀███▀▀▀▀▀   ███    ███
#   ███          ███    █▄  ███      ███     ███  ███    █▄    ███    █▄  ███  ▀███████████ ███    ███
#   ███          ███    ███ ███      ███     ███  ███    ███   ███    ███ ███    ███    ███ ███    ███
#   ███          ██████████ █▀      ▄████▀   █▀   ████████▀    ██████████ █▀     ███    ███  ▀██████▀
#                                                                                ███    ███

# ATO 2
# def game_witcher_ato2():
#     with open('.save') as save:
#         for l in save:
#             if 'Inventario' in l:
#                 invent = l[len('Inventario: '):-1]
#             elif 'Doug' in l:
#                 doug_life = l[len('Doug: '):-1]
#
#     info.modi_file('ato 2.\n', '.save', 0)
#
#     # ATO 2 ──────────────────────────────────────────────────────────────────────
#     sleep(1)
#     print(f'\n\033[35m{" ATO 2":─>40}\033[m')
#     sleep(1)
#
#     #info.narrativa('ato 2.', 'dar_cogumelo.', 'pov_witcher')
#
#     # SE TIVER INVENTÁRIO DESBLOQUEADO ───────────────────────────────────────────
#     if invent == 'True':
#         sleep(1)
#         print('\033[33m[1] Lutar com o javali \033[36m(-? E)')
#         print('\033[33m[2] Verificar inventário')
#         print('\033[33m[3] VER ATRIBUTOS')
#         print('[4] ABRIR INVENTÁRIO\033[m')
#         sleep(1)
#
#         decision = info.make_decision('1234')
#
#     # SE > NÃO < TIVER INVENTÁRIO DESBLOQUEADO ────────────────────────────────────
#     else:
#         sleep(1)
#         print('\033[33m[1] Lutar com o javali \033[36m(-? E)')
#         print('\033[33m[2] VER ATRIBUTOS')
#         sleep(1)
#
#         decision = info.make_decision('12')


# ATO 1
def game_witcher_ato1():
    info.modi_file('ato 1.\n', '.save', 0)

    info.modi_file('Inventario: False\n', '.save', 1)
    info.modi_file('Itens: \n', '.save', 2)

    info.modi_file('Doug: False\n', '.save', 3)
    info.modi_file('Noelle: False\n', '.save', 4)
    info.modi_file('AT_ESP: False\n', '.save', 5)

    info.save_atri()

    # ATO 1 ───────────────────────────────────────────────────────────────────────────────────────
    sleep(1)
    print(f'\n\033[31m{" ATO 1":─>40}\033[m')

    info.narrativa('ato 1.', 'portal.', arquivo)

    sleep(1)
    print('\033[33m[1] Ir pela ponte mesmo assim \033[35m(-? E)')
    print('\033[33m[2] Achar outro caminho \033[36m(-0 E)')
    print('\033[33m[3] Usar magia para atravessar o outro lado \033[36m(-25 E)')
    print('\033[33m[4] VER ATRIBUTOS')
    sleep(1)

    decision = info.make_decision('1234')

    # SE FOR PELA PONTE ────────────────────────────────────────────────────────────────────────────
    if decision == '1':
        info.narrativa('ponte.', 'superficie_ponte.', arquivo)

        sleep(1)
        print('\033[33m[1] Voltar para a superfície \033[31m(-210 E)')
        print('\033[33m[2] Entrar na caverna \033[36m(-0 E)')
        print('\033[33m[3] VER ATRIBUTOS')
        sleep(1)

        decision = info.make_decision('123')

        # SE VOLTAR PARA A SUPERFÍCIE ─────────────────────────────────────────────────────────────────
        if decision == '1':
            info.narrativa('superficie_ponte.', 'caverna_ponte.', arquivo)
            info.attributes['Energia'] -= 210

            info.death_count()

            sleep(1)
            print('\n\033[32mVocê cai novamente todo o penhasco e morre uma dor excruciante nos espinhos\033[m')
            sleep(2)
            print(f'\033[31m{" VOCÊ PERDEU ":─^40}\033[m')
            return True

        # SE ENTRAR NA CAVERNA ──────────────────────────────────────────────────────────────────────────
        else:
            info.narrativa('caverna_ponte.', 'outro caminho.', arquivo)
            info.achieve('Caminho impossível')

            while True:
                luta = info.fight_witch('Sir Dragon', 10000, 2500, 5000, 0)

                # SE PERDEU A LUTA E NÃO QUER TENTAR NOVAMENTE ─────────────────────────
                if luta is False:
                    info.death_count()
                    return True

                # SE GANHOU ────────────────────────────────────────────────────────────
                else:
                    break

    # SE PROCURAR OUTRO CAMINHO ────────────────────────────────────────────────────────
    elif decision == '2':
        info.narrativa('outro caminho.', 'atravessar magia.', arquivo)

        info.death_count()

        sleep(1)
        print('\n\033[32mVocê morre de cansaço\033[m')
        sleep(2)
        print(f'\033[31m{" VOCÊ PERDEU ":─^40}\033[m')
        return True

    # SE ATRAVESSAR COM MAGIA ───────────────────────────────────────────────────────────
    else:
        info.narrativa('atravessar magia.', 'porta_atravessar magia', arquivo)
        info.attributes['Energia'] -= 25

        sleep(1)
        print('\033[33m[1] Entrar pela porta da frente \033[35m(-? E)')
        print('\033[33m[2] Procurar outra entrada \033[36m(-0 E)')
        print('\033[33m[3] VER ATRIBUTOS')
        sleep(1)

        decision = info.make_decision('123')

        # ENTRAR PELA PORTA DA FRENTE ──────────────────────────────────────────────────
        if decision == '1':
            info.narrativa('porta_atravessar magia.', 'outro_atravessar magia.', arquivo)

            info.attributes['Energia'] -= 50
            info.achieve('O que esperar?')

            sleep(1)
            print('\n\033[32mVocê conseguiu entrar na Torre, porém perdeu \033[95m50\033[32m de \033[95mEnergia\033[m.')

        # PROCURAR OUTRA ENTRADA ───────────────────────────────────────────────────────
        else:
            info.narrativa('outro_atravessar magia.', 'esconder_atravessar magia.', arquivo)

            sleep(1)
            print('\033[33m[1] Se esconder \033[36m(-2 E)')
            print('\033[33m[2] Se preparar para lutar \033[36m(-0 E)')
            print('\033[33m[3] VER ATRIBUTOS')
            sleep(1)

            decision = info.make_decision('123')

            # SE ESCONDER ───────────────────────────────────────────────────────────────
            if decision == '1':
                info.narrativa('esconder_atravessar magia.', 'pegar_item_atravessar magia.', arquivo)
                info.attributes['Energia'] -= 2

                sleep(1)
                print('\033[33m[1] Pegar item que o homem deixou cair \033[36m(-0 E)')
                print('\033[33m[2] Entrar na torre atrás dele \033[36m(-0 E)')
                print('\033[33m[3] VER ATRIBUTOS')
                sleep(1)

                decision = info.make_decision('123')

                # PEGAR ITEM QUE O HOMEM DEIXOU CAIR ────────────────────────────────────
                if decision == '1':
                    info.modi_file('Inventario: True\n', '.save', 1)
                    info.add_inve('Barrinha Protein', {'Quantidade': 1,
                                                       'Descricao': 'Parece uma boa fonte de Energia, e um ótimo petisco...',
                                                       'Efeito': 35, 'Onde': 'E'})

                    sleep(1)
                    print('\n\033[32mVocê vai até o item e o pega.')
                    sleep(1)
                    print('É uma barrinha de Energia!')
                    sleep(1)
                    print('\033[33mVOCÊ DESBLOQUEOU INVENTÁRIO\033[m')
                    sleep(2)
                    print('\033[32mInventário vai estar disponível nos momentos de escolha de agora em diante.\033[m')

                    info.narrativa('pegar_item_atravessar magia.', 'logo_atras_atravessar magia.', arquivo)

                    sleep(1)
                    print('\n\033[32mVocê conseguiu entrar na Torre com sucesso.\033[m')
                    info.achieve('O que esperar?')
                    sleep(1)

                # ENTRAR NA TORRE ATRÁS DELE ────────────────────────────────────────────
                else:
                    info.narrativa('logo_atras_atravessar magia.', 'lutar_atravessar magia.', arquivo)

                    sleep(1)
                    print('\n\033[32mVocê conseguiu entrar na Torre com sucesso.\033[m')
                    info.achieve('O que esperar?')
                    sleep(1)

            # SE PREPARAR PARA LUTAR ────────────────────────────────────────────────────
            else:
                info.narrativa('lutar_atravessar magia.', 'ato 2.', arquivo)
                info.modi_file('Doug: True\n', '.save', 3)

                sleep(1)
                print('\n\033[32mVocê e Doug conseguiram entrar na Torre com sucesso.\033[m')
                info.achieve('O que esperar?')
                info.achieve('O Cavalheiro')
                sleep(1)

    info.save_atri()
    print('\n\033[33mATO 2 DO FEITICEIRO EM BREVE ───────────\033[m\n')
    return True


def game_witcher_intro():
    info.achieve('Que a magia esteja com você')

    info.modi_file('intro.\n', '.save', 0)

    info.modi_file('Inventario: False\n', '.save', 1)
    info.modi_file('Itens: \n', '.save', 2)

    # INTRODUÇÃO ─────────────────────────────────────────────────────────────────────────────────
    info.narrativa('intro.', 'intro_2.', arquivo)

    print('\n\033[33mSUA \033[95mENERGIA\033[33m AUMENTA 2x! O suficiente para viajar!\033[m')
    info.attributes['Energia'] += 200

    info.narrativa('intro_2.', 'andar_intro.', arquivo)

    sleep(1)
    print('\033[33m[1] Ir a pé \033[36m(-0 E)\033[m')
    print('\033[33m[2] Fazer um portal \033[36m(-200 E)\033[m')
    print('\033[33m[3] VER ATRIBUTOS\033[m')
    sleep(1)

    decision = info.make_decision('123')

    # SE DECIDIR IR A PÉ ──────────────────────────────────────────────────────────────────────
    if decision == '1':
        info.narrativa('andar_intro.', 'portal_intro.', arquivo)

        info.death_count()

        sleep(1)
        print('\n\033[32mVocê morre de cansaço.\033[m')
        sleep(2)
        print(f'\033[31m{" VOCÊ PERDEU ":─^40}\033[m')
        return True

    # SE DECIDIR IR POR PORTAL ────────────────────────────────────────────────────────────────
    else:
        info.attributes['Energia'] -= 200

        info.narrativa('portal_intro.', 'ato 1.', arquivo)

    sleep(1)
    print('\n\033[37mSalvando progresso... Não interrompa o programa.\033[m')
    sleep(2)

    global perdeu
    perdeu = game_witcher_ato1()
    return perdeu


#  ▄████████    ▄████████  ▄█    █▄     ▄████████  ▄█          ▄█    █▄       ▄████████  ▄█     ▄████████  ▄██████▄
# ███    ███   ███    ███ ███    ███   ███    ███ ███         ███    ███     ███    ███ ███    ███    ███ ███    ███
# ███    █▀    ███    ███ ███    ███   ███    ███ ███         ███    ███     ███    █▀  ███▌   ███    ███ ███    ███
# ███          ███    ███ ███    ███   ███    ███ ███        ▄███▄▄▄▄███▄▄  ▄███▄▄▄     ███▌  ▄███▄▄▄▄██▀ ███    ███
# ███        ▀███████████ ███    ███ ▀███████████ ███       ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ███▌ ▀▀███▀▀▀▀▀   ███    ███
# ███    █▄    ███    ███ ███    ███   ███    ███ ███         ███    ███     ███    █▄  ███  ▀███████████ ███    ███
# ███    ███   ███    ███ ███    ███   ███    ███ ███▌    ▄   ███    ███     ███    ███ ███    ███    ███ ███    ███
# ████████▀    ███    █▀   ▀██████▀    ███    █▀  █████▄▄██   ███    █▀      ██████████ █▀     ███    ███  ▀██████▀
#                                                 ▀                                            ███    ███
# EM BREVE


#    ▄████████    ▄████████ ████████▄   ███    █▄     ▄████████  ▄█     ▄████████  ▄██████▄
#   ███    ███   ███    ███ ███    ███  ███    ███   ███    ███ ███    ███    ███ ███    ███
#   ███    ███   ███    ███ ███    ███  ███    ███   ███    █▀  ███▌   ███    ███ ███    ███
#   ███    ███  ▄███▄▄▄▄██▀ ███    ███  ███    ███  ▄███▄▄▄     ███▌  ▄███▄▄▄▄██▀ ███    ███
# ▀███████████ ▀▀███▀▀▀▀▀   ███    ███  ███    ███ ▀▀███▀▀▀     ███▌ ▀▀███▀▀▀▀▀   ███    ███
#   ███    ███ ▀███████████ ███    ███  ███    ███   ███    █▄  ███  ▀███████████ ███    ███
#   ███    ███   ███    ███ ███  ▀ ███  ███    ███   ███    ███ ███    ███    ███ ███    ███
#   ███    █▀    ███    ███  ▀██████▀▄█ ████████▀    ██████████ █▀     ███    ███  ▀██████▀
#                ███    ███                                            ███    ███
# EM BREVE


#   ▄▄▄▄███▄▄▄▄      ▄████████  ▄█  ███▄▄▄▄
# ▄██▀▀▀███▀▀▀██▄   ███    ███ ███  ███▀▀▀██▄
# ███   ███   ███   ███    ███ ███▌ ███   ███
# ███   ███   ███   ███    ███ ███▌ ███   ███
# ███   ███   ███ ▀███████████ ███▌ ███   ███
# ███   ███   ███   ███    ███ ███  ███   ███
# ███   ███   ███   ███    ███ ███  ███   ███
#  ▀█   ███   █▀    ███    █▀  █▀    ▀█   █▀
def main():
    print('─\033[32m~\033[m' * 20)
    print(f'\033[91m{"SIR GUTOs TOWER":^40}\033[m')
    print('─\033[32m~\033[m' * 20)

    fl_ex = path.isfile('.info')
    if not fl_ex:
        info.narrativa('bemvindo.', 'classes.', '.help')

    info.ver_save()

    global personagem, atributos, arquivo, perdeu

    info.velo_narrativa()

    caract_tuple = info.caract()
    personagem = caract_tuple[0]
    arquivo = caract_tuple[1]

    atributos = info.skills()

    perdeu = False
    while True:
        print('\n\033[37mDefinindo atributos...')
        sleep(1)
        print('Costurando linhas do tempos...')
        sleep(1)
        print('Carregando...\033[m')
        sleep(2)

        if personagem['Classe'] == 'Feiticeiro':
            with open('.save', 'r') as save:
                tamanho = path.getsize('.save')
                file = save.read()

                if 'intro.' in file or tamanho <= 2:
                    perdeu = game_witcher_intro()
                elif 'ato 1.' in file:
                    perdeu = game_witcher_ato1()
                # elif 'ato 2.' in file:
                #     perdeu = game_witcher_ato2()

        # CASO O JOGADOR TENHA PERDIDO
        if perdeu is True:
            while True:
                sleep(1)
                info.achieve()
                sleep(1)
                try_again = input('Quer tentar de novo? [S/N] ').upper().strip()

                if try_again not in 'SN':
                    sleep(1)
                    print('Oh não... Tente novamente.')
                    continue
                else:
                    break

            # CASO O JOGADOR QUEIRA TENTAR NOVAMENTE
            if try_again == 'S':
                while True:
                    sleep(1)
                    pt = input('Deseja mudar suas características? (Ex.: Classe) [S/N] ').upper().strip()
                    if pt not in 'SN':
                        sleep(1)
                        print('Oh não... Tente novamente.')
                        continue
                    else:
                        break

                # CASO O JOGADOR QUEIRA MUDAR DE NOME E/OU CLASSE
                if pt == 'S':
                    with open('.info', 'r+') as save:
                        save.truncate(0)
                        info.ver_save()

                    personagem = info.caract()
                    atributos = info.skills()
                    sleep(1)
                    continue

                # CASO O JOGADOR > NÃO < QUEIRA TROCAR DE NOME E/OU CLASSE
                else:
                    info.ver_save()

                    atributos = info.skills()
                    continue

            # CASO O JOGADOR > NÃO < QUEIRA JOGAR NOVAMENTE
            else:
                sleep(1)
                print('\033[32mObrigado por jogar!\033[m')
                break
        else:
            sleep(1)
            print('\033[31mPROGRAMA SAIU INEXPERADAMENTE DA ROTA\033[m')
            break


if __name__ == '__main__':
    main()
    
