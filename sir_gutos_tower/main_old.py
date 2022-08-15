# -*- coding: utf-8 -*-
from time import sleep
from os import path
import sir_gutos_tower.info as info


# ESCOLHER QUAL FUNÇÃO DO JOGO RODAR
def rodar_funcao(arquivo):
    with open('.save') as save:
        tamanho = path.getsize('.save')

        if tamanho:
            files = save.readlines()
            act = files[0].strip()

        if info.perso_info['Classe'] == 'Feiticeiro':
            funcoes_jogo = {
                'intro.': game_witcher_intro,
                'ato 1.': game_witcher_ato1,
                'ato 2.': game_witcher_ato2,
                'ato 3.': game_witcher_ato3
            }

        elif info.perso_info['Classe'] == 'Cavalheiro':
            funcoes_jogo = {
                'intro.': game_knight_intro,
                'ato 1.': game_knight_ato1,
                'ato 2.': game_knight_ato2,
                'ato 3.': game_knight_ato3
            }

        else:
            funcoes_jogo = {
                'intro.': game_archer_intro,
                'ato 1.': game_archer_ato1,
                'ato 2.': game_archer_ato2,
                'ato 3.': game_archer_ato3
            }

        if tamanho <= 2:
            perdeu = funcoes_jogo['intro.'](arquivo)
        else:
            perdeu = funcoes_jogo[act](arquivo)

    return perdeu


#    ▄████████    ▄████████  ▄█      ███      ▄█   ▄████████    ▄████████  ▄█     ▄████████  ▄██████▄
#   ███    ███   ███    ███ ███  ▀█████████▄ ███  ███    ███   ███    ███ ███    ███    ███ ███    ███
#   ███    █▀    ███    █▀  ███▌    ▀███▀▀██ ███▌ ███    █▀    ███    █▀  ███▌   ███    ███ ███    ███
#  ▄███▄▄▄      ▄███▄▄▄     ███▌     ███   ▀ ███▌ ███         ▄███▄▄▄     ███▌  ▄███▄▄▄▄██▀ ███    ███
# ▀▀███▀▀▀     ▀▀███▀▀▀     ███▌     ███     ███▌ ███        ▀▀███▀▀▀     ███▌ ▀▀███▀▀▀▀▀   ███    ███
#   ███          ███    █▄  ███      ███     ███  ███    █▄    ███    █▄  ███  ▀███████████ ███    ███
#   ███          ███    ███ ███      ███     ███  ███    ███   ███    ███ ███    ███    ███ ███    ███
#   ███          ██████████ █▀      ▄████▀   █▀   ████████▀    ██████████ █▀     ███    ███  ▀██████▀
#                                                                                ███    ███
# ATO 3
def game_witcher_ato3(arquivo):
    info.achieve('Últimos passos')

    with open('.save') as save:

        inventario = False
        for l in save:
            if 'Inventario: True' in l:
                inventario = True

    info.setar_atri()

    if inventario:
        info.setar_inve()

    info.modi_file('Doug: True\n', '.save', 4)
    info.modi_file('Noelle: True\n', '.save', 5)

    # ATO 3 ───────────────────────────────────────────────────────────────────────
    sleep(1)
    print(f'\n\033[94m{" ATO 3":─>40}\033[m')
    sleep(1)

    info.narrativa('ato_3.', arquivo)

    luta = info.fight_witch('Sir Guto', 700, 10, 16, 3)

    # SE GANHARAM ─────────────────────────────────────────────────────────────────
    if luta[0]:
        info.narrativa('ganhou_sir_guto.', arquivo)

    # SE PERDEU E NÃO QUER JOGAR NOVAMENTE ────────────────────────────────────────
    else:
        info.narrativa('perdeu_sir_guto.', arquivo)

        info.mensagem_morte('Você são derrotados pelo poder extremo de Sir Guto')
        return True

    soube_motivo_doug = False
    soube_motivo_noelle = False

    while True:
        if soube_motivo_doug and soube_motivo_noelle:
            break

        decision = info.make_decision('Saber motivos de Doug_Saber motivos de Noelle')

        # SABER MOTIVOS DE DOUG ─────────────────────────────────────────────────────────────────────────────
        if decision == '1':
            info.narrativa('motivos_doug.', arquivo)
            soube_motivo_doug = True

        # SABER MOTIVOS DE NOELLE ───────────────────────────────────────────────────────────────────────────
        else:
            info.narrativa('motivos_noelle.', arquivo)
            soube_motivo_noelle = True

    decision = info.make_decision('Doug_Noelle_Você_Todos', 'Quem você vai escolher?')

    # ESCOLHER DOUG ─────────────────────────────────────────────────────────────────────────────────────
    if decision == '1':
        info.narrativa('escolher_doug.', arquivo)

    # ESCOLHER NOELLE ───────────────────────────────────────────────────────────────────────────────────
    elif decision == '2':
        info.narrativa('escolher_noelle.', arquivo)

    # ESCOLHER VOCÊ MESMO ───────────────────────────────────────────────────────────────────────────────
    elif decision == '3':
        info.narrativa('escolher_você.', arquivo)
        info.achieve('Sacrifícios necessários')

    # ESCOLHER TODOS ────────────────────────────────────────────────────────────────────────────────────
    else:
        info.narrativa('escolher_todos.', arquivo)

        sleep(3)
        info.narrativa('consequencia_escolher_todos.', arquivo)

        while True:
            decision = info.make_decision('Doug_Noelle_Você_Todos', 'Quem você vai escolher?')

            if decision != '4':
                sleep(1)
                print('\n\033[31mVocê não pode mudar de ideia.\033[m')

            else:
                info.narrativa('final_misterioso.', arquivo)
                info.achieve('Quebra de realidade')

    sleep(2)
    print(f'\033[93m{" FIM DO JOGO ":─^40}\033[m')
    return True


