from time import sleep
from os import path
import random

doug_atri = {'Nome': 'Doug', 'Vida': 50, 'Ataque': 35, 'Defesa': 110, 'Escudo': 55, 'Han': 60, 'Energia': 30, 'Critico': 10}
noelle_atri = {'Nome': 'Noelle', 'Vida': 75, 'Ataque': 35, 'Defesa': 15, 'Flecha': 5, 'Energia': 30, 'Critico': 20}
gustav_atri = {'Nome': 'Gustav', 'Vida': 50, 'Ataque': 5, 'Defesa': 10, 'Magia': 35, 'Energia': 210, 'Critico': 15}

tempo = 20
deaths = 0
perso_info = {}
attributes = {}

#  ▄█     █▄   ▄█      ███      ▄████████    ▄█    █▄       ▄████████    ▄████████
# ███     ███ ███  ▀█████████▄ ███    ███   ███    ███     ███    ███   ███    ███
# ███     ███ ███▌    ▀███▀▀██ ███    █▀    ███    ███     ███    █▀    ███    ███
# ███     ███ ███▌     ███   ▀ ███         ▄███▄▄▄▄███▄▄  ▄███▄▄▄      ▄███▄▄▄▄██▀
# ███     ███ ███▌     ███     ███        ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀
# ███     ███ ███      ███     ███    █▄    ███    ███     ███    █▄  ▀███████████
# ███ ▄█▄ ███ ███      ███     ███    ███   ███    ███     ███    ███   ███    ███
#  ▀███▀███▀  █▀      ▄████▀   ████████▀    ███    █▀      ██████████   ███    ███
# FUNÇÕES DE ATAQUE

# SE ALIADO ESTIVER DESMAIADO ─
def aliado_desmaiado(bool_vida, nome_aliado, ms_aliado, characters_list):
    if not bool_vida:
        print(f'\033[33m{nome_aliado} recuperou suas forças!\033[m')
        bool_vida = True
        ms_aliado -= 1

        characters_list.append(nome_aliado)

    return bool_vida, ms_aliado, characters_list


# CURAR ALIADO ─
def curar_aliado_execucao(nome_aliado, aliado_atri, aliado_atri_backup):
    # SE ESTIVER COM A VIDA DIFERENTE DO MÁXIMO ───────────────────────────────────────
    if aliado_atri['Vida'] != aliado_atri_backup['Vida']:
        cura = random.choice((25, 26, 27, 28, 29, 30))

        aliado_atri['Energia'] = aliado_atri_backup['Energia']

        if (aliado_atri['Vida'] + cura) > aliado_atri_backup['Vida']:
            cura = (aliado_atri_backup['Vida'] - aliado_atri['Vida'])
            aliado_atri['Vida'] += cura

        else:
            aliado_atri['Vida'] += cura

        sleep(1)
        print(f'\033[32mVocê curou \033[31m{cura}\033[32m da \033[31mVida\033[32m de {nome_aliado}!\033[m')

    # CASO NÃO TENHA PRECISADO DE CURA ─────────────────────────────────────────────────
    else:
        sleep(1)
        print(f'\033[32mFelizmente, {nome_aliado} não precisou de cura.\033[m')

    return aliado_atri


# CURAR A SI MESMO ─
def recuperar_si_mesmo(attributes_a_modificar):
    if attributes_a_modificar['Vida'] != 50:
        cura = random.choice((25, 26, 27, 28, 29, 30))

        attributes_a_modificar['Energia'] = 210

        if (attributes_a_modificar['Vida'] + cura) > 50:
            cura = (50 - attributes_a_modificar['Vida'])
            attributes_a_modificar['Vida'] += cura

        else:
            attributes_a_modificar['Vida'] += cura

        sleep(1)
        print(f'\033[32mVocê recuperou \033[31m{cura}\033[32m de vida!\033[32m')

    else:
        sleep(1)
        print('\033[32mFelizemente, você não precisou se recuperar.\033[m')

    return attributes_a_modificar


