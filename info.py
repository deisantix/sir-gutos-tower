from time import sleep
from os import path
import random
import conq

doug_atri = {'Nome': 'Doug', 'Vida': 50, 'Ataque': 35, 'Defesa': 110, 'Escudo': 55, 'Han': 70, 'Energia': 30, 'Critico': 10}
noelle_atri = {'Nome': 'Noelle', 'Vida': 75, 'Ataque': 35, 'Defesa': 15, 'Energia': 30, 'Critico': 20}
gustav_atri = {'Nome': 'Gustav', 'Vida': 50, 'Ataque': 5, 'Defesa': 10, 'Magia': 35, 'Energia': 210, 'Critico': 15}

txt = ''
tempo = 20
deaths = 0
perso_info = {}
attributes = {}
inventario = {}
achievements = {}
attributes_backup = attributes.copy()

itens = {'Barrinha Protein': {'Quantidade': 1, 'Descricao': 'Parece uma boa fonte de Energia, e um ótimo petisco...', 'Efeito': 35, 'Onde': 'E'}}


# FUNÇÃO PARA VERIFICAR SAVE
def ver_save():
    file1_exists = path.isfile('.info')
    file2_exists = path.isfile('.save')
    filesize = path.getsize('.info')

    global txt
    txt = ''

    if file1_exists is False or file2_exists is False or filesize <= 2:
        save = open('.info', 'a+')
        save_2 = open('.save', 'a+')
        save.write('conquistas:\n')

    else:
        save = open('.info', 'a+')
        save_2 = open('.save', 'a+')

        while True:
            sleep(1)
            keep = input('Deseja resetar o save? [N/S] ').upper().strip()
            if keep not in 'SN':
                sleep(1)
                print('Oh não... Tente novamente.')
            else:
                break

        if keep == 'S':
            save.truncate(0)
            save_2.truncate(0)

            save.write('conquistas:\n')
        elif keep == 'N':
            txt = 'PPCOP'

    save.close()
    save_2.close()


# FUNÇÃO PARA MODIFICAR O ARQUIVO DE TEXTO
def modi_file(texto, arquivo, pos, mode='w'):
    file = open(arquivo, "r+")
    list_lines = file.readlines()

    if mode == 'w':
        file_size = path.getsize(arquivo)
        if file_size <= 2:
            file.write(texto)

        elif pos > len(list_lines)-1:
            file.write(texto)

        else:
            list_lines[pos] = texto

            file = open(arquivo, "w")
            file.writelines(list_lines)

    elif mode == 'a':
        list_lines[pos] = list_lines[pos].rstrip() + texto + '\n'
        file = open(arquivo, "w")
        file.writelines(list_lines)


# FUNÇÃO PARA DEFINIR VELOCIDADE DE NARRATIVA
def velo_narrativa():
    print('\n\033[mQUAL A VELOCIDADE QUE VOCÊ PREFERE O TEXTO?')
    print('\033[33m[1] NORMAL')
    print('[2] RÁPIDO (Recomendado)')
    print('[3] INSTANTÂNEO\033[m')
    sleep(1)

    while True:
        escolha = input('Digite a velocidade: ')
        if escolha not in '123':
            sleep(1)
            print('\033[31mNão é uma opção.\033[m\n')
            continue
        else:
            break

    global tempo
    if escolha == '1':
        tempo = 20
    elif escolha == '2':
        tempo = 70
    elif escolha == '3':
        tempo = 0

    return tempo


# FUNÇÃO DE NARRATIVA
def narrativa(comeco, final, arquivo):
    file = open(arquivo)
    dia = file.readlines()

    nar = []
    sleep(1)
    print(end='\n')
    for linha in range(len(dia)):
        if final in dia[linha]:
            break
        elif comeco in dia[linha]:
            nar.append(dia[linha][len(comeco) + 1:-1])
    file.close()

    for linha in nar:
        if tempo == 0:
            seg = 0
        else:
            seg = round(len(linha) / tempo)

        if '{NOME}' in linha:
            linha = linha.replace('{NOME}', perso_info['Nome'])
        if '{a}' in linha:
            if perso_info['Genero'] == 'M':
                linha = linha.replace('{a}', 'o')
            else:
                linha = linha.replace('{a}', 'a')
        if '{e}' in linha:
            if perso_info['Genero'] == 'M':
                linha = linha.replace('{e}', 'e')
            else:
                linha = linha.replace('{e}', 'a')
        if '{ae}' in linha:
            if perso_info['Genero'] == 'M':
                linha = linha.replace('{ae}', '')
            else:
                linha = linha.replace('{ae}', 'a')

        print(f'\033[32m{linha}')
        sleep(seg)