# ATO 2
def game_witcher_ato2(arquivo):
    with open('.save') as save:

        inventario = False
        for l in save:
            if 'Inventario: True' in l:
                inventario = True

            if 'outra_entrada: ato1_esconder' in l:
                caminho = 'outra_entrada: ato1_esconder'

            elif 'outra_entrada: ato1_lutar' in l:
                caminho = 'outra_entrada: ato1_lutar'

    info.setar_atri()

    if inventario:
        info.setar_inve()

    info.modi_file('Doug: False\n', '.save', 4)
    info.modi_file('Noelle: False\n', '.save', 5)

    # ATO 2 ──────────────────────────────────────────────────────────────────────
    sleep(1)
    print(f'\n\033[35m{" ATO 2":─>40}\033[m')
    sleep(1)

    # SE CAMINHO = 'ATO1_ESCONDER'
    # DOUG = FALSE
    # INVENTARIO = FALSE ou TRUE
    # NOELLE VAI ATRÁS DE DOUG ANTES QUE O JOGADOR ENTRE NA TORRE
    if 'ato1_esconder' in caminho:
        info.narrativa('ato_2_1.', arquivo)

        decision = info.make_decision('Lutar com o javali \033[35m(-? E)_Ignorar o animal')

        # LUTAR COM O JAVALI ──────────────────────────────────────────────────────────────────────────
        if decision == '1':
            luta = info.fight_witch('Javali Elemental', 150, 8, 4, 4)  # VIDA_MONSTRO = 150

            # SE PERDEU E > NÃO < QUER JOGAR NOVAMENTE
            if not luta:
                info.death_count()
                return True

            info.narrativa('lutar_javali.', arquivo)

            info.attributes['Magia'] += 15
            info.attributes['Defesa'] += 5
            sleep(2)
            print('\n\033[33mSUA MAGIA E DEFESA FORAM AUMENTADAS\033[m')

        else:
            info.narrativa('sair_javali.', arquivo)

        info.narrativa('continuar_ato_2_1.', arquivo)
        info.achieve('O Cavalheiro')
        info.modi_file('Doug: True\n', '.save', 4)


    # SE CAMINHO = 'ATO1_LUTAR'
    # DOUG = TRUE
    # INVENTARIO = FALSE
    # NOELLE ENTRA NA TORRE PRIMEIRO QUE OS DOIS
    elif 'ato1_lutar' in caminho:
        info.narrativa('ato_2_2.', arquivo)

        decision = info.make_decision('Lutar como o javali \033[35m(-? E)_Ignorar o animal')

        # LUTAR COM O JAVALI ──────────────────────────────────────────────────────────────────────────
        if decision == '1':
            luta = info.fight_witch('Javali Elemental', 150, 8, 4, 4)  # VIDA_MONSTRO = 150

            # SE PERDEU E > NÃO < QUER JOGAR NOVAMENTE
            if not luta:
                info.death_count()
                return True

            info.narrativa('lutar_javali.', arquivo)

            info.attributes['Magia'] += 15
            info.attributes['Defesa'] += 5
            sleep(2)
            print('\n\033[33mSUA MAGIA E DEFESA FORAM AUMENTADAS\033[m')

        # IGNORAR O ANIMAL ──────────────────────────────────────────────────────────────────────────────
        else:
            info.narrativa('sair_javali.', arquivo)

        # ───────────────────────────────────────────────────────────────────────────────────────────────

    # CONTINUANDO ───────────────────────────────────────────────────────────────────────────────────────
    info.narrativa('primeira_sala.', arquivo)

    while True:
        decision = info.make_decision('⇽ ESQUERDA_DIREITA ⇾', 'Para onde você vai?')

        # SALA DE ESTAR ─ ESQUERDA ──────────────────────────────────────────────────────────────────────
        if decision == '1':
            break

        # CÔMODO COM LOBOS ─ DIREITA ─────────────────────────────────────────────────────────────────────
        else:
            info.narrativa('lobos.', arquivo)

            info.mensagem_morte('Você e Doug são devorados impiedosamente.')
            return True

    # SALA DE ESTAR ─ ESQUERDA ────────────────────────────────────────────────────────────────────────────
    if decision == '1':
        info.narrativa('sala_estar.', arquivo)

        decision = info.make_decision('Ajudar a mulher (-0 E)_Esperar que ela perca \033[35m(-? E)')

        # AJUDAR A MULHER ────────────────────────────────────────────────────────────────────────────────
        if decision == '1':
            info.narrativa('ajudar_noelle.', arquivo)

            info.modi_file('Noelle: True\n', '.save', 5)
            info.achieve('A Arqueira')

        # ESPERAR QUE ELA PERCA ───────────────────────────────────────────────────────────────────────────
        else:
            info.narrativa('nao_ajudar_noelle.', arquivo)

            luta = info.fight_witch('Monstro', 63, 31, 25, 2)

            # SE PERDEU E > NÃO < QUER JOGAR NOVAMENTE
            if not luta:
                info.death_count()
                return True

            info.narrativa('ganhou_monstro_noelle.', arquivo)

            info.modi_file('Doug: False\n', '.save', 4)
            info.achieve('Até que a morte nos separe')

            info.narrativa('continuar_monstro_noelle.', arquivo)

            info.mensagem_morte('Você é derrotado pelo poder absurdo de Sir Guto')
            return True

    # CONTINUANDO ───────────────────────────────────────────────────────────────────────────────────
    info.narrativa('continuar_noelle.', arquivo)

    sleep(1)
    print('\n\033[32mVocês sobem para o último andar, onde encontram Sir Guto, esperando por vocês\033[m')

    info.show_achieve()

    sleep(1)
    print('\n\033[37mSalvando progresso... Não interrompa o programa.\033[m')
    sleep(2)
    
    info.modi_file('ato 3.\n', '.save', 0)
    info.save_atri()

    with open('.save') as save:
        save = save.read()

        for k in info.itens:
            if k not in info.inventario and k in save:
                info.deledecision = info.make_decision('Lutar um por um \033[35m(-? E)_Se desesperar \033[35m(-? E)')

    return False