# ────────────────────────────────────────────────────────────────────────────────────────────────────────────
# FUNÇÃO DE LUTA ─────────────────────────────────────────────────────────────────────────────────────────────
# ────────────────────────────────────────────────────────────────────────────────────────────────────────────
def fight_witch(nome_monstro, vida_monstro, ataque_monstro, defesa_monstro, accuracy_rate):
    global attributes, doug_atri, noelle_atri
    doug_atri_backup = doug_atri.copy()
    noelle_atri_backup = noelle_atri.copy()
    doug_life = noelle_life = ms_noelle = ms_doug = dano_noelle = None

    # VERIFICANDO SE ACCURACY RATE ESTÁ NO LIMITE ────────────────────────────────────────────────────────────
    if 0 > accuracy_rate > 10:
        return None

    # DEFININDO ACCURACY ─────────────────────────────────────────────────────────────────────────────────────
    chance, hit_chance = verifica_accuracy(accuracy_rate)

    # DEFININDO CARACTERISTICAS DE LUTA ─────────────────────────────────────────────────────────────────────
    characters = [f'{perso_info["Nome"]}']

    # VERIFICANDO INFORMAÇÕES DO ARQUIVO ─────────────────────────────────────────────────────────────────────
    with open('.save') as save:
        inform = save.read()
        if 'Doug: True' in inform:
            doug = True
            characters.append('Doug')
            dano_han_doug = round(doug_atri['Han'] * (100 / (100 + defesa_monstro)))
            dano_espada_doug = round(doug_atri['Ataque'] * (100 / (100 + defesa_monstro)))
            dano_escudo_doug = round(doug_atri['Escudo'] * (100 / (100 + defesa_monstro)))
        else:
            doug = False

        if 'Noelle: True' in inform:
            noelle = True
            characters.append('Noelle')
            dano_noelle = round(noelle_atri['Ataque'] * (100 / (100 + defesa_monstro)))
        else:
            noelle = False

    vida_monstro_backup = vida_monstro

    dano_monstro = round(ataque_monstro * (100 / (100 + attributes['Defesa'])))

    dano_magico = round(attributes['Magia'] * (100 / (100 + defesa_monstro)))
    dano_fisico = round(attributes['Ataque'] * (100 / (100 + defesa_monstro)))

    # FRASES DO PERSONAGEM ───────────────────────────────────────────────────────────────────────────────────
    frases_ataque = (
        f'\033[32mVocê ataca o {nome_monstro} com magia.\033[m',
        '\033[32mVocê queima o monstro com fogo mágico.\033[m',
        f'\033[32mVocê ativa seus poderes elétricos no {nome_monstro}.\033[m',
        '\033[32mVocê joga o monstro no ar, fazendo ele cair com força no chão.\033[m',
        f'\033[32mVocê invoca búfalos fantasma que atropelam o {nome_monstro}\033[m'
        )

    # SISTEMA DE LUTA ─────────────────────────────────────────────────────────────────────────────────────────
    while True:
        shield = False
        doug_shield = False
        special_shield = False
        camuflade = False

        if doug:
            doug_life = True
            ms_doug = 0

        if noelle:
            noelle_life = True
            ms_noelle = 0

        amount_ea = 1
        amount_ea_doug = 1
        amount_ea_noelle = 1

        rodada = 1
        rodada_shield = 0
        ataque_anterior = ['']

        # ─────────────────────────────────────────────────────────────────────────────────────────────────────
        # GAME LOOP ───────────────────────────────────────────────────────────────────────────────────────────
        # ─────────────────────────────────────────────────────────────────────────────────────────────────────
        while True:
            # SE O MONSTRO MORRER ─────────────────────────────────────────────────────────────────────────────
            if vida_monstro <= 0:
                sleep(1)
                if doug or noelle:
                    print('\033[33mVocês ganharam!\033[m')
                    return True, noelle, doug
                else:
                    print('\033[33mVocê ganhou!\033[m')
                    return True

            # SE O JOGADOR DESMAIAR ───────────────────────────────────────────────────────────────────────────
            if attributes['Vida'] <= 0:
                sleep(1)
                print('\033[31mSUA VIDA CHEGOU A \033[33M0\033[m')

                if doug or noelle:
                    sleep(1)
                    print('\033[32mO grupo não pode continuar sem você.\033[m')

                break

            # SE NOELLE DESMAIAR ──────────────────────────────────────────────────────────────────────────────
            if noelle:
                if noelle_atri['Vida'] <= 0 and ms_noelle == 0:
                    mensagem_aliado_derrotado('Noelle')
                    characters.remove('Noelle')
                    noelle_life = False
                    ms_noelle += 1

            # SE DOUG DESMAIAR ────────────────────────────────────────────────────────────────────────────────
            if doug:
                if doug_atri['Vida'] <= 0 and ms_doug == 0:
                    mensagem_aliado_derrotado('Doug')
                    characters.remove('Doug')
                    doug_life = False
                    ms_doug += 1

            # IMPRIMIR NOME DO MONSTRO E VIDA ────────────────────────────────────────────────────────────────
            sleep(1)
            print(f'\n\033[31m{nome_monstro}\033[m: [\033[33m{vida_monstro} HP\033[m]')
            print('=' * 40)

            # MODIFICAR RODADA ───────────────────────────────────────────────────────────────────────────────
            rodada = modificar_rodada(rodada, noelle, doug)

            # CASO ENERGIA AINDA ESTEJA TRANSBORDANDO ────────────────────────────────────────────────────────
            if special_shield:
                special_shield = False
                sleep(1)
                print('\033[31mSua proteção se desfez.\033[m\n')

            # CASO SEJA A VEZ DO FEITICEIRO ──────────────────────────────────────────────────────────────────
            if rodada == 1:
                print('\033[32mÉ a sua vez!\033[m')

                imprimir_amount_ea(amount_ea)

                # OPÇÕES DE AÇÃO ────────────────────────────────────────────────────────────────────────────
                frase_ataque_especial = 'Se curar'
                if doug or noelle:
                    frase_ataque_especial = 'Curar companheiros'

                decision = make_decision(f'Atacar com magia (-8 E)_Defender (-6 E)_Atacar com cajado (-2 E)_{frase_ataque_especial} \033[35m(-AE)')

                # SE USAR MAGIA ──────────────────────────────────────────────────────────────────
                if decision == '1':
                    not_enough_energy = if_not_enough_energy(8)
                    if not_enough_energy:
                        continue

                    ataque_anterior = modifi_ataque_anterior_list(decision, ataque_anterior)

                    possib = random.choice(chance)
                    frase_sn = random.choice(frases_ataque)

                    if possib != 5:
                        attributes['Energia'] -= 8
                        amount_ea += ganhar_bonus_ea(amount_ea, (8, 9, 10, 11, 12))

                        sleep(1)
                        print(frase_sn)
                        if possib == 1 or possib == 2 or possib == 3:
                            sleep(1)
                            print('\033[32mDano crítico!\033[m')
                            vida_monstro -= (dano_magico + attributes['Critico'])
                        else:
                            vida_monstro -= dano_magico

                    else:
                        print('\n\033[31mVocê errou!\033[m')

                # SE ATIVAR ESCUDO ───────────────────────────────────────────────────────────
                elif decision == '2':
                    not_enough_energy = if_not_enough_energy(6)
                    if not_enough_energy:
                        continue

                    elif shield or special_shield:
                        sleep(1)
                        print('\n\033[31mO escudo ainda está ativo! Espere uma rodada.\033[m')
                        continue

                    ataque_anterior = modifi_ataque_anterior_list(decision, ataque_anterior)

                    if ataque_anterior[0] == '2':
                        sleep(1)
                        print('\n\033[31mVocê não pode executar essa ação duas vezes seguidas!')
                        sleep(1)
                        print('\033[32mEspere mais uma rodada.\033[m')
                        continue

                    attributes['Energia'] -= 6
                    shield = True

                    amount_ea += ganhar_bonus_ea(amount_ea, (6, 7, 8, 9, 10))

                    if doug or noelle:
                        sleep(1)
                        print('\033[32mVocê cria um escudo protetor para você e seus companheiros.')
                        sleep(1)
                        print('\033[32mVocês estão protegidos por duas rodadas.\033[m')
                    else:
                        sleep(1)
                        print('\033[32mVocê cria um escudo protetor para você.')
                        sleep(1)
                        print('\033[32mVocê está protegido por duas rodadas.\033[m')

                # SE ATACAR COM CAJADO ───────────────────────────────────────────────────────────
                elif decision == '3':
                    not_enough_energy = if_not_enough_energy(2)
                    if not_enough_energy:
                        continue

                    possib = random.choice(chance)

                    ataque_anterior = modifi_ataque_anterior_list(decision, ataque_anterior)

                    if possib % 2 == 0:

                        amount_ea += ganhar_bonus_ea(amount_ea, (1, 2, 3, 4))
                        attributes['Energia'] -= 2

                        sleep(1)
                        print('\033[32mVocê ataca com seu cajado, mas não parece fazer muita diferença.\033[m')
                        if possib == 1:
                            sleep(1)
                            print('\033[32mDano crítico!\033[m')
                            vida_monstro -= (dano_fisico + attributes['Critico'])
                        else:
                            vida_monstro -= dano_fisico

                    else:
                        print('\n\033[31mVocê errou!\033[m')

                # SE CURAR COMPANHEIROS COM MAGIA ───────────────────────────────────────────────────────────────
                else:
                    if amount_ea != 36:
                        sleep(1)
                        print('\n\033[31mVocê ainda não armazenou magia o suficiente!\033[m')
                        sleep(1)
                        print('\033[32mEncha seu \033[36mAtaque Especial\033[32m para executar essa ação.\033[m')
                        continue

                    ataque_anterior = modifi_ataque_anterior_list(decision, ataque_anterior)
                    amount_ea -= 35

                    if doug:
                        doug_life, ms_doug, characters = aliado_desmaiado(doug_life, 'Doug', ms_doug, characters)
                        doug_atri = curar_aliado_execucao('Doug', doug_atri, doug_atri_backup)

                    if noelle:
                        noelle_life, ms_noelle, characters = aliado_desmaiado(noelle_life, 'Noelle', ms_noelle, characters)
                        noelle_atri = curar_aliado_execucao('Noelle', noelle_atri, noelle_atri_backup)

                    if not doug and not noelle:
                        attributes = recuperar_si_mesmo(attributes)

                    if shield:
                        shield = False

                    special_shield = True
                    sleep(2)
                    print('\n\033[32mSua magia transborda com o poder de cura.')
                    sleep(1)
                    print('O inimigo não pode te tocar com tanta energia vazando de você.')
                    sleep(1)
                    print('Você está protegido por uma rodada.\033[m')

            # PARA DESATIVAR ESCUDO CASO ESTEJA ATIVADO ─────────────────────────────────────────
            if shield:
                rodada_shield += 1
                if rodada_shield > 2:
                    shield = False
                    sleep(1)
                    print('\033[31mSeu escudo é desativado.\033[m')
                    rodada_shield = 0

            # CASO SEJA A VEZ DA NOELLE ────────────────────────────────────────────────────────────────
            if noelle:
                if rodada == 2 and noelle_life:
                    frases_ataque_noelle = (
                        f'\033[32mNoelle ataca o {nome_monstro} com golpes marciais.\033[m',
                        f'\033[32mNoelle derruba o {nome_monstro} com chutes\033[32m',
                        f'\033[32mNoelle prende o {nome_monstro} com um mata-leão.'
                    )

                    frases_flecha_noelle = (
                        f'\033[32mNoelle lança flechas explosivas no {nome_monstro}.\033[m',
                        f'\033[32mFlechas ardentes acertam o {nome_monstro}\033[m',
                        f'\033[32mNoelle perfura o {nome_monstro} com flechas.\033[m'
                    )

                    sleep(1)
                    print('\033[32mÉ a vez de Noelle!\033[m')

                    movimento_noelle = random.choice(chance)

                    if amount_ea_noelle == 36:
                        amount_ea_noelle -= 35

                        quant_flechas = random.choice((16, 18, 20, 22))
                        vida_monstro -= round((noelle_atri['Flecha'] * quant_flechas) * (100 / (100 + defesa_monstro)))

                        sleep(2)
                        print('\n\033[32mNoelle junta toda sua fúria e acerta o adversário com a maior quantidade de flechas que consegue.')
                        sleep(1)
                        print(f'Noelle acertou {quant_flechas} flechas!')

                    elif (movimento_noelle == 2 or movimento_noelle == 10) and not camuflade:
                        amount_ea_noelle += ganhar_bonus_ea(amount_ea_noelle, (3, 4, 5))

                        camuflade = True
                        sleep(1)
                        print('\n\033[32mNoelle se esconde no cenário, se camuflando dos olhos do aversário.')

                    elif (movimento_noelle == 1 or movimento_noelle == 3 or movimento_noelle == 5 or movimento_noelle == 9) and not camuflade:

                        possib = random.choice(chance)
                        frase_nll_atck = random.choice(frases_ataque_noelle)

                        if possib != 1 or possib != 9:
                            amount_ea_noelle += ganhar_bonus_ea(amount_ea_noelle, (6, 7, 8, 9, 10))

                            sleep(1)
                            print('')
                            print(frase_nll_atck)
                            if possib == 5:
                                sleep(1)
                                print('\033[32mDano crítico!\033[m')
                                vida_monstro -= (dano_noelle + noelle_atri['Critico'])
                            else:
                                vida_monstro -= dano_noelle

                        else:
                            print(f'\n\033[31mNoelle tenta atacar {nome_monstro}, porén erra!\033[m')

                    else:
                        possib = random.choice(chance)
                        frase_nll_flc = random.choice(frases_flecha_noelle)

                        if possib != 7:
                            amount_ea_noelle += ganhar_bonus_ea(amount_ea_noelle, (8, 9, 10, 11, 12))
                            quant_flechas = random.choice((2, 3, 4, 5, 6))

                            sleep(1)
                            print('')
                            print(frase_nll_flc)
                            if possib == 10 or possib == 9 or possib == 3:
                                sleep(1)
                                print(f'\033[32mDano crítico!\033[m')
                                quant_flechas += random.choice((2, 3, 4))
                                vida_monstro -= round((noelle_atri['Flecha'] * quant_flechas) * (100 / (100 + defesa_monstro)))
                            else:
                                vida_monstro -= round((noelle_atri['Flecha'] * quant_flechas) * (100 / (100 + defesa_monstro)))

                        else:
                            print('\n\033[31mNoelle tenta atacar o monstro, porém erra!\033[m')

                # CASO NOELLE TENHA DESMAIADO ─────────────────────────────────────────────────────
                elif rodada == 2 and not noelle_life:
                    sleep(1)
                    print('\033[31mNoelle não consegue atacar mais. Ela passa a rodada.')
                    rodada += 1

            # CASO SEJA A VEZ DE DOUG ────────────────────────────────────────────────────────
            if doug:
                if rodada == 3 and doug_life:
                    frases_espada_doug = (
                        '\033[32mDoug pula e corta o monstro por cima com sua espada.\033[m',
                        f'\033[32mDoug acerta o {nome_monstro} consecutivamente com a espada.\033[m',
                        '\033[32mDoug puxa uma segunda espada e corta a criatura em um X.\033[m'
                    )

                    frases_escudo_doug = (
                        f'\033[32mDoug joga o escudo no {nome_monstro}, que volta como um boomerang.\033[m',
                        '\033[32mDoug avança no monstro e o acerta com força com o escudo.\033[m',
                        '\033[32mDoug empurra o monstro com força com seu escudo\033[m.'
                    )

                    frases_han_doug = (
                        '\033[32mHan acerta o monstro com um coice\033[m',
                        '\033[32mHan pula em cima do monstro várias vezes seguidas.\033[m',
                        f'\033[32mHan ataca o {nome_monstro} com mordidas.\033[m'
                    )

                    sleep(1)
                    print('\033[32mÉ a vez de Doug!\033[m')

                    movimento_doug = random.choice(chance)

                    if amount_ea_doug == 36:
                        possib = random.choice(chance)
                        frase_dg_han = random.choice(frases_han_doug)

                        amount_ea_doug -= 35

                        sleep(1)
                        print('')
                        print(frase_dg_han)
                        if possib == 6:
                            sleep(1)
                            print('\033[32mDano crítico!\033[m')
                            vida_monstro -= (dano_han_doug + doug_atri['Critico'])
                        else:
                            vida_monstro -= dano_han_doug

                    elif (movimento_doug == 1 or movimento_doug == 3 or movimento_doug == 7) and not doug_shield:
                        doug_shield = True

                        amount_ea_doug += ganhar_bonus_ea(amount_ea_doug, (2, 3, 4, 5, 6))

                        sleep(1)
                        print('\033[32mDoug levanta seu escudo.')

                    elif movimento_doug == 2 or movimento_doug == 5:
                        possib = random.choice(chance)
                        frase_dg_escudo = random.choice(frases_escudo_doug)

                        if possib % 2 == 1:
                            amount_ea_doug += ganhar_bonus_ea(amount_ea_doug, (8, 9, 10, 11, 12))

                            sleep(1)
                            print('')
                            print(frase_dg_escudo)
                            if possib == 3 or possib == 5:
                                sleep(1)
                                print('\033[32mDano crítico!\033[m')
                                vida_monstro -= (dano_escudo_doug + doug_atri['Critico'])
                            else:
                                vida_monstro -= dano_escudo_doug

                        else:
                            print(f'\n\033[31mDoug tenta atacar {nome_monstro}, mas erra!\033[m')

                    else:
                        possib = random.choice(chance)
                        frase_dg_espada = random.choice(frases_espada_doug)

                        if possib != 9:
                            amount_ea_doug += ganhar_bonus_ea(amount_ea_doug, (6, 7, 8, 9, 10))

                            sleep(1)
                            print('')
                            print(frase_dg_espada)
                            if possib == 7 or possib == 8 or possib == 10:
                                sleep(1)
                                print('\033[32mDano crítico!\033[m')
                                vida_monstro -= (dano_espada_doug + doug_atri['Critico'])
                            else:
                                vida_monstro -= dano_espada_doug

                        else:
                            print(f'\n\033[31mDoug tenta atacar {nome_monstro}, mas erra!\033[m')

                # CASO DOUG TENHA DESMAIADO ───────────────────────────────────────────────────────
                elif rodada == 3 and not doug_life:
                    sleep(1)
                    print('\033[31mDoug não consegue atacar mais. Ele passa a rodada.')
                    rodada += 1
                    continue

            sleep(1)
            print('')

            # PARA MONSTRO ATACAR ──────────────────────────────────────────────────────────────
            if vida_monstro > 0:
                possib = random.choice(chance)
                atacar = random.choice(characters)

                if atacar == perso_info['Nome']:
                    atacar = 'você'

                if possib not in hit_chance:
                    sleep(1)
                    print(f'\033[32m{nome_monstro} tenta atacar {atacar}, mas erra.\033[m')

                else:
                    if atacar == 'Noelle':
                        if camuflade:
                            chance_de_dano = random.choice((True, True, True, False, True))

                            if chance_de_dano:
                                sleep(1)
                                print(f'\033[32m{nome_monstro} tenta atacar Noelle, mas erra.\033[m')
                                rodada += 1
                                continue

                            else:
                                sleep(1)
                                print('\033[31mA camuflagem de Noelle se desfez!\033[m')
                                camuflade = False

                    sleep(1)
                    print(f'\033[31m{nome_monstro} ataca {atacar}.\033[m')

                    if shield:
                        sleep(1)
                        if doug or noelle:
                            print('\033[32mMas o escudo protege vocês.\033[m')
                        else:
                            print('\033[32mMas o escudo te protege.\033[m')

                    if atacar == 'você':
                        if special_shield:
                            sleep(1)
                            print('\033[32mSua magia protege você.\033[m')

                        if not shield and not special_shield:
                            if dano_monstro > attributes['Vida']:
                                dano_monstro = attributes['Vida']

                            attributes['Vida'] -= dano_monstro
                            sleep(1)
                            print(f'\033[32mVocê perde {dano_monstro} de \033[31mVida\033[m')

                            amount_ea += ganhar_bonus_ea(amount_ea, (1, 2))

                    else:
                        if atacar == noelle_atri['Nome'] and not shield:
                            noelle_atri['Vida'] -= round(ataque_monstro * (100 / (100 + noelle_atri['Defesa'])))

                        elif atacar == doug_atri['Nome'] and not shield:
                            if doug_shield:
                                sleep(1)
                                print('\033[32mO escudo dele o protege.\033[m')
                                doug_shield = False
                                sleep(1)
                                print('\033[31mDoug deixa seu escudo cair.\033[m')
                            else:
                                doug_atri['Vida'] -= round(ataque_monstro * (100 / (100 + doug_atri['Defesa'])))

            rodada += 1

        while True:
            try_again = input('Você quer lutar novamente? [S/N] ').upper().strip()
            if try_again not in 'SN':
                sleep(1)
                print('Oh não... Tente novamente.')
            else:
                break

        if try_again == 'S':
            if noelle:
                noelle_atri = noelle_atri_backup.copy()
            if doug:
                doug_atri = doug_atri_backup.copy()

            reset_atri()
            vida_monstro = vida_monstro_backup
        else:
            return False