# FUNÇÃO QUE DESIGNA TODAS AS CARACTERÍSTICAS INICIAIS DO PERSONAGEM PRINCIPAL
def caract():
    global perso_info

    if txt == 'PPCOP':
        with open('.info', 'r+') as save:
            for line in save:
                line = line.rstrip()
                if 'Genero' in line:
                    perso_info['Genero'] = line[8:]
                elif 'Nome' in line:
                    perso_info['Nome'] = line[6:]
                elif 'Classe' in line:
                    perso_info['Classe'] = line[8:]
                elif 'Arquivo' in line:
                    arquivo = line[9:]

            if 'Classe' in perso_info and 'Nome' in perso_info and 'Genero' in perso_info:
                return perso_info, arquivo
            else:
                sleep(1)
                print('\033[31mARQUIVO DE PROGRESSO INCOMPLETO. REINICIANDO...\033[m')
                sleep(1)
                save.truncate(0)
                ver_save()

    # GENERO ───────────────────────────────────────────────────────────────────────────────
    while True:
        sleep(1)
        genero = input('\nDigite seu gênero [M/F]: ').upper().strip()
        if genero not in 'MF':
            sleep(1)
            print('Oh não... Tente novamente.')
            continue
        else:
            break

    perso_info['Genero'] = genero

    with open('.info', 'a') as save:
        save.write(f'Genero: {genero}\n')

    # NOME ────────────────────────────────────────────────────────────────────────────────
    while True:
        sleep(1)
        nome = input('Digite o nome do seu personagem: ').capitalize().strip()

        while True:
            sleep(1)
            assure = input(f'\033[33m{nome}\033[m? Esse nome está correto? [S/N]: ').upper().strip()
            if assure not in 'SN':
                sleep(1)
                print('Oh não... Tente novamente.')
                continue
            else:
                break

        if assure == 'S':
            break
        else:
            continue

    perso_info['Nome'] = nome

    with open('.info', 'a') as save:
        save.write(f'Nome: {nome}\n')

    # CLASSE ────────────────────────────────────────────────────────────────────────────
    while True:
        sleep(1)
        print('\nAgora escolha sua classe!')
        sleep(.5)
        print('[1] \033[95mFeiticeiro\033[m [2] \033[37mCavalheiro\033[m [3] \033[33mArqueiro\033[m [4] Saber mais?')
        sleep(.5)
        classe = input('Digite um número para escolher a classe: ').strip()

        # OPÇÃO 1
        if classe == '1':
            perso_info['Classe'] = 'Feiticeiro'
            arquivo = 'pov_witcher'

            with open('.info', 'a') as save:
                save.write('Classe: Feiticeiro\n')
                save.write('Arquivo: pov_witcher\n')

            print('Você escolheu \033[95mFeiticeiro\033[m!')
            sleep(2)
            break

        # OPÇÃO 2
        elif classe == '2':
            perso_info['Classe'] = 'Cavalheiro'
            print('\033[37mCavalheiro\033[m não está disponível.')
            # print('Você escolheu \033[37mCavalheiro\033[m!')
            sleep(2)
            continue

        # OPÇÃO 3
        elif classe == '3':
            perso_info['Classe'] = 'Arqueiro'
            print('\033[33mArqueiro\033[m não está disponível.')
            # print('Você escolheu \033[33mArqueiro\033[m!')
            sleep(2)
            continue

        # OPÇÃO 4 ─ EXPLICAÇÃO
        elif classe == '4':
            while True:
                narrativa('classes.', 'fim.', '.help')

                while True:
                    gotit = input('\n\033[mEntendeu? [S/N] ').upper().strip()
                    if gotit not in 'SN':
                        sleep(1)
                        print('Oh não... Tente novamente.')
                        continue
                    else:
                        break

                if gotit == 'S':
                    break
                else:
                    continue

        else:
            sleep(1)
            print('\033[31mNão é uma opção.\033[m')
            continue

    return perso_info, arquivo


# FUNÇÃO QUE DESIGNA OS attributes DO PERSONAGEM DEPENDENDO DA SUA CLASSE
def skills():
    global attributes, attributes_backup
    if perso_info['Classe'] == 'Feiticeiro':
        attributes = {'Vida': 50, 'Ataque': 5, 'Defesa': 10, 'Magia': 35, 'Energia': 210, 'Critico': 15}
    elif perso_info['Classe'] == 'Cavalheiro':
        attributes = {'Vida': 50, 'Ataque': 35, 'Defesa': 110, 'Escudo': 55, 'Han': 70, 'Energia': 30, 'Critico': 10}
    elif perso_info['Classe'] == 'Arqueiro':
        attributes = {'Vida': 75, 'Ataque': 35, 'Defesa': 15, 'Energia': 30, 'Critico': 20}

    attributes_backup = attributes.copy()

    return attributes