# ATO 1
def game_witcher_ato1(arquivo):
    info.modi_file('Inventario: False\n', '.save', 2)
    info.modi_file('Itens: \n', '.save', 3)

    info.modi_file('Doug: False\n', '.save', 4)
    info.modi_file('Noelle: False\n', '.save', 5)

    info.save_atri()

    # ATO 1 ───────────────────────────────────────────────────────────────────────────────────────
    sleep(1)
    print(f'\n\033[31m{" ATO 1":─>40}\033[m')

    info.narrativa('ato_1.', arquivo)

    decision = info.make_decision('Ir pela ponte mesmo assim \033[35m(-? E)_Achar outro caminho (-0 E)_'
                                  'Usar magia para atravessar o outro lado (-25 E)')

    # SE FOR PELA PONTE ────────────────────────────────────────────────────────────────────────────
    if decision == '1':
        info.narrativa('ponte.', arquivo)

        decision = info.make_decision('Voltar para a superfície \033[31m(-210 E)_Entrar na caverna (-0 E)')

        # SE VOLTAR PARA A SUPERFÍCIE ─────────────────────────────────────────────────────────────────
        if decision == '1':
            info.narrativa('superficie_ponte.', arquivo)
            info.attributes['Energia'] -= 210

            info.mensagem_morte('Você cai todo o penhasco novamente e morre uma dor excruciante nos espinhos.')
            return True

        # SE ENTRAR NA CAVERNA ──────────────────────────────────────────────────────────────────────────
        else:
            info.narrativa('caverna_ponte.', arquivo)
            info.achieve('Caminho impossível')

            luta = info.fight_witch('Sir Dragon', 10000, 2500, 5000, 0)

            # SE PERDEU A LUTA E NÃO QUER TENTAR NOVAMENTE ─────────────────────────
            if luta is False:
                info.death_count()
                return True

    # SE PROCURAR OUTRO CAMINHO ────────────────────────────────────────────────────────
    elif decision == '2':
        info.narrativa('outro_caminho.', arquivo)

        info.mensagem_morte('Você morre de cansaço.')
        return True

    # SE ATRAVESSAR COM MAGIA ───────────────────────────────────────────────────────────
    else:
        info.narrativa('atravessar_magia.', arquivo)
        info.attributes['Energia'] -= 25

        decision = info.make_decision('Entrar pela porta da frente \033[35m(-? E)_'
                                      'Procurar outra entrada (-0 E)')

        # ENTRAR PELA PORTA DA FRENTE ──────────────────────────────────────────────────
        if decision == '1':
            info.narrativa('porta_atravessar_magia.', arquivo)

            info.mensagem_morte('Você é devorad{a} impiedosamente.')
            return True

        # PROCURAR OUTRA ENTRADA ───────────────────────────────────────────────────────
        else:
            info.modi_file(' outra_entrada: ', '.save', 1, 'a')
            info.narrativa('outro_atravessar_magia.', arquivo)

            decision = info.make_decision('Se esconder (-2 E)_Se preparar para lutar (-0 E)')

            # SE ESCONDER ───────────────────────────────────────────────────────────────
            if decision == '1':
                info.modi_file(' ato1_esconder', '.save', 1, 'a')

                info.narrativa('esconder_atravessar_magia.', arquivo)
                info.attributes['Energia'] -= 2

                decision = info.make_decision('Pegar item que o homem deixou cair (-0 E)_'
                                              'Entrar na torre atrás dele (-0 E)')

                # PEGAR ITEM QUE O HOMEM DEIXOU CAIR ────────────────────────────────────
                if decision == '1':
                    info.narrativa('pegar_item_atravessar_magia.', arquivo)

                    info.modi_file('Inventario: True\n', '.save', 2)
                    info.achieve('Um peso a mais')

                    info.add_inve('Barrinha Protein')

                    sleep(1)
                    print('\n\033[32mVocê coleta o item. É uma barrinha de Energia!')
                    sleep(2)
                    print('\033[33mVOCÊ DESBLOQUEOU INVENTÁRIO\033[m')
                    sleep(2)
                    print('\033[32mInventário vai estar disponível nos momentos de escolha de agora em diante.\033[m')

                    sleep(1)
                    print('\n\033[32mVocê conseguiu entrar na Torre com sucesso.\033[m')
                    info.achieve('O que esperar?')
                    sleep(1)

                # ENTRAR NA TORRE ATRÁS DELE ────────────────────────────────────────────
                else:
                    info.narrativa('logo_atras_atravessar_magia.', arquivo)

                    sleep(1)
                    print('\n\033[32mVocê conseguiu entrar na Torre com sucesso.\033[m')
                    info.achieve('O que esperar?')
                    sleep(1)

            # SE PREPARAR PARA LUTAR ────────────────────────────────────────────────────
            else:
                info.narrativa('lutar_atravessar_magia.', arquivo)
                info.modi_file(' ato1_lutar,', '.save', 1, 'a')
                info.modi_file('Doug: True\n', '.save', 4)

                sleep(1)
                print('\n\033[32mVocê e Doug conseguiram entrar na Torre com sucesso.\033[m')
                info.achieve('O que esperar?')
                info.achieve('O Cavalheiro')
                sleep(1)

    info.show_achieve()

    sleep(1)
    print('\n\033[37mSalvando progresso... Não interrompa o programa.\033[m')
    sleep(2)

    info.modi_file('ato 2.\n', '.save', 0)
    info.save_atri()
    info.add_inve('Barrinha Protein', 'm')

    return False


# INTRO
def game_witcher_intro(arquivo):
    info.achieve('Que a magia esteja com você')

    info.modi_file('intro.\n', '.save', 0)
    info.modi_file('caminho:\n', '.save', 1)

    info.modi_file('Inventario: False\n', '.save', 2)
    info.modi_file('Itens: \n', '.save', 3)

    # INTRODUÇÃO ─────────────────────────────────────────────────────────────────────────────────
    info.narrativa('intro.', arquivo)

    print('\n\033[33mSUA \033[95mENERGIA\033[33m AUMENTA 2x! O suficiente para viajar!\033[m')
    info.attributes['Energia'] += 200

    info.narrativa('intro_2.', arquivo)

    decision = info.make_decision('Ir a pé (-0 E)_Fazer um portal (-200 E)')

    # SE DECIDIR IR A PÉ ──────────────────────────────────────────────────────────────────────
    if decision == '1':
        info.narrativa('andar_intro.', arquivo)

        info.mensagem_morte('Você morre de cansaço.')
        return True

    # SE DECIDIR IR POR PORTAL ────────────────────────────────────────────────────────────────
    else:
        info.attributes['Energia'] -= 200

        info.narrativa('portal_intro.', arquivo)

    info.show_achieve()

    sleep(1)
    print('\n\033[37mSalvando progresso... Não interrompa o programa.\033[m')
    sleep(2)

    info.modi_file('ato 1.\n', '.save', 0)

    return False


