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


#  ▄█       ███    █▄      ███        ▄████████         ▄█   ▄█▄ ███▄▄▄▄    ▄█     ▄██████▄     ▄█    █▄        ███
# ███       ███    ███ ▀█████████▄   ███    ███        ███ ▄███▀ ███▀▀▀██▄ ███    ███    ███   ███    ███   ▀█████████▄
# ███       ███    ███    ▀███▀▀██   ███    ███        ███▐██▀   ███   ███ ███▌   ███    █▀    ███    ███      ▀███▀▀██
# ███       ███    ███     ███   ▀   ███    ███       ▄█████▀    ███   ███ ███▌  ▄███         ▄███▄▄▄▄███▄▄     ███   ▀
# ███       ███    ███     ███     ▀███████████      ▀▀█████▄    ███   ███ ███▌ ▀▀███ ████▄  ▀▀███▀▀▀▀███▀      ███
# ███       ███    ███     ███       ███    ███        ███▐██▄   ███   ███ ███    ███    ███   ███    ███       ███
# ███▌    ▄ ███    ███     ███       ███    ███        ███ ▀███▄ ███   ███ ███    ███    ███   ███    ███       ███
# █████▄▄██ ████████▀     ▄████▀     ███    █▀         ███   ▀█▀  ▀█   █▀  █▀     ████████▀    ███    █▀       ▄████▀
# ▀                                                    ▀
def fight_knight(nome_monstro, vida_monstro, ataque_monstro, defesa_monstro):
    chance = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    characters = [f'{personagem["Nome"]}', 'Gustav', 'Noelle']
    frases_espada = ('\033[32mVocê pula e corta o monstro por cima com sua espada.\033[m',
                     f'\033[32mVocê acerta o {nome_monstro} consecutivamente com a espada.\033[m',
                     '\033[32mVocê puxa uma segunda espada e corta a criatura em um X.\033[m')

    frases_escudo = (f'\033[32mVocê joga o escudo no {nome_monstro}, que volta como um boomerang.\033[m',
                     '\033[32mVocê avança no monstro e o acerta com força com o escudo.\033[m',
                     '\033[32mVocê empurra o monstro com força com seu escudo\033[m.')

    frases_han = ('\033[32mHan acerta o monstro com um coice\033[m',
                  '\033[32mHan pula em cima do monstro várias vezes seguidas.\033[m',
                  f'\033[32mHan ataca o {nome_monstro} com mordidas.\033[m')

    # SISTEMA DE LUTA ────────────────────────────────────────────────────────────────
    dano_monstro = round(ataque_monstro * (100 / (100 + atributos['Defesa'])))
    dano_han = round(atributos['Han'] * (100 / (100 + defesa_monstro)))
    dano_espada = round(atributos['Ataque'] * (100 / (100 + defesa_monstro)))
    dano_escudo = round(atributos['Escudo'] * (100 / (100 + defesa_monstro)))
    dano_noelle = round(noelle_atri['Ataque'] * (100 / (100 + defesa_monstro)))
    dano_gustav = round(gustav_atri['Magia'] * (100 / (100 + defesa_monstro)))

    shield = None
    noelle = True
    gustav = True

    rodada = 1
    amount_ea = 1
    ataque_anterior = ['']

    ms_gustav = 0
    ms_noelle = 0


    while True:
        # SE O MONSTRO MORRER ────────────────────────────────────────────────────────
        if vida_monstro <= 0:
            sleep(1)
            print('\033[33mVocês ganharam!\033[m')
            return True, noelle, gustav

        # SE O JOGADOR DESMAIAR ──────────────────────────────────────────────────────
        if atributos['Vida'] <= 0:
            sleep(1)
            print('\033[31mSUA VIDA CHEGOU A \033[33M0\033[m')
            sleep(1)
            print('\033[32mO grupo não pode continuar sem você.\033[m')
            return False

        # SE NOELLE DESMAIAR ────────────────────────────────────────────────────────
        if ms_noelle == 0:
            if noelle_atri['Vida'] <= 0:
                sleep(1)
                print('\033[31mA VIDA DE NOELLE CHEGOU A \033[33m0\033[m')
                sleep(1)
                print('\033[32mEla não atacará mais durante a luta.\033[m')

                characters.remove('Noelle')
                noelle = False
                ms_noelle += 1

        # SE GUSTAV DESMAIAR ──────────────────────────────────────────────────────────
        if ms_gustav == 0:
            if gustav_atri['Vida'] <= 0:
                sleep(1)
                print('\033[31mA VIDA DE GUSTAV CHEGOU A \033[33m0\033[m')
                sleep(1)
                print('\033[32mEle não atacará mais durante a luta.\033[m')

                characters.remove('Gustav')
                gustav = False
                ms_gustav += 1

        # IMPRIMIR NOME DO MONSTRO E VIDA ───────────────────────────────────────────
        sleep(1)
        print(f'\n\033[31m{nome_monstro}\033[m: [\033[33m{vida_monstro} HP\033[m]')
        print('=' * 40)

        if rodada == 4:
            rodada = 1

        # CASO SEJA A VEZ DO CAVALHEIRO ─────────────────────────────────────────────────
        if rodada == 1:
            print('\033[32mÉ a sua vez!\033[m\n')

            if shield is True:
                sleep(1)
                print('\033[32mSeu escudo não foi necessário.\033[m\n')
                sleep(1)
                shield = False

            if amount_ea <= 6:
                especial_attack = '\033[31m='
            elif amount_ea <= 15:
                especial_attack = '\033[33m='
            elif amount_ea <= 26:
                especial_attack = '\033[35m='
            elif amount_ea <= 35:
                especial_attack = '\033[36m='
            else:
                especial_attack = '\033[32m='
            print(f'\033[36mAE\033[m: {especial_attack * amount_ea}')

            # OPÇÕES DE AÇÃO ────────────────────────────────────────────────────────────
            if atributos['Energia'] > 5:
                print('\033[33m[1] Atacar com espada \033[36m(-5 E)')
            else:
                print('\033[31m[1] Atacar com espada (-5 E)')
            if atributos['Energia'] > 0:
                print('\033[33m[2] Defender \033[36m(-0 E)')
            else:
                print('\033[31m[2] Defender (-0 E)')
            if atributos['Energia'] > 2:
                print('\033[33m[3] Atacar com escudo \033[36m(-2 E)')
            else:
                print('\033[31m[3] Atacar com escudo (-2 E)')
            if amount_ea == 36:
                print('\033[33m[4] Usar Han \033[36m(-AE)')
            else:
                print('\033[31m[4] Usar Han (-AE)')
            print('\033[33m[5] VER ATRIBUTOS')

            decision = info.make_decision('12345')

            # SE ATACAR COM ESPADA ──────────────────────────────────────────────────────────────────
            if decision == '1':
                if atributos['Energia'] < 5:
                    sleep(1)
                    print('\n\033[31mVocê não tem energia suficiente para essa ação.\033[m')
                    continue

                frase_sn = random.choice(frases_espada)
                possib = random.choice(chance)

                ataque_anterior.append(decision)
                if len(ataque_anterior) > 2:
                    ataque_anterior.pop(0)

                if possib != 9:
                    bonus_ea = random.choice((6, 7, 8, 9, 10))
                    if amount_ea != 36:
                        if amount_ea + bonus_ea > 36:
                            r_ea = 36 - amount_ea
                            amount_ea += r_ea
                        else:
                            amount_ea += bonus_ea

                    atributos['Energia'] = atributos['Energia'] - 5
                    if possib == 7 or possib == 8 or possib == 10:
                        vida_monstro -= (dano_espada + atributos['Critico'])
                        sleep(1)
                        print(frase_sn)
                        sleep(1)
                        print('\033[32mDano crítico!\033[m')
                    else:
                        vida_monstro -= dano_espada
                        sleep(1)
                        print(frase_sn)
                else:
                    print('\n\033[31mVocê errou!\033[m')

            # SE USAR ESCUDO PARA DEFESA ───────────────────────────────────────────────────────────
            elif decision == '2':
                if atributos['Energia'] < 0:
                    sleep(1)
                    print('\n\033[31mVocê não tem energia suficiente para essa ação.\033[m')
                    continue

                ataque_anterior.append(decision)
                if len(ataque_anterior) > 2:
                    ataque_anterior.pop(0)

                if ataque_anterior[0] == '2':
                    sleep(1)
                    print('\n\033[31mSeu escudo ainda está no chão!')
                    sleep(1)
                    print('\033[32mEspere mais uma rodada para executar essa ação.\033[m')
                    continue

                shield = True

                bonus_ea = random.choice((2, 3, 4, 5, 6))
                if amount_ea != 36:
                    if amount_ea + bonus_ea > 36:
                        r_ea = 36 - amount_ea
                        amount_ea += r_ea
                    else:
                        amount_ea += bonus_ea

                sleep(1)
                print('\033[32mVocê levanta seu escudo.')
                sleep(1)
                print('\033[32mVocê será protegido de qualquer ataque contra você.\033[m')

            # SE ATACAR COM ESCUDO ───────────────────────────────────────────────────────────
            elif decision == '3':
                if atributos['Energia'] < 2:
                    sleep(1)
                    print('\n\033[31mVocê não tem energia suficiente para essa ação.\033[m')
                    continue

                frase_sn = random.choice(frases_escudo)
                possib = random.choice(chance)

                ataque_anterior.append(decision)
                if len(ataque_anterior) > 2:
                    ataque_anterior.pop(0)

                if possib % 2 == 1:
                    bonus_ea = random.choice((8, 9, 10, 11, 12))
                    if amount_ea != 36:
                        if amount_ea + bonus_ea > 36:
                            r_ea = 36 - amount_ea
                            amount_ea += r_ea
                        else:
                            amount_ea += bonus_ea

                    atributos['Energia'] = atributos['Energia'] - 2
                    if possib == 3 or possib == 5:
                        vida_monstro -= (dano_escudo + atributos['Critico'])
                        sleep(1)
                        print(frase_sn)
                        sleep(1)
                        print('\033[32mDano crítico!\033[m')
                    else:
                        vida_monstro -= dano_escudo
                        sleep(1)
                        print(frase_sn)
                else:
                    print('\n\033[31mVocê errou!\033[m')

            # SE USAR HAN ───────────────────────────────────────────────────────────────────
            else:
                if amount_ea != 36:
                    sleep(1)
                    print('\n\033[31mHan ainda não está pronto!\033[m')
                    sleep(1)
                    print('\033[32mEncha seu \033[36mAtaque Especial\033[32m para executar essa ação.\033[m')
                    continue

                ataque_anterior.append(decision)
                if len(ataque_anterior) > 2:
                    ataque_anterior.pop(0)

                frase_sn = random.choice(frases_han)
                possib = random.choice(chance)

                amount_ea -= 35

                if possib == 6:
                    vida_monstro -= (dano_han + atributos['Critico'])
                    sleep(1)
                    print(frase_sn)
                    sleep(1)
                    print('\033[32mDano crítico!\033[m')
                else:
                    vida_monstro -= dano_han
                    sleep(1)
                    print(frase_sn)

        # CASO SEJA A VEZ DA NOELLE ────────────────────────────────────────────────────────────────
        if rodada == 2 and noelle is True:
            frases_noelle = (f'\033[32mNoelle ataca o {nome_monstro} com golpes marciais.\033[m',
                             '\033[32mNoelle lança flechas explosivas no monstro.\033[m',
                             f'\033[32mNoelle perfura o {nome_monstro} com flechas.\033[m')

            frase_nll = random.choice(frases_noelle)

            sleep(1)
            print('\033[32mÉ a vez de Noelle!\033[m\n')

            possib = random.choice(chance)
            if possib == 1:
                sleep(2)
                print('\033[31mNoelle tenta atacar o monstro, porém erra.\033[m')
            else:
                if possib == 2 or possib == 8 or possib == 10:
                    vida_monstro -= dano_noelle + noelle_atri['Critico']
                    sleep(2)
                    print(frase_nll)
                    sleep(1)
                    print('\033[32mDano crítico!\033[m')
                else:
                    vida_monstro -= dano_noelle
                    sleep(2)
                    print(frase_nll)

        # CASO NOELLE TENHA DESMAIADO ─────────────────────────────────────────────────────
        elif rodada == 2 and noelle is False:
            sleep(1)
            print('\033[31mNoelle não consegue atacar mais. Ela passa a rodada.')
            rodada += 1

        # CASO SEJA A VEZ DE GUSTAV ────────────────────────────────────────────────────────
        if rodada == 3 and gustav is True:
            frases_gustav = (f'\033[32mGustav ataca o {nome_monstro} com magia.\033[m',
                             '\033[32mGustav queima o monstro com fogo mágico.\033[m',
                             f'\033[32mGustav ativa seus poderes elétricos no {nome_monstro}.\033[m',
                             '\033[32mGustav joga o monstro no ar, fazendo ele cair com força no chão.\033[m',
                             f'\033[32mGustav invoca búfalos fantasma que atropelam o {nome_monstro}\033[m')

            frase_gv = random.choice(frases_gustav)

            sleep(1)
            print('\033[32mÉ a vez de Gustav!\033[m\n')

            possib = random.choice(chance)
            if possib == 1:
                sleep(2)
                print('\033[31mGustav tenta atacar o monstro, porém erra.\033[m')
            else:
                if possib == 1 or possib == 3 or possib == 6:
                    vida_monstro -= dano_gustav + gustav_atri['Critico']
                    sleep(2)
                    print(frase_gv)
                    sleep(1)
                    print('\033[32mDano crítico!\033[m')
                else:
                    vida_monstro -= dano_gustav
                    sleep(2)
                    print(frase_gv)

        # CASO GUSTAV TENHA DESMAIADO ───────────────────────────────────────────────────────
        elif rodada == 3 and gustav is False:
            sleep(1)
            print('\033[31mGustav não consegue atacar mais. Ele passa a rodada.')
            rodada += 1
            continue

        sleep(1)
        print(end='\n')

        # PARA MONSTRO ATACAR ──────────────────────────────────────────────────────────────
        if vida_monstro > 0:

            possib = random.choice(chance)
            atacar = random.choice(characters)

            if possib == 1 or possib == 5 or possib == 10:
                if atacar == personagem['Nome']:
                    sleep(1)
                    print(f'\033[32m{nome_monstro} tenta atacar você, mas erra.\033[m')
                else:
                    sleep(1)
                    print(f'\033[32m{nome_monstro} tenta atacar {atacar}, mas erra.\033[m')
            else:
                if atacar == personagem['Nome']:
                    sleep(1)
                    print(f'\033[32m{nome_monstro} ataca você.')

                    bonus_ea = random.choice((1, 2))
                    if amount_ea != 36:
                        if amount_ea + bonus_ea > 36:
                            r_ea = 36 - amount_ea
                            amount_ea += r_ea
                        else:
                            amount_ea += bonus_ea

                    if shield is True:
                        sleep(1)
                        print('\033[32mSeu escudo protege você.\033[m')
                        shield = False
                        sleep(1)
                        print('\033[31mVocê deixa seu escudo cair.\033[m')

                    else:
                        if dano_monstro > atributos['Vida']:
                            dano_monstro = atributos['Vida']
                            atributos['Vida'] -= dano_monstro
                            sleep(1)
                            print(f'Você perde {dano_monstro} de \033[31mVida\033[m')
                        else:
                            atributos['Vida'] = atributos['Vida'] - dano_monstro
                            sleep(1)
                            print(f'\033[32mVocê perde {dano_monstro} de \033[31mVida\033[m')
                else:
                    sleep(1)
                    print(f'\033[31m{nome_monstro} ataca {atacar}.')

                    if atacar == noelle_atri['Nome']:
                        noelle_atri['Vida'] = noelle_atri['Vida'] - round(ataque_monstro * (100 / (100 + noelle_atri['Defesa'])))
                    elif atacar == gustav_atri['Nome']:
                        gustav_atri['Vida'] = gustav_atri['Vida'] - round(ataque_monstro * (100 / (100 + gustav_atri['Defesa'])))

        rodada += 1


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