#    ▄█   ▄█▄ ███▄▄▄▄    ▄█     ▄██████▄     ▄█    █▄        ███
#   ███ ▄███▀ ███▀▀▀██▄ ███    ███    ███   ███    ███   ▀█████████▄
#   ███▐██▀   ███   ███ ███▌   ███    █▀    ███    ███      ▀███▀▀██
#  ▄█████▀    ███   ███ ███▌  ▄███         ▄███▄▄▄▄███▄▄     ███   ▀
# ▀▀█████▄    ███   ███ ███▌ ▀▀███ ████▄  ▀▀███▀▀▀▀███▀      ███
#   ███▐██▄   ███   ███ ███    ███    ███   ███    ███       ███
#   ███ ▀███▄ ███   ███ ███    ███    ███   ███    ███       ███
#   ███   ▀█▀  ▀█   █▀  █▀     ████████▀    ███    █▀       ▄████▀
#   ▀
def fight_knight(nome_monstro, vida_monstro, ataque_monstro, defesa_monstro, accuracy_rate):
    # DEFININDO VARIÁVEIS ───────────────────────────────────────────────────────────────────────────────────────
    global attributes, gustav_atri, noelle_atri
    gustav_atri_backup = gustav_atri.copy()
    noelle_atri_backup = noelle_atri.copy()
    gustav_life = noelle_life = ms_gustav = ms_noelle = dano_noelle = None

    # VERIFICANDO SE ACCURACY RATE ESTÁ NO LIMITE ───────────────────────────────────────────────────────────────
    if 0 > accuracy_rate > 10:
        return None

    # DEFININDO ACCURACY ────────────────────────────────────────────────────────────────────────────────────────
    chance, hit_chance = verifica_accuracy(accuracy_rate)

    # DEFININDO CARACTERÍSTICAS DE LUTA ──────────────────────────────────────────────────────────────────────
    characters = [f'{perso_info["Nome"]}']

    # VERIFICANDO INFORMAÇÕES DO JOGADOR ──────────────────────────────────────────────────────────────────────
    with open('.save') as save:
        inform = save.read()
        if 'Gustav: True' in inform:
            gustav = True
            characters.append('Gustav')
            dano_magico_gustav = round(gustav_atri['Magia'] * (100 / (100 + defesa_monstro)))
            dano_fisico_gustav = round(gustav_atri['Ataque'] * (100 / (100 + defesa_monstro)))
        else:
            gustav = False

        if 'Noelle: True' in inform:
            noelle = True
            characters.append('Noelle')
            dano_noelle = round(noelle_atri['Ataque'] * (100 / (100 + defesa_monstro)))
        else:
            noelle = False

    vida_monstro_backup = vida_monstro

    dano_monstro = round(ataque_monstro * (100 / (100 + attributes['Defesa'])))

    dano_han = round(attributes['Han'] * (100 / (100 + defesa_monstro)))
    dano_espada = round(attributes['Ataque'] * (100 / (100 + defesa_monstro)))
    dano_escudo = round(attributes['Escudo'] * (100 / (100 + defesa_monstro)))

    # FRASES DO PERSONAGEM ────────────────────────────────────────────────────────────────────────────────────
    frases_espada = (
        '\033[32mVocê pula e corta o monstro por cima com sua espada.\033[m',
        f'\033[32mVocê acerta o {nome_monstro} consecutivamente com a espada.\033[m',
        '\033[32mVocê puxa uma segunda espada e corta a criatura em um X.\033[m'
        )

    frases_escudo = (
        f'\033[32mVocê joga o escudo no {nome_monstro}, que volta como um boomerang.\033[m',
        '\033[32mVocê avança no monstro e o acerta com força com o escudo.\033[m',
        '\033[32mVocê empurra o monstro com força com seu escudo\033[m.'
        )

    frases_han = (
        '\033[32mHan acerta o monstro com um coice\033[m',
        '\033[32mHan pula em cima do monstro várias vezes seguidas.\033[m',
        f'\033[32mHan ataca o {nome_monstro} com mordidas.\033[m'
        )

    # SISTEMA DE LUTA ────────────────────────────────────────────────────────────────
    while True:
        shield = False
        camuflade = False
        gustav_shield = False
        special_shield_gustav = False

        if gustav:
            gustav_life = True
            ms_gustav = 0

        if noelle:
            noelle_life = True
            ms_noelle = 0

        amount_ea = 1
        amount_ea_gustav = 1
        amount_ea_noelle = 1

        rodada = 1
        rodada_shield = 0
        ataque_anterior = ['']

        # ────────────────────────────────────────────────────────────────────────────────────────────────────
        # GAME LOOP ──────────────────────────────────────────────────────────────────────────────────────────
        # ────────────────────────────────────────────────────────────────────────────────────────────────────
        while True:
            # SE O MONSTRO MORRER ────────────────────────────────────────────────────────
            if vida_monstro <= 0:
                sleep(1)
                if gustav or noelle:
                    print('\033[33mVocês ganharam!\033[m')
                    return True, noelle, gustav
                else:
                    print('\033[33mVocê ganhou!\033[m')
                    return True

            # SE O JOGADOR DESMAIAR ──────────────────────────────────────────────────────
            if attributes['Vida'] <= 0:
                sleep(1)
                print('\033[31mSUA VIDA CHEGOU A \033[33M0\033[m')

                if gustav or noelle:
                    sleep(1)
                    print('\033[32mO grupo não pode continuar sem você.\033[m')

                break

            # SE NOELLE DESMAIAR ────────────────────────────────────────────────────────
            if noelle:
                if noelle_atri['Vida'] <= 0 and ms_noelle == 0:
                    sleep(1)
                    print('\033[31mA VIDA DE NOELLE CHEGOU A \033[33m0\033[m')
                    sleep(1)
                    print('\033[32mEla não atacará mais durante a luta.\033[m')

                    characters.remove('Noelle')
                    noelle = False
                    ms_noelle += 1

            # SE GUSTAV DESMAIAR ──────────────────────────────────────────────────────────
            if gustav:
                if gustav_atri['Vida'] <= 0 and ms_gustav == 0:
                    sleep(1)
                    print('\033[31mA VIDA DE GUSTAV CHEGOU A \033[33m0\033[m')
                    sleep(1)
                    print('\033[32mEle não atacará mais durante a luta.\033[m')

                    characters.remove('Gustav')
                    gustav = False
                    ms_gustav += 1

            # IMPRIMIR NOME DO MONSTRO E VIDA ───────────────────────────────────────────────
            sleep(1)
            print(f'\n\033[31m{nome_monstro}\033[m: [\033[33m{vida_monstro} HP\033[m]')
            print('=' * 40)

            # MODIFICAR RODADA ──────────────────────────────────────────────────────────────
            rodada = modificar_rodada(rodada, noelle, gustav)

            # CASO ENERGIA DE GUSTAV AINDA ESTEJA TRANSBORDANDO ────────────────────────────────────────────────────────
            if special_shield_gustav:
                special_shield_gustav = False
                sleep(1)
                print('\033[31mA proteção de Gustav se desfez.\033[m\n')

            # CASO SEJA A VEZ DO CAVALHEIRO ─────────────────────────────────────────────────
            if rodada == 1:
                print('\033[32mÉ a sua vez!\033[m\n')

                if shield is True:
                    sleep(1)
                    print('\033[32mSeu escudo não foi necessário.\033[m\n')
                    sleep(1)
                    shield = False

                imprimir_amount_ea(amount_ea)

                # OPÇÕES DE AÇÃO ────────────────────────────────────────────────────────────
                decision = make_decision('Atacar com espada (-1 E)_Defender (-0 E)_Atacar com escudo (-2 E)_Usar Han \033[35m(-AE)')

                # SE ATACAR COM ESPADA ──────────────────────────────────────────────────────────────────
                if decision == '1':
                    not_enough_energy = if_not_enough_energy(2)
                    if not_enough_energy:
                        continue

                    possib = random.choice(chance)
                    frase_sn = random.choice(frases_espada)
                    ataque_anterior = modifi_ataque_anterior_list(decision, ataque_anterior)

                    if possib != 9:
                        amount_ea += ganhar_bonus_ea(amount_ea, (6, 7, 8, 9, 10))

                        attributes['Energia'] -= 1

                        sleep(1)
                        print(frase_sn)
                        if possib == 7 or possib == 8 or possib == 10:
                            sleep(1)
                            print('\033[32mDano crítico!\033[m')
                            vida_monstro -= (dano_espada + attributes['Critico'])
                        else:
                            vida_monstro -= dano_espada

                    else:
                        print('\n\033[31mVocê errou!\033[m')

                # SE USAR ESCUDO PARA DEFESA ───────────────────────────────────────────────────────────
                elif decision == '2':
                    not_enough_energy = if_not_enough_energy(0)
                    if not_enough_energy:
                        continue

                    ataque_anterior = modifi_ataque_anterior_list(decision, ataque_anterior)

                    if ataque_anterior[0] == '2':
                        sleep(1)
                        print('\n\033[31mSeu escudo ainda está no chão!')
                        sleep(1)
                        print('\033[32mEspere mais uma rodada para executar essa ação.\033[m')
                        continue

                    shield = True

                    amount_ea += ganhar_bonus_ea(amount_ea, (2, 3, 4, 5, 6))

                    sleep(1)
                    print('\033[32mVocê levanta seu escudo.')
                    sleep(1)
                    print('\033[32mVocê será protegido de qualquer ataque contra você.\033[m')

                # SE ATACAR COM ESCUDO ───────────────────────────────────────────────────────────
                elif decision == '3':
                    not_enough_energy = if_not_enough_energy(2)
                    if not_enough_energy:
                        continue

                    possib = random.choice(chance)
                    frase_sn = random.choice(frases_escudo)
                    ataque_anterior = modifi_ataque_anterior_list(decision, ataque_anterior)

                    if possib % 2 == 1:
                        amount_ea += ganhar_bonus_ea(amount_ea, (8, 9, 10, 11, 12))
                        attributes['Energia'] -= 2

                        sleep(1)
                        print(frase_sn)
                        if possib == 3 or possib == 5:
                            sleep(1)
                            print('\033[32mDano crítico!\033[m')
                            vida_monstro -= (dano_escudo + attributes['Critico'])
                        else:
                            vida_monstro -= dano_escudo

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

                    possib = random.choice(chance)
                    frase_sn = random.choice(frases_han)
                    ataque_anterior = modifi_ataque_anterior_list(decision, ataque_anterior)

                    amount_ea -= 35

                    sleep(1)
                    print(frase_sn)
                    if possib == 6:
                        sleep(1)
                        print('\033[32mDano crítico!\033[m')
                        vida_monstro -= (dano_han + attributes['Critico'])
                    else:
                        vida_monstro -= dano_han

            # CASO SEJA A VEZ DA NOELLE ────────────────────────────────────────────────────────────────
            if noelle:
                if rodada == 2 and noelle_life:
                    frases_ataque_noelle = (
                        f'\033[32mNoelle ataca o {nome_monstro} com golpes marciais.\033[m',
                        f'\033[32mNoelle derruba o {nome_monstro} com chutes\033[32m',
                        f'\033[32mNoelle prende o {nome_monstro} com um mata-leão.'
                    )

                    frases_flecha_noelle = (
                        f'\033[32mNoelle lança flechas explosivas no {nome_monstro}.\033[m',
                        f'\033[32mFlechas ardentes acertam o {nome_monstro}\033[m',
                        f'\033[32mNoelle perfura o {nome_monstro} com flechas.\033[m'
                    )

                    sleep(1)
                    print('\033[32mÉ a vez de Noelle!\033[m')

                    movimento_noelle = random.choice(chance)

                    if amount_ea_noelle == 36:
                        amount_ea_noelle -= 35

                        quant_flechas = random.choice((16, 18, 20, 22))
                        vida_monstro -= round((noelle_atri['Flecha'] * quant_flechas) * (100 / (100 + defesa_monstro)))

                        sleep(2)
                        print(
                            '\n\033[32mNoelle junta toda sua fúria e acerta o adversário com a maior quantidade de flechas que consegue.')
                        sleep(1)
                        print(f'Noelle acertou {quant_flechas} flechas!')

                    elif (movimento_noelle == 2 or movimento_noelle == 10) and not camuflade:
                        amount_ea_noelle += ganhar_bonus_ea(amount_ea_noelle, (3, 4, 5))

                        camuflade = True
                        sleep(1)
                        print('\n\033[32mNoelle se esconde no cenário, se camuflando dos olhos do aversário.')

                    elif (movimento_noelle == 1 or movimento_noelle == 3 or movimento_noelle == 5 or movimento_noelle == 9) and not camuflade:

                        possib = random.choice(chance)
                        frase_nll_atck = random.choice(frases_ataque_noelle)

                        if possib != 1 or possib != 9:
                            amount_ea_noelle += ganhar_bonus_ea(amount_ea_noelle, (6, 7, 8, 9, 10))

                            sleep(1)
                            print('')
                            print(frase_nll_atck)
                            if possib == 5:
                                sleep(1)
                                print('\033[32mDano crítico!\033[m')
                                vida_monstro -= (dano_noelle + noelle_atri['Critico'])
                            else:
                                vida_monstro -= dano_noelle

                        else:
                            print(f'\n\033[31mNoelle tenta atacar {nome_monstro}, porén erra!\033[m')

                    else:
                        possib = random.choice(chance)
                        frase_nll_flc = random.choice(frases_flecha_noelle)

                        if possib != 7:
                            amount_ea_noelle += ganhar_bonus_ea(amount_ea_noelle, (8, 9, 10, 11, 12))
                            quant_flechas = random.choice((2, 3, 4, 5, 6))

                            sleep(1)
                            print('')
                            print(frase_nll_flc)
                            if possib == 10 or possib == 9 or possib == 3:
                                sleep(1)
                                print(f'\033[32mDano crítico!\033[m')
                                quant_flechas += random.choice((2, 3, 4))
                                vida_monstro -= round(
                                    (noelle_atri['Flecha'] * quant_flechas) * (100 / (100 + defesa_monstro)))
                            else:
                                vida_monstro -= round(
                                    (noelle_atri['Flecha'] * quant_flechas) * (100 / (100 + defesa_monstro)))

                        else:
                            print('\n\033[31mNoelle tenta atacar o monstro, porém erra!\033[m')

                # CASO NOELLE TENHA DESMAIADO ─────────────────────────────────────────────────────
                elif rodada == 2 and not noelle_life:
                    sleep(1)
                    print('\033[31mNoelle não consegue atacar mais. Ela passa a rodada.')
                    rodada += 1

            # CASO SEJA A VEZ DE GUSTAV ────────────────────────────────────────────────────────
            if gustav:
                if rodada == 3 and gustav_life:
                    frases_ataque_gustav = (
                        f'\033[32mGustav ataca o {nome_monstro} com magia.\033[m',
                        '\033[32mGustav queima o monstro com fogo mágico.\033[m',
                        f'\033[32mGustav ativa seus poderes elétricos no {nome_monstro}.\033[m',
                        '\033[32mGustav joga o monstro no ar, fazendo ele cair com força no chão.\033[m',
                        f'\033[32mGustav invoca búfalos fantasma que atropelam o {nome_monstro}\033[m'
                    )

                    sleep(1)
                    print('\033[32mÉ a vez de Gustav!\033[m')

                    movimento_gustav = random.choice(chance)

                    if amount_ea_gustav == 36:
                        amount_ea_gustav -= 35

                        recuperar = (50 - attributes['Vida'])
                        if not recuperar:
                            print('\033[32mFelizmente, você não precisou de cura.\033[m')
                        else:
                            attributes['Vida'] += recuperar
                            print(f'\033[32mGustav recuperou {recuperar} da sua \033[31mVida!\033[m')

                        if noelle:
                            recuperar = (75 - noelle_atri['Vida'])
                            if not recuperar:
                                print('\033[32mFelizmente, Noelle não precisou de cura.\033[m')
                            else:
                                noelle_atri['Vida'] += recuperar
                                print(f'\033[32mGustav recuperou {recuperar} da \033[31mVida\033[32m de Noelle!\033[m')

                        special_shield_gustav = True
                        sleep(2)
                        print('\n\033[32mA magia de Gustav transborda com o poder de cura.')
                        sleep(1)
                        print('O inimigo não pode tocá-lo com tanta energia vazando dele.')

                    elif movimento_gustav == 6:
                        possib = random.choice(chance)

                        if possib % 2 == 0:
                            amount_ea_gustav += ganhar_bonus_ea(amount_ea_gustav, (1, 2, 3, 4))

                            sleep(1)
                            print('')
                            print('\033[32mGustav ataca com seu cajado, mas não parece fazer muita diferença.\033[m')
                            if possib == 1:
                                sleep(1)
                                print('\033[32mDano crítico!\033[m')
                                vida_monstro -= (dano_fisico_gustav + gustav_atri['Critico'])
                            else:
                                vida_monstro -= dano_fisico_gustav

                        else:
                            print(f'\n\033[31mGustav tenta atacar {nome_monstro}, mas erra!\033[m')

                    elif (movimento_gustav == 1 or movimento_gustav == 3 or movimento_gustav == 5) and not gustav_shield:
                        gustav_shield = True

                        amount_ea_gustav += ganhar_bonus_ea(amount_ea_gustav, (6, 7, 8, 9, 10))

                        sleep(1)
                        print('\033[32mGustav cria um escudo protetor para vocês.')
                        sleep(1)
                        print('\033[32mVocês estão protegidos por duas rodadas.\033[m')

                    else:
                        possib = random.choice(chance)
                        frase_gv = random.choice(frases_ataque_gustav)

                        if possib != 5:
                            amount_ea_gustav += ganhar_bonus_ea(amount_ea_gustav, (8, 9, 10, 11, 12))

                            sleep(1)
                            print('')
                            print(frase_gv)
                            if possib == 1 or possib == 2 or possib == 3:
                                sleep(1)
                                print('\033[32mDano crítico!\033[m')
                                vida_monstro -= (dano_magico_gustav + gustav_atri['Critico'])
                            else:
                                vida_monstro -= dano_magico_gustav

                        else:
                            print(f'\n\033[31mGustav tenta atacar {nome_monstro}, mas erra!\033[m')

                # CASO GUSTAV TENHA DESMAIADO ───────────────────────────────────────────────────────
                elif rodada == 3 and not gustav_life:
                    sleep(1)
                    print('\033[31mGustav não consegue atacar mais. Ele passa a rodada.')
                    rodada += 1
                    continue

            # PARA DESATIVAR ESCUDO CASO ESTEJA ATIVADO ─────────────────────────────────────────
            if gustav_shield:
                rodada_shield += 1
                if rodada_shield > 2:
                    gustav_shield = False
                    sleep(1)
                    print('\033[31mO escudo de Gustav é desativado.\033[m')
                    rodada_shield = 0

            sleep(1)
            print('')

            # PARA MONSTRO ATACAR ──────────────────────────────────────────────────────────────
            if vida_monstro > 0:
                possib = random.choice(chance)
                atacar = random.choice(characters)

                if atacar == perso_info['Nome']:
                    atacar = 'você'

                if possib not in hit_chance:
                    sleep(1)
                    print(f'\033[32m{nome_monstro} tenta atacar {atacar}, mas erra.\033[m')

                else:
                    if atacar == 'Noelle':
                        if camuflade:
                            chance_de_dano = random.choice((True, True, True, False, True))

                            if chance_de_dano:
                                sleep(1)
                                print(f'\033[32m{nome_monstro} tenta atacar Noelle, mas erra.\033[m')
                                rodada += 1
                                continue

                            else:
                                sleep(1)
                                print('\033[31mA camuflagem de Noelle se desfez!\033[m')
                                camuflade = False

                    sleep(1)
                    print(f'\033[31m{nome_monstro} ataca {atacar}.\033[m')

                    if gustav_shield:
                        sleep(1)
                        print('\033[32mMas o escudo de Gustav protege vocês.\033[m')
                        rodada += 1
                        continue

                    if atacar == 'você':
                        if shield:
                            sleep(1)
                            print('\033[32mSeu escudo protege você.\033[m')
                            shield = False
                            sleep(1)
                            print('\033[31mVocê deixa seu escudo cair.\033[m')

                        else:
                            if dano_monstro > attributes['Vida']:
                                dano_monstro = attributes['Vida']

                            attributes['Vida'] -= dano_monstro
                            sleep(1)
                            print(f'\033[32mVocê perde {dano_monstro} de \033[31mVida\033[m')

                            amount_ea += ganhar_bonus_ea(amount_ea, (1, 2))

                    else:
                        if atacar == noelle_atri['Nome']:
                            noelle_atri['Vida'] -= round(ataque_monstro * (100 / (100 + noelle_atri['Defesa'])))

                        elif atacar == gustav_atri['Nome']:
                            if special_shield_gustav:
                                sleep(1)
                                print('\033[32mMas a magia de Gustav o protege\033[m')
                            else:
                                gustav_atri['Vida'] -= round(ataque_monstro * (100 / (100 + gustav_atri['Defesa'])))

            rodada += 1

        while True:
            try_again = input('Você quer lutar novamente? [S/N] ').upper().strip()
            if try_again not in 'SN':
                sleep(1)
                print('Oh não... Tente novamente.')
            else:
                break

        if try_again == 'S':
            if noelle:
                noelle_atri = noelle_atri_backup.copy()
            if gustav:
                gustav_atri = gustav_atri_backup.copy()

            reset_atri()
            vida_monstro = vida_monstro_backup
        else:
            return False