#  ▄████████    ▄████████  ▄█    █▄     ▄████████  ▄█          ▄█    █▄       ▄████████  ▄█     ▄████████  ▄██████▄
# ███    ███   ███    ███ ███    ███   ███    ███ ███         ███    ███     ███    ███ ███    ███    ███ ███    ███
# ███    █▀    ███    ███ ███    ███   ███    ███ ███         ███    ███     ███    █▀  ███▌   ███    ███ ███    ███
# ███          ███    ███ ███    ███   ███    ███ ███        ▄███▄▄▄▄███▄▄  ▄███▄▄▄     ███▌  ▄███▄▄▄▄██▀ ███    ███
# ███        ▀███████████ ███    ███ ▀███████████ ███       ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ███▌ ▀▀███▀▀▀▀▀   ███    ███
# ███    █▄    ███    ███ ███    ███   ███    ███ ███         ███    ███     ███    █▄  ███  ▀███████████ ███    ███
# ███    ███   ███    ███ ███    ███   ███    ███ ███▌    ▄   ███    ███     ███    ███ ███    ███    ███ ███    ███
# ████████▀    ███    █▀   ▀██████▀    ███    █▀  █████▄▄██   ███    █▀      ██████████ █▀     ███    ███  ▀██████▀
#                                                 ▀                                            ███    ███
# ATO 3
def game_knight_ato3(arquivo):
    info.achieve('Últimos passos')

    with open('.save') as save:

        inventario = False
        for l in save:
            if 'Inventario: True' in l:
                inventario = True

    info.setar_atri()

    if inventario:
        info.setar_inve()
        
    info.modi_file('Gustav: True\n', '.save', 4)
    info.modi_file('Noelle: True\n', '.save', 5)

    # ATO 3 ───────────────────────────────────────────────────────────────────────
    sleep(1)
    print(f'\n\033[94m{" ATO 3":─>40}\033[m')
    sleep(1)

    info.narrativa('ato_3.', arquivo)

    luta = info.fight_knight('Sir Guto', 0, 10, 16, 3)

    # SE GANHARAM ─────────────────────────────────────────────────────────────────
    if luta[0]:
        info.narrativa('ganhou_sir_guto.', arquivo)

    # SE PERDEU E NÃO QUER JOGAR NOVAMENTE ────────────────────────────────────────
    else:
        info.narrativa('perdeu_sir_guto.', arquivo)

        info.mensagem_morte('Você são derrotados pelo poder extremo de Sir Guto')
        return True

    soube_motivo_gustav = False
    soube_motivo_noelle = False

    while True:
        if soube_motivo_gustav and soube_motivo_noelle:
            break

        decision = info.make_decision('Saber motivos de Gustav_Saber motivos de Noelle')

        # SABER MOTIVOS DE GUSTAV ─────────────────────────────────────────────────────────────────────────────
        if decision == '1':
            info.narrativa('motivos_gustav.', arquivo)
            soube_motivo_gustav = True

        # SABER MOTIVOS DE NOELLE ───────────────────────────────────────────────────────────────────────────
        else:
            info.narrativa('motivos_noelle.', arquivo)
            soube_motivo_noelle = True

    decision = info.make_decision('Gustav_Noelle_Você_Todos', 'Quem você vai escolher?')

    # ESCOLHER GUSTAV ─────────────────────────────────────────────────────────────────────────────────────
    if decision == '1':
        info.narrativa('escolher_gustav.', arquivo)

    # ESCOLHER NOELLE ───────────────────────────────────────────────────────────────────────────────────
    elif decision == '2':
        info.narrativa('escolher_noelle.', arquivo)

    # ESCOLHER VOCÊ MESMO ───────────────────────────────────────────────────────────────────────────────
    elif decision == '3':
        info.narrativa('escolher_você.', arquivo)
        info.achieve('Sacrifícios necessários')

    sleep(2)
    print(f'\033[93m{" FIM DO JOGO ":─^40}\033[m')
    return True


# ATO 2
def game_knight_ato2(arquivo):
    info.modi_file('caminho:\n', '.save', 1)

    info.modi_file('Gustav: False\n', '.save', 4)
    info.modi_file('Noelle: False\n', '.save', 5)

    with open('.save') as save:

        inventario = False
        for l in save:
            if 'Inventario: True' in l:
                inventario = True

    info.setar_atri()

    if inventario:
        info.setar_inve()

    # ATO 2 ───────────────────────────────────────────────────────────────────────────────────
    sleep(1)
    print(f'\n\033[35m{" ATO 2":─>40}\033[m')
    sleep(1)

    info.narrativa('ato_2.', arquivo)

    decision = info.make_decision('Lutar com o javali \033[35m(-? E)_Deixar o javali em paz (-0 E)')

    # LUTAR COM O JAVALI ──────────────────────────────────────────────────────────────────────
    if decision == '1':
        luta = info.fight_knight('Javali Elemental', 150, 8, 4, 4)  # VIDA_MONSTRO = 150

        # SE PERDEU E > NÃO < QUER JOGAR NOVAMENTE
        if not luta:
            info.death_count()
            return True

        info.narrativa('lutar_javali.', arquivo)

        sleep(1)
        print('\n\033[32mVocê pega a presa do chão.')
        sleep(1)
        print('\033[33mSEU ATAQUE AUMENTA\033[m')
        sleep(2)

        info.attributes['Ataque'] += 10

    # DEIXAR JAVALI EM PAZ ─────────────────────────────────────────────────────────────────────
    else:
        info.narrativa('nao_lutar_javali.', arquivo)

    # CONTINUAR ────────────────────────────────────────────────────────────────────────────────
    info.narrativa('subir_torre.', arquivo)

    info.achieve('O Feiticeiro')
    info.modi_file('Gustav: True\n', '.save', 4)

    sleep(1)
    print('\n\033[33mGUSTAV ENTROU NA FESTA\033[m')
    sleep(2)

    info.narrativa('primeira_sala.', arquivo)

    decision = info.make_decision('⇽ ESQUERDA_DIREITA ⇾', 'Para onde você vai?')

    # ESQUERDA ─────────────────────────────────────────────────────────────────────────────────
    if decision == '1':
        info.narrativa('esquerda.', arquivo)

        decision = info.make_decision('Ajudar a mulher \033[35m(-? E)_Esperar ela perder \033[35m(-? E)')

        # AJUDAR A MULHER ──────────────────────────────────────────────────────────────────────
        if decision == '1':
            info.narrativa('ajudar_noelle.', arquivo)

            info.achieve('A Arqueira')
            info.modi_file('Noelle: True\n', '.save', 5)

            sleep(1)
            print('\n\033[33mNOELLE ENTROU NA FESTA\033[m')
            sleep(2)

            info.narrativa('continuar_noelle.', arquivo)

            sleep(1)
            print('\n\033[32mVocês sobem para o último andar, onde encontram Sir Guto, esperando por vocês\033[m')

        # ESPERAR ELA PERDER ───────────────────────────────────────────────────────────────────
        else:
            info.narrativa('nao_ajudar_noelle.', arquivo)

            luta = info.fight_knight('Monstro', 63, 31, 25, 2)  # VIDA_MONSTRO = 150

            # SE PERDEU E > NÃO < QUER JOGAR NOVAMENTE
            if not luta:
                info.death_count()
                return True

            info.narrativa('ganhou_monstro_noelle.', arquivo)

            info.achieve('Até que a morte nos separe')
            info.modi_file('Gustav: False\n', '.save', 4)

            sleep(1)
            print('\n\033[31mGUSTAV SAIU NA FESTA\033[m')
            sleep(2)

            info.narrativa('continuar_monstro_noelle.', arquivo)

            info.mensagem_morte('Você morre pelo poder extremo de Sir Guto.')
            return True

    # DIREITA ──────────────────────────────────────────────────────────────────────────────────
    else:
        info.narrativa('lobos.', arquivo)

        info.mensagem_morte('Você e Gustav são devorados impiedosamente.')
        return True

    info.show_achieve()

    sleep(1)
    print('\n\033[37mSalvando progresso... Não interrompa o programa.\033[m')
    sleep(2)

    info.modi_file('ato 3.\n', '.save', 0)
    info.save_atri()

    with open('.save') as save:
        save = save.read()

        for k in info.itens:
            if k not in info.inventario and k in save:
                info.delet_item_inve(k)

    return False