# MOSTRAR attributes FORMATADOS E COLORIDOS:
def show_atri():
    sleep(1)
    for d in attributes:
        if d == 'Vida':
            print(f'\033[31m{d:<7}\033[m: {attributes[d]:>0}')
        elif d == 'Ataque':
            print(f'\033[33m{d:<7}\033[m: {attributes[d]:>0}')
        elif d == 'Defesa':
            print(f'\033[37m{d:<7}\033[m: {attributes[d]:>0}')
        elif d == 'Magia':
            print(f'\033[35m{d:<7}\033[m: {attributes[d]:>0}')
        elif d == 'Escudo':
            print(f'\033[37m{d:<7}\033[m: {attributes[d]:>0}')
        elif d == 'Han':
            print(f'\033[33m{d:<7}\033[m: {attributes[d]:>0}')
        elif d == 'Energia':
            print(f'\033[95m{d:<7}\033[m: {attributes[d]:>0}')
        elif d == 'Critico':
            continue


# FUNÇÃO PARA VER INVENTÁRIO FORMATADO:
def show_inve():
    global inventario

    sleep(1)
    mapear = {}

    with open('.save') as save:
        for line in save:
            if 'Itens:' in line:

                for key in itens:
                    if key in line:
                        x = inventario.get(key, 0)

                        if x == 0:
                            inventario[key] = itens[key]

                            psc = line.find(key)
                            qtd = int(line[psc+len(key)])
                            inventario[key]['Quantidade'] = qtd

    # SE INVENTÁRIO ESTIVER VAZIO ─────────────────────────────────────────────────────────────────
    if inventario == {}:
        print('\033[37mSeu inventário está vazio...\033[m\n')

    # CASO NÃO ESTEJA VAZIO ────────────────────────────────────────────────────────────────────────
    else:
        # IMPRIMIR ITENS DENTRO DO INVENTÁRIO ──────────────────────────────────────────────────────
        for pos, i in enumerate(inventario):
            print(f'\033[33m[{pos}] {i:<10}\033[m: \033[31m{inventario[i]["Quantidade"]:>0}\033[m')
            mapear[str(pos)] = i

        # PARA USAR OU NÃO UM ITEM ─────────────────────────────────────────────────────────────────
        while True:
            sleep(1)
            decision = input('\nDigite o número do item que deseja acessar ou N para sair: ').upper().strip()
            if decision in mapear:
                decision = mapear[decision]

                # nome do item e efeito
                print(f'\033[33m{decision}\033[m: '
                      f'\033[31m{inventario[decision]["Efeito"]} {inventario[decision]["Onde"]}\033[m')
                # descrição
                print(f'\033[32m{inventario[decision]["Descricao"]}\033[m')

                while True:
                    sleep(1)
                    decisao = input('\nDeseja usar este item? [S/N] ').upper().strip()
                    if decisao not in 'SN':
                        sleep(1)
                        print('\033[31mNão é uma opção.\033[m')

                    else:
                        break

                # CASO NÃO QUEIRA USAR O ITEM ────────────────────────────────────────────
                if decisao == 'N':
                    continue

                # CASO USE O ITEM ───────────────────────────────────────────────────────
                else:
                    if inventario[decision]['Onde'] == 'E':
                        attributes['Energia'] += inventario[decision]['Efeito']

                        sleep(1)
                        print(f'\033[32mVocê usou \033[33m{decision}\033[32m!')
                        sleep(1)
                        print(f'Sua \033[95mEnergia\033[32m aumentou \033[31m{inventario[decision]["Efeito"]}\033[32m!\033[m\n')
                        sleep(1)

                        # DIMINUIR QUANTIDADE CASO FOR MAIS DE UM MESMO ITEM ────────────────────────────
                        if inventario[decision]['Quantidade'] > 1:
                            inventario[decision]['Quantidade'] -= 1

                            with open('.save', 'r+') as save:
                                list_l = save.readlines()

                                for line in list_l:
                                    if decision in line:
                                        psc = list_l[2].find(decision)
                                        old_nmbr = int(list_l[2][psc + len(decision)])

                                        nmbr = old_nmbr - 1
                                        old_nmbr = str(old_nmbr)
                                        nmbr = str(nmbr)

                                        listnew = list_l[2].replace(decision+old_nmbr, decision+nmbr)
                                        list_l[2] = listnew

                                        save = open('.save', 'w')
                                        save.writelines(list_l)

                        # EXCLUIR ITEM DO INVENTARIO CASO SEJA APENAS UM ───────────────────────────────
                        elif inventario[decision]['Quantidade'] == 1:
                            del inventario[decision]

                            with open('.save', 'r+') as save:
                                list_l = save.readlines()

                                for line in list_l:
                                    if decision in line:
                                        listnew = list_l[2].replace(decision+'1,', '')
                                        list_l[2] = listnew

                                        save = open('.save', 'w')
                                        save.writelines(list_l)

                        break


            elif decision in 'N':
                break

            else:
                sleep(1)
                print('\033[31mNão é uma opção.\033[m')