#    ▄████████    ▄████████  ▄████████    ▄█    █▄       ▄████████    ▄████████
#   ███    ███   ███    ███ ███    ███   ███    ███     ███    ███   ███    ███
#   ███    ███   ███    ███ ███    █▀    ███    ███     ███    █▀    ███    ███
#   ███    ███  ▄███▄▄▄▄██▀ ███         ▄███▄▄▄▄███▄▄  ▄███▄▄▄      ▄███▄▄▄▄██▀
# ▀███████████ ▀▀███▀▀▀▀▀   ███        ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀
#   ███    ███ ▀███████████ ███    █▄    ███    ███     ███    █▄  ▀███████████
#   ███    ███   ███    ███ ███    ███   ███    ███     ███    ███   ███    ███
#   ███    █▀    ███    ███ ████████▀    ███    █▀      ██████████   ███    ███
#                ███    ███                                          ███    ███
def fight_archer(nome_monstro, vida_monstro, ataque_monstro, defesa_monstro, accuracy_rate):
    # DEFININDO VARIÁVEIS ─────────────────────────────────────────────────────────────────────────────────────
    global attributes, doug_atri, gustav_atri
    doug_atri_backup = doug_atri.copy()
    gustav_atri_backup = gustav_atri.copy()
    doug_life = gustav_life = ms_doug = ms_gustav = None

    # VERIFICANDO SE ACCURACY RATE ESTÁ NO LIMITE ─────────────────────────────────────────────────────────────
    if 0 > accuracy_rate > 10:
        return None

    # DEFININDO ACCURACY ──────────────────────────────────────────────────────────────────────────────────────
    chance, hit_chance = verifica_accuracy(accuracy_rate)

    # DEFININDO CARACTERÍSTICAS DE LUTA ───────────────────────────────────────────────────────────────────────
    characters = [f'{perso_info["Nome"]}']

    # VERIFICANDO INFORMAÇÕES DO JOGADOR ───────────────────────────────────────────────────────────────────────
    with open('.save') as save:
        inform = save.read()
        if 'Doug: True' in inform:
            doug = True
            characters.append('Doug')
            dano_han_doug = round(doug_atri['Han'] * (100 / (100 + defesa_monstro)))
            dano_espada_doug = round(doug_atri['Ataque'] * (100 / (100 + defesa_monstro)))
            dano_escudo_doug = round(doug_atri['Escudo'] * (100 / (100 + defesa_monstro)))
        else:
            doug = False

        if 'Gustav: True' in inform:
            gustav = True
            characters.append('Gustav')
            dano_magico_gustav = round(gustav_atri['Magia'] * (100 / (100 + defesa_monstro)))
            dano_fisico_gustav = round(gustav_atri['Ataque'] * (100 / (100 + defesa_monstro)))
        else:
            gustav = False

    vida_monstro_backup = vida_monstro

    dano_monstro = round(ataque_monstro * (100 / (100 + attributes['Defesa'])))
    dano_fisico = round(attributes['Ataque'] * (100 / (100 + defesa_monstro)))

    # FRASES NOELLE ───────────────────────────────────────────────────────────────────────────────────────────
    frases_ataque = (
        f'\033[32mVocê ataca o {nome_monstro} com golpes marciais.\033[m',
        f'\033[32mVocê derruba o {nome_monstro} com chutes\033[32m',
        f'\033[32mVocê prende o {nome_monstro} com um mata-leão.'
    )

    frases_flecha = (
        f'\033[32mVocê lança flechas explosivas no {nome_monstro}.\033[m',
        f'\033[32mFlechas ardentes acertam o {nome_monstro}\033[m',
        f'\033[32mVocê perfura o {nome_monstro} com flechas.\033[m'
    )

    # SISTEMA DE LUTA ────────────────────────────────────────────────────────────────────────────────────────
    while True:
        camuflade = False
        doug_shield = False
        gustav_shield = False
        special_shield_gustav = False

        if doug:
            doug_life = True
            ms_doug = 0

        if gustav:
            gustav_life = True
            ms_gustav = 0

        amount_ea = 1
        amount_ea_doug = 1
        amount_ea_gustav = 1
        atacar_com_artes_marciais = 0

        rodada = 1
        rodada_shield = 0
        ataque_anterior = ['']

        # ─────────────────────────────────────────────────────────────────────────────────────────────────────
        # GAME LOOP ───────────────────────────────────────────────────────────────────────────────────────────
        # ─────────────────────────────────────────────────────────────────────────────────────────────────────
        while True:
            # SE O MONSTRO MORRER ─────────────────────────────────────────────────────────────────────────────
            if vida_monstro <= 0:
                sleep(1)
                if doug or gustav:
                    print('\033[33mVocês ganharam!\033[m')
                    return True, doug, gustav
                else:
                    print('\033[33mVocê ganhou!\033[m')
                    return True

            # SE O JOGADOR DESMAIAR ───────────────────────────────────────────────────────────────────────────
            if attributes['Vida'] <= 0:
                sleep(1)
                print('\n\033[31mSUA VIDA CHEGOU A \033[33M0\033[m')

                if doug or gustav:
                    sleep(1)
                    print('\033[32mO grupo não pode continuar sem você.\033[m')

                break

            # SE GUSTAV DESMAIAR ──────────────────────────────────────────────────────────────────────────────
            if gustav:
                if gustav_atri["Vida"] <= 0 and ms_gustav == 0:
                    sleep(1)
                    print('\033[31mA VIDA DE GUSTAV CHEGOU A \033[33m0\033[m')
                    sleep(1)
                    print('\033[32mEle não atacará mais durante a luta.\033[m')

                    characters.remove('Gustav')
                    gustav_life = False
                    ms_gustav += 1

            # SE DOUG DESMAIAR ────────────────────────────────────────────────────────────────────────────────
            if doug:
                if doug_atri["Vida"] <= 0 and ms_doug == 0:
                    sleep(1)
                    print('\033[31mA VIDA DE DOUG CHEGOU A \033[33m0\033[m')
                    sleep(1)
                    print('\033[32mEle não atacará mais durante a luta.\033[m')

                    characters.remove('Doug')
                    doug_life = False
                    ms_doug += 1

            # IMPRIMIR NOME DO MONSTRO E VIDA ─────────────────────────────────────────────────────────────────
            sleep(1)
            print(f'\n\033[31m{nome_monstro}\033[m: [\033[33m{vida_monstro} HP\033[m]')
            print('=' * 40)

            # MODIFICAR RODADA ────────────────────────────────────────────────────────────────────────────────
            rodada = modificar_rodada(rodada, doug, gustav)

            # CASO ENERGIA DE GUSTAV AINDA ESTEJA TRANSBORDANDO ────────────────────────────────────────────────────────
            if special_shield_gustav:
                special_shield_gustav = False
                sleep(1)
                print('\033[31mA proteção de Gustav se desfez.\033[m\n')

            # CASO SEJA A VEZ DO ARQUEIRO ─────────────────────────────────────────────────────────────────────
            if rodada == 1:
                print('\033[32mÉ a sua vez!\033[m')

                imprimir_amount_ea(amount_ea)

                # OPÇÕES DE AÇÃO ────────────────────────────────────────────────────────────────────────────
                decision = make_decision('Atirar flechas (-1 E)_Se camuflar (-3 E)_Atacar com artes marciais (-3 E)_Combo de flechas \033[35m(-AE)')

                # ATIRAR FLECHAS ────────────────────────────────────────────────────────────────────────────
                if decision == '1':
                    not_enough_energy = if_not_enough_energy(1)
                    if not_enough_energy:
                        continue

                    possib = random.choice(chance)
                    frase_sn = random.choice(frases_flecha)

                    ataque_anterior = modifi_ataque_anterior_list(decision, ataque_anterior)

                    if possib != 7:
                        amount_ea += ganhar_bonus_ea(amount_ea, (8, 9, 10, 11, 12))

                        attributes['Energia'] -= 1
                        quant_flechas = random.choice((2, 3, 4, 5, 6))

                        if possib == 10 or possib == 9 or possib == 3:
                            quant_flechas += random.choice((2, 3, 4))
                            vida_monstro -= round((attributes['Flecha'] * quant_flechas) * (100 / (100 + defesa_monstro)))
                            sleep(1)
                            print(frase_sn)
                            sleep(1)
                            print(f'\033[32mDano crítico!\033[m')
                        else:
                            vida_monstro -= round((attributes['Flecha'] * quant_flechas) * (100 / (100 + defesa_monstro)))
                            sleep(1)
                            print(frase_sn)

                    else:
                        print('\n\033[31mVocê errou!\033[m')

                # SE CAMUFLAR ────────────────────────────────────────────────────────────────────────
                elif decision == '2':
                    not_enough_energy = if_not_enough_energy(3)
                    if not_enough_energy:
                        continue

                    if camuflade:
                        sleep(1)
                        print('\n\033[31mVocê já está escondido!')
                        continue

                    ataque_anterior = modifi_ataque_anterior_list(decision, ataque_anterior)

                    if ataque_anterior[0] == '2':
                        sleep(1)
                        print('\n\033[31mVocê não pode executar essa ação duas vezes seguidas!')
                        sleep(1)
                        print('\033[32mEspere mais uma rodada.\033[m')
                        continue

                    amount_ea += ganhar_bonus_ea(amount_ea, (3, 4, 5))

                    sleep(1)
                    print('\n\033[32mVocê se esconde no cenário, se camuflando dos olhos do aversário.')
                    sleep(2)
                    print('Suas chances de levar dano diminuíram.\033[m')

                    camuflade = True


                # ATACAR COM ARTES MARCIAIS ──────────────────────────────────────────────────────────
                elif decision == '3':
                    not_enough_energy = if_not_enough_energy(3)
                    if not_enough_energy:
                        continue

                    if camuflade:
                        if not atacar_com_artes_marciais:
                            sleep(1)
                            print('\n\033[31mVocê está escondido! Atacar de perto vai desfazer sua camuflagem!')
                            sleep(2)
                            print('Se quiser mesmo assim usar esse ataque, tente novamente.\033[m')

                            atacar_com_artes_marciais += 1
                            continue

                        elif atacar_com_artes_marciais:
                            sleep(1)
                            print('\033[31mSua camuflagem se desfez!\033[m\n')

                            atacar_com_artes_marciais -= 1
                            camuflade = False

                    possib = random.choice(chance)
                    frase_sn = random.choice(frases_ataque)
                    ataque_anterior = modifi_ataque_anterior_list(decision, ataque_anterior)

                    if possib != 1 or possib != 9:
                        amount_ea += ganhar_bonus_ea(amount_ea, (6, 7, 8, 9, 10))
                        attributes['Energia'] -= 3

                        sleep(1)
                        print(frase_sn)
                        if possib == 5:
                            sleep(1)
                            print('\033[32mDano crítico!\033[m')
                            vida_monstro -= (dano_fisico + attributes['Critico'])
                        else:
                            vida_monstro -= dano_fisico

                    else:
                        print('\n\033[31mVocê errou!\033[m')

                # COMBO DE FLECHAS ──────────────────────────────────────────────────────────────────────────────
                else:
                    if amount_ea != 36:
                        sleep(1)
                        print('\n\033[31mVocê não armazenou fúria o suficiente!\033[m')
                        sleep(1)
                        print('\033[32mEncha seu \033[36mAtaque Especial\033[32m para executar essa ação.\033[m')
                        continue

                    ataque_anterior = modifi_ataque_anterior_list(decision, ataque_anterior)

                    amount_ea -= 35

                    quant_flechas = random.choice((16, 18, 20, 22))
                    vida_monstro -= round((attributes['Flecha'] * quant_flechas) * (100 / (100 + defesa_monstro)))

                    sleep(2)
                    print('\n\033[32mVocê junta toda sua fúria e acerta o adversário com a maior quantidade de flechas que consegue.')
                    sleep(1)
                    print(f'Você acertou {quant_flechas} flechas!')

            # CASO SEJA A VEZ DE DOUG ────────────────────────────────────────────────────────
            if doug:
                if rodada == 2 and doug_life:
                    frases_espada_doug = (
                        '\033[32mDoug pula e corta o monstro por cima com sua espada.\033[m',
                        f'\033[32mDoug acerta o {nome_monstro} consecutivamente com a espada.\033[m',
                        '\033[32mDoug puxa uma segunda espada e corta a criatura em um X.\033[m'
                    )

                    frases_escudo_doug = (
                        f'\033[32mDoug joga o escudo no {nome_monstro}, que volta como um boomerang.\033[m',
                        '\033[32mDoug avança no monstro e o acerta com força com o escudo.\033[m',
                        '\033[32mDoug empurra o monstro com força com seu escudo\033[m.'
                    )

                    frases_han_doug = (
                        '\033[32mHan acerta o monstro com um coice\033[m',
                        '\033[32mHan pula em cima do monstro várias vezes seguidas.\033[m',
                        f'\033[32mHan ataca o {nome_monstro} com mordidas.\033[m'
                    )

                    sleep(1)
                    print('\033[32mÉ a vez de Doug!\033[m')

                    movimento_doug = random.choice(chance)

                    if amount_ea_doug == 36:
                        possib = random.choice(chance)
                        frase_dg_han = random.choice(frases_han_doug)

                        amount_ea_doug -= 35

                        sleep(1)
                        print('')
                        print(frase_dg_han)
                        if possib == 6:
                            sleep(1)
                            print('\033[32mDano crítico!\033[m')
                            vida_monstro -= (dano_han_doug + doug_atri['Critico'])
                        else:
                            vida_monstro -= dano_han_doug

                    elif (movimento_doug == 1 or movimento_doug == 3 or movimento_doug == 7) and not doug_shield:
                        doug_shield = True

                        amount_ea_doug += ganhar_bonus_ea(amount_ea_doug, (2, 3, 4, 5, 6))

                        sleep(1)
                        print('\033[32mDoug levanta seu escudo.')

                    elif movimento_doug == 2 or movimento_doug == 5:
                        possib = random.choice(chance)
                        frase_dg_escudo = random.choice(frases_escudo_doug)

                        if possib % 2 == 1:
                            amount_ea_doug += ganhar_bonus_ea(amount_ea_doug, (8, 9, 10, 11, 12))

                            sleep(1)
                            print('')
                            print(frase_dg_escudo)
                            if possib == 3 or possib == 5:
                                sleep(1)
                                print('\033[32mDano crítico!\033[m')
                                vida_monstro -= (dano_escudo_doug + doug_atri['Critico'])
                            else:
                                vida_monstro -= dano_escudo_doug

                        else:
                            print(f'\n\033[31mDoug tenta atacar {nome_monstro}, mas erra!\033[m')

                    else:
                        possib = random.choice(chance)
                        frase_dg_espada = random.choice(frases_espada_doug)

                        if possib != 9:
                            amount_ea_doug += ganhar_bonus_ea(amount_ea_doug, (6, 7, 8, 9, 10))

                            sleep(1)
                            print('')
                            print(frase_dg_espada)
                            if possib == 7 or possib == 8 or possib == 10:
                                sleep(1)
                                print('\033[32mDano crítico!\033[m')
                                vida_monstro -= (dano_espada_doug + doug_atri['Critico'])
                            else:
                                vida_monstro -= dano_espada_doug

                        else:
                            print(f'\n\033[31mDoug tenta atacar {nome_monstro}, mas erra!\033[m')

                # CASO DOUG TENHA DESMAIADO ───────────────────────────────────────────────────────
                elif rodada == 2 and doug_life is False:
                    sleep(1)
                    print('\033[31mDoug não consegue atacar mais. Ele passa a rodada.')
                    rodada += 1

            # CASO SEJA A VEZ DE GUSTAV ────────────────────────────────────────────────────────
            if gustav:
                if rodada == 3 and gustav_life:
                    frases_ataque_gustav = (
                        f'\033[32mGustav ataca o {nome_monstro} com magia.\033[m',
                        '\033[32mGustav queima o monstro com fogo mágico.\033[m',
                        f'\033[32mGustav ativa seus poderes elétricos no {nome_monstro}.\033[m',
                        '\033[32mGustav joga o monstro no ar, fazendo ele cair com força no chão.\033[m',
                        f'\033[32mGustav invoca búfalos fantasma que atropelam o {nome_monstro}\033[m'
                    )

                    sleep(1)
                    print('\033[32mÉ a vez de Gustav!\033[m')

                    movimento_gustav = random.choice(chance)

                    if amount_ea_gustav == 36:
                        amount_ea_gustav -= 35

                        recuperar = (75 - attributes['Vida'])
                        if not recuperar:
                            print('\033[32mFelizmente, você não precisou de cura.\033[m')
                        else:
                            attributes['Vida'] += recuperar
                            print(f'\033[32mGustav recuperou {recuperar} da sua \033[31mVida!\033[m')

                        if doug:
                            recuperar = (50 - doug_atri['Vida'])
                            if not recuperar:
                                print('\033[32mFelizmente, Doug não precisou de cura.\033[m')
                            else:
                                doug_atri['Vida'] += recuperar
                                print(f'\033[32mGustav recuperou {recuperar} da \033[31mVida\033[32m de Doug!\033[m')

                        special_shield_gustav = True
                        sleep(2)
                        print('\n\033[32mA magia de Gustav transborda com o poder de cura.')
                        sleep(1)
                        print('O inimigo não pode tocá-lo com tanta energia vazando dele.')

                    elif movimento_gustav == 6:
                        possib = random.choice(chance)

                        if possib % 2 == 0:
                            amount_ea_gustav += ganhar_bonus_ea(amount_ea_gustav, (1, 2, 3, 4))

                            sleep(1)
                            print('')
                            print('\033[32mGustav ataca com seu cajado, mas não parece fazer muita diferença.\033[m')
                            if possib == 1:
                                sleep(1)
                                print('\033[32mDano crítico!\033[m')
                                vida_monstro -= (dano_fisico_gustav + gustav_atri['Critico'])
                            else:
                                vida_monstro -= dano_fisico_gustav

                        else:
                            print(f'\n\033[31mGustav tenta atacar {nome_monstro}, mas erra!\033[m')

                    elif (
                            movimento_gustav == 1 or movimento_gustav == 3 or movimento_gustav == 5) and not gustav_shield:
                        gustav_shield = True

                        amount_ea_gustav += ganhar_bonus_ea(amount_ea_gustav, (6, 7, 8, 9, 10))

                        sleep(1)
                        print('\033[32mGustav cria um escudo protetor para vocês.')
                        sleep(1)
                        print('\033[32mVocês estão protegidos por duas rodadas.\033[m')

                    else:
                        possib = random.choice(chance)
                        frase_gv = random.choice(frases_ataque_gustav)

                        if possib != 5:
                            amount_ea_gustav += ganhar_bonus_ea(amount_ea_gustav, (8, 9, 10, 11, 12))

                            sleep(1)
                            print('')
                            print(frase_gv)
                            if possib == 1 or possib == 2 or possib == 3:
                                sleep(1)
                                print('\033[32mDano crítico!\033[m')
                                vida_monstro -= (dano_magico_gustav + gustav_atri['Critico'])
                            else:
                                vida_monstro -= dano_magico_gustav

                        else:
                            print(f'\n\033[31mGustav tenta atacar {nome_monstro}, mas erra!\033[m')

                # CASO GUSTAV TENHA DESMAIADO ───────────────────────────────────────────────────────
                elif rodada == 3 and not gustav_life:
                    sleep(1)
                    print('\033[31mGustav não consegue atacar mais. Ele passa a rodada.')
                    rodada += 1
                    continue

            # PARA DESATIVAR ESCUDO CASO ESTEJA ATIVADO ─────────────────────────────────────────
            if gustav_shield:
                rodada_shield += 1
                if rodada_shield > 2:
                    gustav_shield = False
                    sleep(1)
                    print('\033[31mO escudo de Gustav é desativado.\033[m')
                    rodada_shield = 0

            sleep(1)
            print('')

            # PARA MONSTRO ATACAR ───────────────────────────────────────────────────────────────────
            if vida_monstro > 0:
                possib = random.choice(chance)
                atacar = random.choice(characters)
                if atacar == perso_info['Nome']:
                    atacar = 'você'

                if possib not in hit_chance:
                    sleep(1)
                    print(f'\033[32m{nome_monstro} tenta atacar {atacar}, mas erra.\033[m')

                else:
                    sleep(1)
                    print(f'\033[31m{nome_monstro} ataca {atacar}.')

                    if gustav_shield:
                        sleep(1)
                        print('\033[32mMas o escudo de Gustav protege vocês.\033[m')
                        rodada += 1
                        continue

                    if atacar == 'você':
                        if camuflade:
                            if accuracy_rate != 0:
                                chance_de_dano = random.choice((True, True, True, False, True))

                                if chance_de_dano:
                                    sleep(1)
                                    print(f'\033[32mPorém, erra.\033[m')
                                    rodada += 1
                                    continue

                                else:
                                    sleep(1)
                                    print('\033[31mSua camuflagem se desfez!\033[m\n')
                                    camuflade = False

                            else:
                                sleep(1)
                                print(f'\033[31m{nome_monstro} tem uma mira certeira! Sua camuflagem se desfez!\033[m\n')
                                camuflade = False


                        if dano_monstro > attributes['Vida']:
                            dano_monstro = attributes['Vida']

                        attributes['Vida'] -= dano_monstro
                        sleep(1)
                        print(f'\033[32mVocê perde {dano_monstro} de \033[31mVida\033[m')

                        amount_ea += ganhar_bonus_ea(amount_ea, (1, 2))

                    else:
                        if atacar == gustav_atri['Nome']:
                            if special_shield_gustav:
                                sleep(1)
                                print('\033[32mMas a magia de Gustav o protege\033[m')
                            else:
                                gustav_atri['Vida'] -= round(ataque_monstro * (100 / (100 + gustav_atri['Defesa'])))

                        elif atacar == doug_atri['Nome']:
                            if doug_shield:
                                sleep(1)
                                print('\033[32mO escudo dele o protege.\033[m')
                                doug_shield = False
                                sleep(1)
                                print('\033[31mDoug deixa seu escudo cair.\033[m')
                            else:
                                doug_atri['Vida'] -= round(ataque_monstro * (100 / (100 + doug_atri['Defesa'])))

            rodada += 1

        while True:
            try_again = input('Você quer lutar novamente? [S/N] ').upper().strip()
            if try_again not in 'SN':
                sleep(1)
                print('Oh não... Tente novamente.')
            else:
                break

        if try_again == 'S':
            if gustav:
                gustav_atri = gustav_atri_backup.copy()
            if doug:
                doug_atri = doug_atri_backup.copy()

            reset_atri()
            vida_monstro = vida_monstro_backup
        else:
            return False


if __name__ == '__main__':
    perso_info = {'Nome': 'Ethaniel', 'Classe': 'Arqueiro'}
    attributes = {'Vida': 75, 'Ataque': 35, 'Defesa': 15, 'Flecha': 5, 'Energia': 30, 'Critico': 20}

    fight_archer('Sir Guto', 700, 12, 10, 2)