# ATO 1
def game_knight_ato1(arquivo):
    info.modi_file('caminho:\n', '.save', 1)

    info.modi_file('Inventario: False\n', '.save', 2)
    info.modi_file('Itens: \n', '.save', 3)

    info.modi_file('Gustav: False\n', '.save', 4)
    info.modi_file('Noelle: False\n', '.save', 5)

    # ATO 1 ──────────────────────────────────────────────────────────────────────────────────
    sleep(1)
    print(f'\n\033[31m{" ATO 1":─>40}\033[m')

    info.narrativa('ato_1.', arquivo)

    decision = info.make_decision('Ir pelo caminho alegre_Ir pelo caminho sombrio e assustador')

    # IR PELO CAMINHO ALEGRE ─────────────────────────────────────────────────────────────────
    if decision == '1':
        info.narrativa('caminho_alegre_ato_1.', arquivo)

        info.mensagem_morte('Toda sua sanidade é sugada de você e você morre nos campos esverdeados com Han, o cavalo.')
        return True

    # IR PELO CAMINHO SOMBRIO E ASSUSTADOR ───────────────────────────────────────────────────
    else:
        info.narrativa('caminho_sombrio_ato_1.', arquivo)

        luta = info.fight_knight('Sombrio', 100, 15, 5, 6)

        # SE PERDEU A LUTA E NÃO QUER TENTAR NOVAMENTE ───────────────────────────────────
        if not luta:
            info.death_count()
            return True

        info.narrativa('continuar_caminho_sombrio.', arquivo)

        decision = info.make_decision('Pegar_Não pegar')

        # PEGAR ──────────────────────────────────────────────────────────────────────────────
        if decision == '1':
            info.narrativa('pegar_barrinha_caminho_sombrio.', arquivo)
            info.modi_file('Inventario: True\n', '.save', 2)
            info.achieve('Um peso a mais')

            info.add_inve('Barrinha Protein')

            sleep(1)
            print('\033[33mVOCÊ DESBLOQUEOU INVENTÁRIO\033[m')
            sleep(2)
            print('\033[32mInventário vai estar disponível nos momentos de escolha de agora em diante.\033[m')

        # NÃO PEGAR ───────────────────────────────────────────────────────────────────────────
        else:
            info.narrativa('nao_pegar_barrinha_caminho_sombrio.', arquivo)

        # CONTINUAR ───────────────────────────────────────────────────────────────────────────
        info.narrativa('torre.', arquivo)

        decision = info.make_decision('Procurar entrada escondida_Procurar entrada visível')

        # PROCURAR ENTRADA ESCONDIDA ──────────────────────────────────────────────────────────
        if decision == '1':
            info.narrativa('procurar_entrada_escondida.', arquivo)

            sleep(1)
            print('\n\033[32mVocê conseguiu entrar na Torre com sucesso.')

        # PROCURAR ENTRADA VISÍVEL ────────────────────────────────────────────────────────────
        else:
            info.narrativa('procurar_entrada_visivel.', arquivo)

            info.mensagem_morte('Você é devorad{a} impiedosamente.')
            return True

    info.show_achieve()

    sleep(1)
    print('\n\033[37mSalvando progresso... Não interrompa o programa.\033[m')
    sleep(2)

    info.modi_file('ato 2.\n', '.save', 0)
    info.save_atri()
    info.add_inve('Barrinha Protein', 'm')

    return False


# INTRO
def game_knight_intro(arquivo):
    info.achieve('Um por todos e todos por um')

    info.modi_file('intro.\n', '.save', 0)
    info.modi_file('caminho:\n', '.save', 1)

    info.modi_file('Inventario: False\n', '.save', 2)
    info.modi_file('Itens: \n', '.save', 3)

    info.modi_file('Gustav: False\n', '.save', 4)
    info.modi_file('Noelle: False\n', '.save', 5)

    # INTRODUÇÃO ──────────────────────────────────────────────────────────────────────────
    info.narrativa('intro.', arquivo)

    info.show_achieve()

    sleep(1)
    print('\n\033[37mSalvando progresso... Não interrompa o programa.\033[m')
    sleep(2)

    info.modi_file('ato 1.\n', '.save', 0)

    return False


#    ▄████████    ▄████████ ████████▄   ███    █▄     ▄████████  ▄█     ▄████████  ▄██████▄
#   ███    ███   ███    ███ ███    ███  ███    ███   ███    ███ ███    ███    ███ ███    ███
#   ███    ███   ███    ███ ███    ███  ███    ███   ███    █▀  ███▌   ███    ███ ███    ███
#   ███    ███  ▄███▄▄▄▄██▀ ███    ███  ███    ███  ▄███▄▄▄     ███▌  ▄███▄▄▄▄██▀ ███    ███
# ▀███████████ ▀▀███▀▀▀▀▀   ███    ███  ███    ███ ▀▀███▀▀▀     ███▌ ▀▀███▀▀▀▀▀   ███    ███
#   ███    ███ ▀███████████ ███    ███  ███    ███   ███    █▄  ███  ▀███████████ ███    ███
#   ███    ███   ███    ███ ███  ▀ ███  ███    ███   ███    ███ ███    ███    ███ ███    ███
#   ███    █▀    ███    ███  ▀██████▀▄█ ████████▀    ██████████ █▀     ███    ███  ▀██████▀
#                ███    ███                                            ███    ███
# ATO 3
def game_archer_ato3(arquivo):
    info.achieve('Últimos passos')

    with open('.save') as save:

        inventario = False
        for l in save:
            if 'Inventario: True' in l:
                inventario = True

    info.setar_atri()

    if inventario:
        info.setar_inve()

    info.modi_file('Gustav: True\n', '.save', 4)
    info.modi_file('Doug: True\n', '.save', 5)

    # ATO 3 ───────────────────────────────────────────────────────────────────────
    sleep(1)
    print(f'\n\033[94m{" ATO 3":─>40}\033[m')
    sleep(1)

    info.narrativa('ato_3.', arquivo)

    luta = info.fight_archer('Sir Guto', 700, 10, 16, 3)

    # SE GANHARAM ─────────────────────────────────────────────────────────────────
    if luta[0]:
        info.narrativa('ganhou_sir_guto.', arquivo)

    # SE PERDEU E NÃO QUER JOGAR NOVAMENTE ────────────────────────────────────────
    else:
        info.narrativa('perdeu_sir_guto.', arquivo)

        info.mensagem_morte('Você são derrotados pelo poder extremo de Sir Guto')
        return True

    soube_motivo_gustav = False
    soube_motivo_doug = False

    while True:
        if soube_motivo_gustav and soube_motivo_doug:
            break

        decision = info.make_decision('Saber motivos de Gustav_Saber motivos de Doug')

        # SABER MOTIVOS DE GUSTAV ─────────────────────────────────────────────────────────────────────────────
        if decision == '1':
            info.narrativa('motivos_gustav.', arquivo)
            soube_motivo_gustav = True

        # SABER MOTIVOS DE DOUG ───────────────────────────────────────────────────────────────────────────
        else:
            info.narrativa('motivos_doug.', arquivo)
            soube_motivo_doug = True

    decision = info.make_decision('Gustav_Doug_Você_Todos', 'Quem você vai escolher?')

    # ESCOLHER GUSTAV ─────────────────────────────────────────────────────────────────────────────────────
    if decision == '1':
        info.narrativa('escolher_gustav.', arquivo)

    # ESCOLHER DOUG ───────────────────────────────────────────────────────────────────────────────────
    elif decision == '2':
        info.narrativa('escolher_doug.', arquivo)

    # ESCOLHER VOCÊ MESMO ───────────────────────────────────────────────────────────────────────────────
    elif decision == '3':
        info.narrativa('escolher_você.', arquivo)
        info.achieve('Sacrifícios necessários')

    sleep(2)
    print(f'\033[93m{" FIM DO JOGO ":─^40}\033[m')
    return True