# FUNÇÃO PARA TOMAR DECISÕES
def make_decision(options):
    # OPTIONS == STRING
    while True:
        dc = input('\033[mO que você vai fazer? ').strip()
        if dc not in options or dc == '':
            sleep(1)
            print('\033[31mNão é uma opção.\033[m\n')
            continue

        with open('.save') as save:
            file = save.read()
            if 'Inventario: False' in file:

                # VER attributes
                if dc == options[-1]:
                    show_atri()
                    continue
                else:
                    break

            elif 'Inventario: True' in file:

                # VER attributes
                if dc == options[-2]:
                    show_atri()
                    continue

                # ABRIR INVENTÁRIO
                elif dc == options[-1]:
                    show_inve()
                    continue

                else:
                    break

    return dc


# VOLTAR ATRIBUTOS PARA OS VALORES INICIAIS
def reset_atri():
    global attributes, attributes_backup
    attributes = attributes_backup.copy()

    return attributes


# SALVAR ATRIBUTOS NO .SAVE
def save_atri():
    modi_file('Atributos\n', '.save', 6)

    for pos, k in enumerate(attributes):
        modi_file(f'{k}: {attributes[k]}\n', '.save', pos+7)


# ADICIONAR ITEM AO INVENTÁRIO DO JOGADOR
def add_inve(key, value):
    global inventario
    inventario[key] = value

    modi_file(f' {key},', '.save', 2, 'a')


# SALVAR CONQUISTAS NO .INFO E PEGÁ-LAS DE VOLTA CASO PRECISE
def achieve(conquis=None):
    global achievements

    if conquis is not None:
        with open('.info') as inform:
            file = inform.read()
            if conquis in file:
                return None

        if conquis in conq.conquistas:
            modi_file(f' {conquis},', '.info', 0, 'a')
            achievements[conquis] = conq.conquistas[conquis]

    else:
        with open('.info') as save:
            inform = save.read()
            if 'conquistas' in inform:

                for key in conq.conquistas:
                    if key in inform:
                        x = achievements.get(key, 0)

                        if x == 0:
                            achievements[key] = conq.conquistas[key]

        print(f'\n\033[93m{"CONQUISTAS ":─<40}\033[m')
        sleep(1)
        for k in achievements:
            print(f'\033[93m{k}\033[m: \033[32m{achievements[k]}\033[m')

        tm = len(conq.conquistas)
        tm_nw = len(achievements)
        print(f'{tm_nw} de {tm} alcançadas\n')


# CONTADOR DE MORTES
def death_count():
    global deaths

    with open('.info',) as file:
        inform = file.read()
        if 'Mortes' in inform:
            dth = True
        else:
            dth = False

    if dth is True:
        with open('.info') as file:
            inform = file.readlines()

            for line in inform:
                if 'Mortes' in line:
                    deaths = int(line[7:])
                    old_number = deaths
                    deaths += 1

                    newline = inform[5].replace(f'Mortes: {old_number}\n', f'Mortes: {deaths}\n')
                    inform[5] = newline

                    file = open('.info', 'w')
                    file.writelines(inform)

    else:
        modi_file('Mortes: 1\n', '.info', 5)
        deaths = 1

    if deaths == 1:
        achieve('Má decisão')


