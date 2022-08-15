from time import sleep
from os import path

# FUNÇÃO PARA VERIFICAR SAVE
def ver_save():
    file1_exists = path.isfile('.info')
    file2_exists = path.isfile('.save')

    if not file1_exists and not file2_exists:
        save = open('.info', 'a+')
        save_2 = open('.save', 'a+')

        save.close()
        save_2.close()

    else:
        while True:
            sleep(1)
            keep = input('Deseja resetar o save? [N/S] ').upper().strip()
            if verifica_resposta(keep, 'SN'):
                break

        if keep == 'S':
            apagar_save('.save', '.info', '.conq')
            with open('.conq', 'w') as conquists:
                conquists.write('conquistas:\n')


# APAGAR DE SAVE
def apagar_save(*args):
    for arg in args:
        existe = path.isfile(arg)
        if not existe:
            raise FileNotFoundError(f'{arg} não existe')

        with open(arg, 'w') as save:
            save.truncate(0)


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


# FUNÇÃO QUE DESIGNA TODAS AS CARACTERÍSTICAS INICIAIS DO PERSONAGEM PRINCIPAL
def caract():
    global perso_info

    with open('.info') as save:
        tamanho = path.getsize('.info')
        if tamanho > 1:
            save = save.readlines()

            for line in range(len(save)):
                caracteristica = save[line].split(':')
                perso_info[caracteristica[0]] = caracteristica[1].strip()

            if ('Classe' in perso_info) and ('Nome' in perso_info) and ('Genero' in perso_info) and ('Arquivo' in perso_info):
                skills()
                return perso_info['Arquivo']
            else:
                print('\033[31mARQUIVO DE PROGRESSO INCOMPLETO. REINICIANDO...\033[m')
                sleep(2)

                apagar_save('.save')
                ver_save()

    # GENERO ───────────────────────────────────────────────────────────────────────────────
    while True:
        sleep(1)
        genero = input('\nDigite seu gênero [M/F]: ').upper().strip()
        if not verifica_resposta(genero, 'MF'):
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
            if not verifica_resposta(assure, 'SN'):
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
        if not verifica_resposta(classe, '1234'):
            continue

        # OPÇÃO 4 ─ EXPLICAÇÃO
        if classe == '4':
            while True:
                narrativa('classes.', '.help')

                while True:
                    gotit = input('\n\033[mEntendeu? [S/N] ').upper().strip()
                    if not verifica_resposta(gotit, 'SN'):
                        continue
                    else:
                        break

                if gotit == 'N':
                    continue
                else:
                    break

        else:
            break

    # OPÇÃO 1
    if classe == '1':
        perso_info['Classe'] = 'Feiticeiro'
        perso_info['Arquivo'] = 'pov_witcher'

        with open('.info', 'a') as save:
            save.write('Classe: Feiticeiro\n')
            save.write('Arquivo: pov_witcher\n')

        print('Você escolheu \033[95mFeiticeiro\033[m!')
        sleep(2)

    # OPÇÃO 2
    elif classe == '2':
        perso_info['Classe'] = 'Cavalheiro'
        perso_info['Arquivo'] = 'pov_knight'

        with open('.info', 'a') as save:
            save.write('Classe: Cavalheiro\n')
            save.write('Arquivo: pov_knight\n')

        print('Você escolheu \033[37mCavalheiro\033[m!')
        sleep(2)

    # OPÇÃO 3
    elif classe == '3':
        perso_info['Classe'] = 'Arqueiro'
        perso_info['Arquivo'] = 'pov_archer'

        with open('.info', 'a') as save:
            save.write('Classe: Arqueiro\n')
            save.write('Arquivo: pov_archer\n')

        print('Você escolheu \033[33mArqueiro\033[m!')
        sleep(2)

    skills()
    return perso_info['Arquivo']