# ATO 2
def game_archer_ato2(arquivo):
    with open('.save') as save:

        inventario = False
        for l in save:
            if 'Inventario: True' in l:
                inventario = True

            if 'ato1_antes_doug' in l:
                caminho = 'ato1_antes_doug'

            elif 'ato1_depois_doug' in l:
                caminho = 'ato1_depois_doug'

    info.setar_atri()

    if inventario:
        info.setar_inve()

    info.modi_file('Gustav: False\n', '.save', 4)
    info.modi_file('Doug: False\n', '.save', 5)

    conhece_gustav = False
    gustav = False
    # ATO 2 ───────────────────────────────────────────────────────────────────────────────────────
    sleep(1)
    print(f'\n\033[35m{" ATO 2":─>40}\033[m')
    sleep(1)

    # SE CAMINHO = 'ATO1_ANTES_DOUG'
    # INVENTARIO = FALSE ou TRUE
    # JOGADOR ENTRA NA TORRE ANTES DE DOUG
    if caminho == 'ato1_antes_doug':
        info.narrativa('ato_2_1.', arquivo)

        decision = info.make_decision('Lutar com o javali_Deixá-lo em paz')

        # LUTAR COM O JAVALI ─────────────────────────────────────────────────────────────────────────────
        if decision == '1':
            luta = info.fight_archer('Javali Elemental', 150, 8, 4, 4)

            if not luta:
                info.death_count()
                return True

            info.narrativa('lutar_javali.', arquivo)

            info.attributes['Flecha'] += 10
            sleep(1)
            print('\n\033[33mO DANO DAS SUAS FLECHAS AUMENTARAM!\033[m')
            sleep(2)

        # DEIXÁ-LO EM PAZ ────────────────────────────────────────────────────────────────────────────────
        else:
            info.narrativa('sair_javali.', arquivo)

    # SE CAMINHO = 'ATO1_DEPOIS_DOUG'
    # INVENTARIO = FALSE ou TRUE
    # JOGADOR ENTRA NA TORRE DEPOIS DE DOUG E GUSTAV
    elif caminho == 'ato1_depois_doug':
        info.narrativa('ato_2_2.', arquivo)

        decision = info.make_decision('Nocautear os dois_Passar por eles de fininho')

        # NOCAUTEAR OS DOIS ─────────────────────────────────────────────────────────────────────────────────
        if decision == '1':
            info.narrativa('nocautear_os_dois.', arquivo)

            info.mensagem_morte('Você fica pres{a} por tempo suficiente para perder a chance de ter o item.')
            return True

        # PASSAR POR ELES DE FININHO ────────────────────────────────────────────────────────────────────────
        else:
            info.narrativa('passar_fininho.', arquivo)

    # CONTINUANDO ───────────────────────────────────────────────────────────────────────────────────────────
    info.narrativa('primeira_sala.', arquivo)

    while True:
        decision = info.make_decision('⇽ ESQUERDA_DIREITA ⇾', 'Para onde você vai?')

        # DIREITA ───────────────────────────────────────────────────────────────────────────────────────────
        if decision == '2':
            # se caminho for 'ato1_antes_doug', gustav vai aparecer caso jogador for pela direita
            if caminho == 'ato1_antes_doug':

                # se ainda não conhece gustav
                if not conhece_gustav:
                    info.narrativa('lobos_gustav_aviso.', arquivo)

                    decision = info.make_decision('Se juntar a Gustav_Não se juntar a ele.')

                    # SE JUNTAR A GUSTAV ────────────────────────────────────────────────────────────────────
                    if decision == '1':
                        info.modi_file('Gustav: True\n', '.save', 4)
                        info.achieve('O Feiticeiro')
                        gustav = True

                        sleep(1)
                        print('\n\033[33mGUSTAV ENTROU NA FESTA\033[m')
                        sleep(2)

                    # NÃO SE JUNTAR A ELE ───────────────────────────────────────────────────────────────────
                    else:
                        info.narrativa('lobos_gustav_recusar.', arquivo)

                    conhece_gustav = True
                    continue

                # se já conheceu gustav e ainda assim foi para a direita
                else:
                    with open('.save') as save:
                        save = save.read()

                        if 'Gustav: True' in save:
                            info.narrativa('lobos_ignorar_aviso_com_gustav.', arquivo)

                            info.mensagem_morte('Vocês são devorados impiedosamente.')
                            return True

                        else:
                            info.narrativa('lobos_ignorar_aviso_sem_gustav.', arquivo)

                            info.mensagem_morte('Você é devorad{a} impiedosamente.')
                            return True

            else:
                info.narrativa('lobos.', arquivo)

                info.mensagem_morte('Você é devorad{a} impiedosamente.')
                return True

        else:
            break

    # CONTINUAR COM GUSTAV ───────────────────────────────────────────────────────────────────────────────────
    if gustav:
        info.narrativa('sala_estar_gustav.', arquivo)

        decision = info.make_decision('Lutar um por um_Observar a sala_Pedir ajuda a Gustav')

        # LUTAR UM POR UM ───────────────────────────────────────────────────────────────────────────────────
        if decision == '1':
            info.narrativa('um_por_um_gustav.', arquivo)

            info.mensagem_morte('Vocês morrem queimados pelos monstros de fogo.')
            return True

        # OBSERVAR A SALA ───────────────────────────────────────────────────────────────────────────────────
        elif decision == '2':
            info.narrativa('observar_sala.', arquivo)

            decision = info.make_decision('Irrigadores_Pá_Copos')

            # IRRIGADORES ─ QUEBRADOS ───────────────────────────────────────────────────────────────────────
            if decision == '1':
                info.narrativa('irrigadores.', arquivo)

                info.mensagem_morte('Vocês morrem queimados pelos monstros de fogo.')
                return True

            # PÁ ─ INEFICIENTE ──────────────────────────────────────────────────────────────────────────────
            elif decision == '2':
                info.narrativa('pa', arquivo)

                info.mensagem_morte('Vocês morrem queimados pelos monstros de fogo.')
                return True

            # COPOS ─ FUNCIONA ─────────────────────────────────────────────────────────────────────────────
            else:
                info.narrativa('copos_gustav.', arquivo)

        # PEDIR AJUDA A GUSTAV ─────────────────────────────────────────────────────────────────────────────
        else:
            info.narrativa('pedir_ajuda_gustav.', arquivo)

        # CONTINUANDO CASO NÃO TENHA MORRIDO ───────────────────────────────────────────────────────────────
        info.narrativa('monstro_porta_gustav.', arquivo)

        decision = info.make_decision('Enfrentá-lo_Tentar passar por ele de fininho.')

        # ENFRENTÁ-LO ──────────────────────────────────────────────────────────────────────────────────────────
        if decision == '1':
            info.narrativa('enfrentar_monstro_porta_gustav.', arquivo)

        # TENTAR PASSAR POR ELE DE FININHO ─────────────────────────────────────────────────────────────────────
        else:
            info.narrativa('fininho_monstro_porta_gustav.', arquivo)

        # LUTA COM OGRO ────────────────────────────────────────────────────────────────────────────────────────
        luta = info.fight_archer('Ogro Guardião', 500, 20, 72, 2)

        if not luta[0]:
            info.death_count()
            return True

        if luta[2]:
            info.achieve('Sorte ou habilidade?')

        info.narrativa('ganhou_monstro_porta_gustav.', arquivo)

        info.modi_file('Doug: True\n', '.save', 5)
        info.achieve('O Cavalheiro')
        info.reset_atri()

        sleep(1)
        print('\n\033[33mDOUG ENTROU NA FESTA\033[m')
        sleep(2)

        info.narrativa('continuar_monstro_porta.', arquivo)

        sleep(1)
        print('\n\033[32mVocês sobem para o último andar, onde encontram Sir Guto, esperando por vocês\033[m')


    # CONTINUAR SEM GUSTAV ───────────────────────────────────────────────────────────────────────────────────
    else:
        info.narrativa('sala_estar.', arquivo)

        decision = info.make_decision('Lutar um por um_Observar a sala')

        # LUTAR UM POR UM ───────────────────────────────────────────────────────────────────────────────────
        if decision == '1':
            info.narrativa('um_por_um.', arquivo)

            info.mensagem_morte('Você morre queimad{a} pelos monstros de fogo.')
            return True

        # OBSERVAR A SALA ───────────────────────────────────────────────────────────────────────────────────
        else:
            info.narrativa('observar_sala.', arquivo)

            decision = info.make_decision('Irrigadores_Pá_Copos')

            # IRRIGADORES ─ QUEBRADOS ───────────────────────────────────────────────────────────────────────
            if decision == '1':
                info.narrativa('irrigadores.', arquivo)

                info.mensagem_morte('Você morre queimad{a} pelos monstros de fogo.')
                return True

            # PÁ ─ INEFICIENTE ──────────────────────────────────────────────────────────────────────────────
            elif decision == '2':
                info.narrativa('pa', arquivo)

                info.mensagem_morte('Você morre queimad{a} pelos monstros de fogo.')
                return True

            # COPOS ─ FUNCIONA ─────────────────────────────────────────────────────────────────────────────
            else:
                info.narrativa('copos.', arquivo)

        # CONTINUANDO CASO NÃO TENHA MORRIDO ───────────────────────────────────────────────────────────────────
        info.narrativa('monstro_porta.', arquivo)

        decision = info.make_decision('Enfrentá-lo_Tentar passar por ele de fininho.')

        # ENFRENTÁ-LO ──────────────────────────────────────────────────────────────────────────────────────────
        if decision == '1':
            info.narrativa('enfrentar_monstro_porta.', arquivo)

            luta = info.fight_archer('Ogro Guardião', 500, 46, 72, 0)

            if luta[0]:
                print('Como você fez isso?')
                return True

            # se já conhecia gustav
            if conhece_gustav:
                info.narrativa('gustav_perdeu_monstro_porta.', arquivo)

            # se não conhece gustav
            else:
                info.narrativa('perdeu_monstro_porta.', arquivo)

            info.modi_file('Gustav: True\n', '.save', 4)
            info.modi_file('Doug: True\n', '.save', 5)
            info.achieve('O Feiticeiro')
            info.achieve('O Cavalheiro')

            info.reset_atri()

            sleep(1)
            print('\n\033[33mGUSTAV & DOUG ENTRARAM NA FESTA\033[m')
            sleep(2)

            info.narrativa('continuar_monstro_porta.', arquivo)

            sleep(1)
            print('\n\033[32mVocês sobem para o último andar, onde encontram Sir Guto, esperando por vocês\033[m')

        # TENTAR PASSAR POR ELE DE FININHO ─────────────────────────────────────────────────────────────────────
        else:
            info.narrativa('passar_fininho_monstro_porta.', arquivo)

            info.mensagem_morte('Você é derrotad{a} pelo poder extremo de Sir Guto')
            return True

    info.show_achieve()

    sleep(1)
    print('\n\033[37mSalvando progresso... Não interrompa o programa.\033[m')
    sleep(2)

    info.modi_file('ato 3.\n', '.save', 0)
    info.save_atri()

    with open('.save') as save:
        save = save.read()

        for k in info.itens:
            if k not in info.inventario and k in save:
                info.delet_item_inve(k)

    return False