#  ▄█     █▄   ▄█      ███      ▄████████    ▄█    █▄       ▄████████    ▄████████
# ███     ███ ███  ▀█████████▄ ███    ███   ███    ███     ███    ███   ███    ███
# ███     ███ ███▌    ▀███▀▀██ ███    █▀    ███    ███     ███    █▀    ███    ███
# ███     ███ ███▌     ███   ▀ ███         ▄███▄▄▄▄███▄▄  ▄███▄▄▄      ▄███▄▄▄▄██▀
# ███     ███ ███▌     ███     ███        ▀▀███▀▀▀▀███▀  ▀▀███▀▀▀     ▀▀███▀▀▀▀▀
# ███     ███ ███      ███     ███    █▄    ███    ███     ███    █▄  ▀███████████
# ███ ▄█▄ ███ ███      ███     ███    ███   ███    ███     ███    ███   ███    ███
#  ▀███▀███▀  █▀      ▄████▀   ████████▀    ███    █▀      ██████████   ███    ███
def fight_witch(nome_monstro, vida_monstro, ataque_monstro, defesa_monstro, accuracy_rate):
    global attributes, doug_atri, noelle_atri
    doug = noelle = doug_life = noelle_life = at_esp = ms_noelle = ms_doug = amount_ea = dano_noelle = dano_doug = None
    doug_atri_backup = None
    noelle_atri_backup = None

    if 0 > accuracy_rate > 10:
        return None

    accuracy = accuracy_rate
    chance = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']

    hit_chance = []

    count = 10 - accuracy
    while count > 0:
        x = random.choice(chance)

        if x in hit_chance:
            continue

        hit_chance.append(x)

        count -= 1

    characters = [f'{perso_info["Nome"]}']

    with open('.save') as save:
        inform = save.read()
        if 'Doug: False' in inform and 'Noelle: False' in inform:
            doug = False
            noelle = False
        elif 'Doug: True' in inform and 'Noelle: True' in inform:
            doug = True
            noelle = True

        if 'AT_ESP: False' in inform:
            at_esp = False
        elif 'AT_ESP: True' in inform:
            at_esp = True

    if doug is True:
        characters.append('Doug')
        doug_atri_backup = doug_atri.copy()
        dano_doug = round(doug_atri['Ataque'] * (100 / (100 + defesa_monstro)))
    if noelle is True:
        characters.append('Noelle')
        noelle_atri_backup = noelle_atri.copy()
        dano_noelle = round(noelle_atri['Ataque'] * (100 / (100 + defesa_monstro)))

    witcher_atri_backup = attributes.copy()
    vida_monstro_backup = vida_monstro

    dano_monstro = round(ataque_monstro * (100 / (100 + attributes['Defesa'])))

    dano_magico = round(attributes['Magia'] * (100 / (100 + defesa_monstro)))
    dano_fisico = round(attributes['Ataque'] * (100 / (100 + defesa_monstro)))

    frases_ataque = (f'\033[32mVocê ataca o {nome_monstro} com magia.\033[m',
                     '\033[32mVocê queima o monstro com fogo mágico.\033[m',
                     f'\033[32mVocê ativa seus poderes elétricos no {nome_monstro}.\033[m',
                     '\033[32mVocê joga o monstro no ar, fazendo ele cair com força no chão.\033[m',
                     f'\033[32mVocê invoca búfalos fantasma que atropelam o {nome_monstro}\033[m')

    # SISTEMA DE LUTA ────────────────────────────────────────────────────────────────
    while True:
        shield = False
        special_shield = False

        if doug is True and noelle is True:
            noelle_life = True
            ms_noelle = 0
            doug_life = True
            ms_doug = 0

        if at_esp is True:
            amount_ea = 1

        rodada = 1
        rodada_shield = 0
        ataque_anterior = ['']

        while True:
            # SE O MONSTRO MORRER ────────────────────────────────────────────────────────
            if vida_monstro <= 0:
                sleep(1)
                print('\033[33mVocês ganharam!\033[m')
                return True, noelle, doug

            # SE O JOGADOR DESMAIAR ──────────────────────────────────────────────────────
            if attributes['Vida'] <= 0:
                sleep(1)
                print('\033[31mSUA VIDA CHEGOU A \033[33M0\033[m')
                sleep(1)
                print('\033[32mO grupo não pode continuar sem você.\033[m')
                break

            # SE NOELLE DESMAIAR ────────────────────────────────────────────────────────
            if noelle is True:
                if noelle_atri['Vida'] <= 0 and ms_noelle == 0:
                    sleep(1)
                    print('\033[31mA VIDA DE NOELLE CHEGOU A \033[33m0\033[m')
                    sleep(1)
                    print('\033[32mEla não atacará mais durante a luta.\033[m')

                    characters.remove('Noelle')
                    noelle_life = False
                    ms_noelle += 1

            # SE DOUG DESMAIAR ──────────────────────────────────────────────────────────
            if doug is True:
                if doug_atri['Vida'] <= 0 and ms_doug == 0:
                    sleep(1)
                    print('\033[31mA VIDA DE DOUG CHEGOU A \033[33m0\033[m')
                    sleep(1)
                    print('\033[32mEle não atacará mais durante a luta.\033[m')

                    characters.remove('Doug')
                    doug_life = False
                    ms_doug += 1

            # IMPRIMIR NOME DO MONSTRO E VIDA ───────────────────────────────────────────
            sleep(1)
            print(f'\n\033[31m{nome_monstro}\033[m: [\033[33m{vida_monstro} HP\033[m]')
            print('=' * 40)

            if doug is True and noelle is True:
                if rodada == 4:
                    rodada = 1
            else:
                if rodada == 2:
                    rodada = 1

            # CASO ENERGIA AINDA ESTEJA TRANSBORDANDO ─────────────────────────────────────────
            if special_shield is True:
                special_shield = False
                sleep(1)
                print('\033[31mSua proteção se desfez.\033[m\n')

            # CASO SEJA A VEZ DO FEITICEIRO ─────────────────────────────────────────────────
            if rodada == 1:
                print('\033[32mÉ a sua vez!\033[m\n')

                if amount_ea is not None:
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
                if attributes['Energia'] > 15:
                    print('\033[33m[1] Atacar com magia \033[36m(-15 E)')
                else:
                    print('\033[31m[1] Atacar com magia (-15 E)')

                if attributes['Energia'] > 6:
                    print('\033[33m[2] Defender \033[36m(-6 E)')
                else:
                    print('\033[31m[2] Defender (-6 E)')

                if attributes['Energia'] > 2:
                    print('\033[33m[3] Atacar com cajado \033[36m(-2 E)')
                else:
                    print('\033[31m[3] Atacar com cajado (-2 E)')

                if at_esp is True:
                    if amount_ea == 36:
                        print('\033[33m[4] Curar companheiros (-AE)')
                    else:
                        print('\033[31m[4] Curar companheiros (-AE)')
                    print('\033[33m[5] VER ATRIBUTOS')
                else:
                    print('\033[33m[4] VER ATRIBUTOS')

                if at_esp is True:
                    decision = make_decision('12345')
                else:
                    decision = make_decision('1234')

                # ESCOLHER A FRASE QUE VAI APARECER QUANDO O JOGADOR ATACAR ─────────────────────
                frase_sn = random.choice(frases_ataque)

                # SE USAR MAGIA ──────────────────────────────────────────────────────────────────
                if decision == '1':
                    if attributes['Energia'] < 15:
                        sleep(1)
                        print('\n\033[31mVocê não tem energia suficiente para essa ação.\033[m')
                        continue

                    possib = random.choice(chance)

                    ataque_anterior.append(decision)
                    if len(ataque_anterior) > 2:
                        ataque_anterior.pop(0)

                    if possib != 5:
                        if at_esp is True:
                            bonus_ea = random.choice((8, 9, 10, 11, 12))
                            if amount_ea != 36:
                                if amount_ea + bonus_ea > 36:
                                    r_ea = 36 - amount_ea
                                    amount_ea += r_ea
                                else:
                                    amount_ea += bonus_ea

                        attributes['Energia'] = attributes['Energia'] - 15

                        if possib == 1 or possib == 2 or possib == 3:
                            vida_monstro -= (dano_magico + attributes['Critico'])
                            sleep(1)
                            print(frase_sn)
                            sleep(1)
                            print('\033[32mDano crítico!\033[m')
                        else:
                            vida_monstro -= dano_magico
                            sleep(1)
                            print(frase_sn)
                    else:
                        print('\n\033[31mVocê errou!\033[m')

                # SE ATIVAR ESCUDO ───────────────────────────────────────────────────────────
                elif decision == '2':
                    if attributes['Energia'] < 6:
                        sleep(1)
                        print('\n\033[31mVocê não tem energia suficiente para essa ação.\033[m')
                        continue

                    elif shield is True or special_shield is True:
                        sleep(1)
                        print('\n\033[31mO escudo ainda está ativo! Espere uma rodada.\033[m')
                        continue

                    ataque_anterior.append(decision)
                    if len(ataque_anterior) > 2:
                        ataque_anterior.pop(0)

                    if ataque_anterior[0] == '2':
                        sleep(1)
                        print('\n\033[31mVocê não pode executar essa ação duas vezes seguidas!')
                        sleep(1)
                        print('\033[32mEspere mais uma rodada.\033[m')
                        continue

                    attributes['Energia'] = attributes['Energia'] - 6
                    shield = True

                    if at_esp is True:
                        bonus_ea = random.choice((6, 7, 8, 9, 10))
                        if amount_ea != 36:
                            if amount_ea + bonus_ea > 36:
                                r_ea = 36 - amount_ea
                                amount_ea += r_ea
                            else:
                                amount_ea += bonus_ea

                    sleep(1)
                    print('\033[32mVocê cria um escudo protetor para você e seus companheiros.')
                    sleep(1)
                    print('\033[32mVocês estão protegidos por duas rodadas.\033[m')

                # SE ATACAR COM CAJADO ───────────────────────────────────────────────────────────
                elif decision == '3':
                    if attributes['Energia'] < 2:
                        sleep(1)
                        print('\n\033[31mVocê não tem energia suficiente para essa ação.\033[m')
                        continue

                    possib = random.choice(chance)

                    ataque_anterior.append(decision)
                    if len(ataque_anterior) > 2:
                        ataque_anterior.pop(0)

                    if possib % 2 == 0:

                        if at_esp is True:
                            bonus_ea = random.choice((1, 2, 3, 4))
                            if amount_ea != 36:
                                if amount_ea + bonus_ea > 36:
                                    r_ea = 36 - amount_ea
                                    amount_ea += r_ea
                                else:
                                    amount_ea += bonus_ea

                        attributes['Energia'] = attributes['Energia'] - 2
                        if possib == 1:
                            vida_monstro -= (dano_fisico + attributes['Critico'])
                            sleep(1)
                            print('\033[32mVocê ataca com seu cajado.')
                            sleep(1)
                            print('\033[32mDano crítico!\033[m')
                        else:
                            vida_monstro -= dano_fisico
                            sleep(1)
                            print('\033[32mVocê ataca com seu cajado, mas não parece fazer muita diferença.\033[m')
                    else:
                        print('\n\033[31mVocê errou!\033[m')

                # SE CURAR COMPANHEIROS COM MAGIA ───────────────────────────────────────────────────────────────
                if at_esp is True:
                    if decision == '4':
                        if amount_ea != 36:
                            sleep(1)
                            print('\n\033[31mVocê ainda não armazenou magia o suficiente!\033[m')
                            sleep(1)
                            print('\033[32mEncha seu \033[36mAtaque Especial\033[32m para executar essa ação.\033[m')
                            continue

                        ataque_anterior.append(decision)
                        if len(ataque_anterior) > 2:
                            ataque_anterior.pop(0)

                        amount_ea -= 35

                        if doug_life is False:
                            print('\033[33mDoug recuperou suas forças!\033[m')
                            doug_life = True
                            ms_doug = 0
                            characters.append('Doug')

                        if doug_atri['Vida'] != doug_atri_backup['Vida']:
                            cura = random.choice((25, 26, 27, 28, 29, 30))

                            doug_atri['Energia'] = doug_atri_backup['Energia']

                            if doug_atri['Vida'] + cura > doug_atri_backup['Vida']:
                                cura = doug_atri_backup['Vida'] - doug_atri['Vida']
                                doug_atri['Vida'] += cura

                                sleep(1)
                                print(f'\033[32mVocê curou \033[31m{cura}\033[32m da \033[31mVida\033[32m de Doug!\033[m')
                            else:
                                doug_atri['Vida'] += cura
                                sleep(1)
                                print(f'\033[32mVocê curou \033[31m{cura}\033[32m da \033[31mVida\033[32m de Doug!\033[m')

                        else:
                            sleep(1)
                            print('\033[32mFelizmente, Doug não precisou de cura.\033[m')

                        if noelle_life is False:
                            print('\033[33mNoelle recuperou suas forças!\033[m')
                            noelle_life = True
                            ms_noelle = 0
                            characters.append('Noelle')

                        if noelle_atri['Vida'] != noelle_atri_backup['Vida']:
                            cura = random.choice((25, 26, 27, 28, 29, 30))

                            noelle_atri['Energia'] = noelle_atri_backup['Energia']

                            if noelle_atri['Vida'] + cura > noelle_atri_backup['Vida']:
                                cura = noelle_atri_backup['Vida'] - noelle_atri['Vida']
                                noelle_atri['Vida'] += cura

                                sleep(1)
                                print(f'\033[32mVocê curou \033[31m{cura}\033[32m da \033[31mVida\033[32m de Noelle!\033[m')
                            else:
                                noelle_atri['Vida'] += cura
                                sleep(1)
                                print(f'\033[32mVocê curou \033[31m{cura}\033[32m da \033[31mVida\033[32m de Noelle!\033[m')

                        else:
                            sleep(1)
                            print('\033[32mFelizmente, Noelle não precisou de cura.\033[m')

                        special_shield = True
                        sleep(2)
                        print('\n\033[32mSua magia transborda, curando seus companheiros')
                        sleep(1)
                        print('O inimigo não pode te tocar com tanta energia vazando de você.')
                        sleep(1)
                        print('Você está protegido por uma rodada.\033[m')

            # PARA DESATIVAR ESCUDO CASO ESTEJA ATIVADO ─────────────────────────────────────────
            if shield is True:
                rodada_shield += 1
                if rodada_shield > 2:
                    shield = False
                    sleep(1)
                    print('\033[31mSeu escudo é desativado.\033[m')
                    rodada_shield = 0

            # CASO SEJA A VEZ DA NOELLE ────────────────────────────────────────────────────────────────
            if noelle is True:
                if rodada == 2 and noelle_life is True:
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
                elif rodada == 2 and noelle_life is False:
                    sleep(1)
                    print('\033[31mNoelle não consegue atacar mais. Ela passa a rodada.')
                    rodada += 1

            # CASO SEJA A VEZ DE DOUG ────────────────────────────────────────────────────────
            if doug is True:
                if rodada == 3 and doug_life is True:
                    frases_doug = ('\033[32mHan, o cavalo de Doug, acerta o monstro com um coice\033[m',
                                   f'\033[32mDoug acerta o {nome_monstro} consecutivamente com a espada.\033[m',
                                   '\033[32mDoug puxa uma segunda espada e corta a criatura em um X.\033[m',
                                   '\033[32mDoug joga o escudo no monstro, que volta como um boomerang.\033[m')

                    frase_dg = random.choice(frases_doug)

                    sleep(1)
                    print('\033[32mÉ a vez de Doug!\033[m\n')

                    possib = random.choice(chance)
                    if possib == 2 or possib == 7:
                        sleep(2)
                        print('\033[31mDoug tenta atacar o monstro, porém erra.\033[m')
                    else:
                        if possib == 1 or possib == 3 or possib == 6:
                            vida_monstro -= dano_doug + doug_atri['Critico']
                            sleep(2)
                            print(frase_dg)
                            sleep(1)
                            print('\033[32mDano crítico!\033[m')
                        else:
                            vida_monstro -= dano_doug
                            sleep(2)
                            print(frase_dg)

                # CASO DOUG TENHA DESMAIADO ───────────────────────────────────────────────────────
                elif rodada == 3 and doug_life is False:
                    sleep(1)
                    print('\033[31mDoug não consegue atacar mais. Ele passa a rodada.')
                    rodada += 1
                    continue

            sleep(1)
            print(end='\n')

            # PARA MONSTRO ATACAR ──────────────────────────────────────────────────────────────
            if vida_monstro > 0:
                possib = random.choice(chance)
                atacar = random.choice(characters)

                if possib not in hit_chance:
                    if atacar == perso_info['Nome']:
                        sleep(1)
                        print(f'\033[32m{nome_monstro} tenta atacar você, mas erra.\033[m')
                    else:
                        sleep(1)
                        print(f'\033[32m{nome_monstro} tenta atacar {atacar}, mas erra.\033[m')

                else:
                    if atacar == perso_info['Nome']:
                        sleep(1)
                        print(f'\033[31m{nome_monstro} ataca você.\033[m')

                        if at_esp is True:
                            bonus_ea = random.choice((1, 2))
                            if amount_ea != 36:
                                if amount_ea + bonus_ea > 36:
                                    r_ea = 36 - amount_ea
                                    amount_ea += r_ea
                                else:
                                    amount_ea += bonus_ea

                        if shield is True:
                            sleep(1)
                            print('\033[32mMas o escudo protege vocês.\033[m')

                        elif special_shield is True:
                            sleep(1)
                            print('\033[32mSua magia protege você.\033[m')

                        else:
                            if dano_monstro > attributes['Vida']:
                                dm = attributes['Vida']
                                attributes['Vida'] -= dm
                                sleep(1)
                                print(f'\033[32mVocê perde {dm} de \033[31mVida\033[m')
                            else:
                                attributes['Vida'] = attributes['Vida'] - dano_monstro
                                sleep(1)
                                print(f'\033[32mVocê perde {dano_monstro} de \033[31mVida\033[m')
                    else:
                        sleep(1)
                        print(f'\033[31m{nome_monstro} ataca {atacar}.')

                        if shield is True:
                            sleep(1)
                            print('\033[32mMas o escudo protege vocês.\033[m')
                        else:
                            if atacar == noelle_atri['Nome']:
                                noelle_atri['Vida'] = noelle_atri['Vida'] - round(
                                    ataque_monstro * (100 / (100 + noelle_atri['Defesa'])))
                            elif atacar == doug_atri['Nome']:
                                doug_atri['Vida'] = doug_atri['Vida'] - round(
                                    ataque_monstro * (100 / (100 + doug_atri['Defesa'])))

            rodada += 1

        while True:
            try_again = input('Você quer lutar novamente? [S/N] ').upper().strip()
            if try_again not in 'SN':
                sleep(1)
                print('Oh não... Tente novamente.')
            else:
                break

        if try_again == 'S':
            if noelle is True:
                noelle_atri = noelle_atri_backup.copy()
            if doug is True:
                doug_atri = doug_atri_backup.copy()

            attributes = witcher_atri_backup.copy()
            vida_monstro = vida_monstro_backup
        else:
            return False