# ATO 1
def game_archer_ato1(arquivo):
    info.modi_file('caminho:\n', '.save', 1)

    info.modi_file('Inventario: False\n', '.save', 2)
    info.modi_file('Itens: \n', '.save', 3)

    info.modi_file('Gustav: False\n', '.save', 4)
    info.modi_file('Doug: False\n', '.save', 5)

    # ATO 1 ────────────────────────────────────────────────────────────────────────────
    sleep(1)
    print(f'\n\033[31m{" ATO 1":─>40}\033[m')

    info.narrativa('ato_1.', arquivo)

    decision = info.make_decision('Lutar_Entregar tudo_Fugir')

    # ENTREGAR TUDO ────────────────────────────────────────────────────────────────────
    if decision == '2':
        info.narrativa('entregar_tudo.',  arquivo)

        info.attributes['Ataque'] = 0
        info.attributes['Defesa'] = 0

        info.narrativa('continuar_floresta_sem_defesa.', arquivo)

        info.mensagem_morte('Você é derrotad{a} pelo monstro cogumelo.')
        return True

    # LUTAR ────────────────────────────────────────────────────────────────────────────
    elif decision == '1':
        info.narrativa('nao_entregar.', arquivo)

        luta = info.fight_archer('Forasteiro', 200, 15, 15, 2)

        if not luta:
            info.death_count()
            return True

        info.narrativa('ganhou_nao_entregar.', arquivo)

        sleep(1)
        print('\n\033[33mSEU DEFESA AUMENTA\033[m')
        sleep(2)

        info.attributes['Defesa'] += 25

    # FUGIR ─────────────────────────────────────────────────────────────────────────────
    else:
        info.narrativa('fugir.', arquivo)

    # CONTINUANDO ───────────────────────────────────────────────────────────────────────
    info.narrativa('continuar_floresta.', arquivo)

    luta = info.fight_archer('Monstro Cogumelo', 150, 12, 8, 4)

    if not luta:
        info.death_count()
        return True

    info.narrativa('ganhou_monstro_cogumelo.', arquivo)

    decision = info.make_decision('Pegar_Não pegar')

    # PEGAR COGUMELO ────────────────────────────────────────────────────────────────────
    if decision == '1':
        info.narrativa('pegar_cogumelo.', arquivo)
        info.modi_file('Inventario: True\n', '.save', 2)

        info.achieve('Um peso a mais')
        info.add_inve('Cogumelo Vermelho')

        sleep(1)
        print('\033[33mVOCÊ DESBLOQUEOU INVENTÁRIO\033[m')
        sleep(2)
        print('\033[32mInventário vai estar disponível nos momentos de escolha de agora em diante.\033[m')

    # NÃO PEGAR COGUMELO ────────────────────────────────────────────────────────────────
    else:
        info.narrativa('nao_pegar_cogumelo.', arquivo)

    # CONTINUANDO # 2 ───────────────────────────────────────────────────────────────────
    info.narrativa('torre.', arquivo)

    decision = info.make_decision('Entrar antes do cavalheiro para conseguir o item primeiro_'
                                  'Entrar depois do cavalheiro para ter certeza que é seguro')

    # ENTRAR ANTES DO CAVALHEIRO PARA CONSEGUIR O ITEM PRIMEIRO ──────────────────────────
    if decision == '1':
        info.narrativa('entrar_antes_torre.', arquivo)
        info.modi_file(' ato1_antes_doug,', '.save', 1, 'a')

    # ENTRAR DEPOIS DO CAVALHEIRO PARA TER CERTEZA QUE É SEGURO ──────────────────────────
    else:
        info.narrativa('entrar_depois_torre.', arquivo)
        info.modi_file(' ato1_depois_doug,', '.save', 1, 'a')

    info.achieve('O que esperar?')
    sleep(1)
    print('\n\033[32mVocê conseguiu entrar na Torre com sucesso.')

    info.show_achieve()

    sleep(1)
    print('\n\033[37mSalvando progresso... Não interrompa o programa.\033[m')
    sleep(2)

    info.modi_file('ato 2.\n', '.save', 0)
    info.save_atri()
    info.add_inve('Cogumelo Vermelho', 'm')

    return False


# INTRO
def game_archer_intro(arquivo):
    info.achieve('Mira certeira')

    info.modi_file('intro.\n', '.save', 0)
    info.modi_file('caminho:\n', '.save', 1)

    info.modi_file('Inventario: False\n', '.save', 2)
    info.modi_file('Itens: \n', '.save', 3)

    info.modi_file('Gustav: False\n', '.save', 4)
    info.modi_file('Doug: False\n', '.save', 5)

    # INTRODUÇÃO ────────────────────────────────────────────────────────────────────────────────────
    info.narrativa('intro.', arquivo)

    decision = info.make_decision('Roubar os nobres_Ir atrás do item mágico')

    # ROUBAR OS NOBRES ──────────────────────────────────────────────────────────────────────────────
    if decision == '1':
        info.narrativa('roubar_intro.', arquivo)

        info.mensagem_morte('Você passa o resto da sua vida nas masmorras.')
        return True

    # IR ATRÁS DO ITEM MÁGICO ────────────────────────────────────────────────────────────────────────
    else:
        info.narrativa('ir_embora_intro.', arquivo)

    info.show_achieve()

    sleep(1)
    print('\n\033[37mSalvando progresso... Não interrompa o programa.\033[m')
    sleep(2)

    info.modi_file('ato 1.\n', '.save', 0)

    return False


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
        info.narrativa('bemvindo.', '.help')

    info.ver_save()
    info.velo_narrativa()
    arquivo = info.caract()

    perdeu = False
    while True:
        # PERDEU = FALSE
        if not perdeu:
            print('\n\033[37mDefinindo atributos...')
            sleep(1)
            print('Costurando linhas do tempo...')
            sleep(1)
            print('Carregando...\033[m')
            sleep(2)

            perdeu = rodar_funcao(arquivo)

        # CASO O JOGADOR TENHA PERDIDO ─ PERDEU = TRUE
        elif perdeu:
            while True:
                sleep(1)
                info.show_achieve()
                sleep(1)
                try_again = input('Quer tentar de novo? [S/N] ').upper().strip()

                if not info.verifica_resposta(try_again, 'SN'):
                    continue  # esse continue vai para o começo do loop em q está
                else:
                    break

            # CASO O JOGADOR QUEIRA TENTAR NOVAMENTE
            if try_again == 'S':
                while True:
                    sleep(1)
                    pt = input('Deseja mudar suas características? (Ex.: Classe) [S/N] ').upper().strip()
                    if not info.verifica_resposta(pt, 'SN'):
                        continue  # esse continue vai para o começo do loop em q está
                    else:
                        break

                # CASO O JOGADOR QUEIRA MUDAR DE NOME E/OU CLASSE
                if pt == 'S':
                    info.apagar_save('.info')
                    info.ver_save()

                    arquivo = info.caract()
                    continue  # esse continue vai para o começo do loop principal (o game-loop)

                # CASO O JOGADOR > NÃO < QUEIRA TROCAR DE NOME E/OU CLASSE MAS QUEIRA JOGAR NOVAMENTE
                else:
                    info.ver_save()
                    continue  # esse continue vai para o começo do loop principal (o game-loop)

            # CASO O JOGADOR > NÃO < QUEIRA JOGAR NOVAMENTE
            else:
                sleep(1)
                print('\033[32mObrigado por jogar!\033[m')
                break

        # CASO PERDEU SEJA NONE
        else:
            sleep(1)
            raise ValueError('PROGRAMA SAIU INEXPERADAMENTE DA ROTA')


if __name__ == '__main__':
    main()
