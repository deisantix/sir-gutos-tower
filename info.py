from time import sleep
from os import path
import random

doug_atri = {'Nome': 'Doug', 'Vida': 50, 'Ataque': 35, 'Defesa': 110, 'Escudo': 55, 'Han': 60, 'Energia': 30, 'Critico': 10}
noelle_atri = {'Nome': 'Noelle', 'Vida': 75, 'Ataque': 35, 'Defesa': 15, 'Flecha': 5, 'Energia': 30, 'Critico': 20}
gustav_atri = {'Nome': 'Gustav', 'Vida': 50, 'Ataque': 5, 'Defesa': 10, 'Magia': 35, 'Energia': 210, 'Critico': 15}

txt = ''
tempo = 20
deaths = 0
perso_info = {}
attributes = {}
inventario = {}
achievements = {}

itens = {'Barrinha Protein': {'Quantidade': 1, 'Descricao': 'Parece uma boa fonte de Energia, e um ótimo petisco...',
                              'Usavel': 'S', 'Efeito': 35, 'Onde': 'E'},
         'Papel Misterioso': {'Quantidade': 1, 'Descricao': 'Há uma frase apagada no papel, o que será que significa?',
                              'Usavel': 'N', 'Efeito': 'S/N', 'Onde': ''},
         'Cogumelo Vermelho': {'Quantidade': 1, 'Descricao': 'Não é muito apetitoso, mas é uma boa fonte de Energia',
                               'Usavel': 'S', 'Efeito': 35, 'Onde': 'E'}
         }

conquistas = {
    'Que a magia esteja com você': 'Jogue com o Feiticeiro',
    'Um por todos e todos por um': 'Jogue com o Cavalheiro',
    'Mira certeira': 'Jogue com o Arqueiro',
    'Má decisão': 'Morra pela primeira vez',
    'Péssima sorte': 'Morra cinco vezes',
    'A curiosidade matou o gato': 'Morra dez vezes',
    'Masoquista': 'Morra vinte vezes',
    'Caminho impossível': 'Encontre o Sir Dragon',
    'Um peso a mais': 'Desbloqueie o inventário',
    'O que esperar?': 'Entre na Torre',
    'O Cavalheiro': 'Tenha Doug no seu grupo',
    'A Arqueira': 'Tenha Noelle no seu grupo',
    'O Feiticeiro': 'Tenha Gustav no seu grupo',
    'Até que a morte nos separe': 'Perca um companheiro',
    'Sorte ou habilidade?': 'Derrote o Ogro Guardião sem perder Gustav no meio da batalha',
    'Últimos passos': 'Chegue no último Ato',
    'Sacrifícios necessários': 'Escolha você mesmo',
    'Quebra de realidade': 'Escolha salvar todos os personagens ao mesmo tempo'
            }


# FUNÇÃO PARA VERIFICAR SAVE
def ver_save():
    file1_exists = path.isfile('.info')
    file2_exists = path.isfile('.save')

    if file1_exists:
        filesize = path.getsize('.info')
    else:
        filesize = 0

    global txt
    txt = ''

    if not file1_exists or not file2_exists or filesize < 2:
        save = open('.info', 'a+')
        save_2 = open('.save', 'a+')

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
    print('\033[33m[1] NORMAL (Recomendado)')
    print('[2] RÁPIDO')
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


# FLEXIONAR GENERO NO TEXTO
def flexao_genero_textos(linha_a_modificar):
    # SUBSTITUIR POR NOME
    if '{NOME}' in linha_a_modificar:
        linha_a_modificar = linha_a_modificar.replace('{NOME}', perso_info['Nome'])

    # PALAVRAS QUE EM MASCULINO TEM "o" NO FINAL
    if '{a}' in linha_a_modificar:
        if perso_info['Genero'] == 'M':
            linha_a_modificar = linha_a_modificar.replace('{a}', 'o')
        else:
            linha_a_modificar = linha_a_modificar.replace('{a}', 'a')

    # PALAVRAS QUE EM MASCULINO TERMINAM COM "e"
    if '{e}' in linha_a_modificar:
        if perso_info['Genero'] == 'M':
            linha_a_modificar = linha_a_modificar.replace('{e}', 'e')
        else:
            linha_a_modificar = linha_a_modificar.replace('{e}', 'a')

    # PALAVRAS QUE NO MASCULINO NÃO TERMINAM COM NADA
    if '{ae}' in linha_a_modificar:
        if perso_info['Genero'] == 'M':
            linha_a_modificar = linha_a_modificar.replace('{ae}', '')
        else:
            linha_a_modificar = linha_a_modificar.replace('{ae}', 'a')

    return linha_a_modificar


# FUNÇÃO DE JUNTAR FRASES PARA A NARRATIVA
def juntar_frases_narrativa(comeco, arquivo):
    with open(arquivo) as file:
        dia = file.readlines()

        nar = []
        sleep(1)
        print('')

        for linha in range(len(dia)):
            dia[linha] = dia[linha].strip()

            if dia[linha][:len(comeco)] == comeco:
                if dia[linha] == '':
                    break

                nar.append(dia[linha][len(comeco) + 1:])

    return nar


# FUNÇÃO DE NARRATIVA
def narrativa(comeco, arquivo):
    nar = juntar_frases_narrativa(comeco, arquivo)

    for linha in nar:
        linha_modificada = flexao_genero_textos(linha)

        if tempo == 0:
            seg = 0
        else:
            seg = round(len(linha_modificada) / tempo)

        print(f'\033[32m{linha_modificada}')
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
            arquivo = 'pov_knight'

            with open('.info', 'a') as save:
                save.write('Classe: Cavalheiro\n')
                save.write('Arquivo: pov_knight\n')

            print('Você escolheu \033[37mCavalheiro\033[m!')
            sleep(2)
            break

        # OPÇÃO 3
        elif classe == '3':
            perso_info['Classe'] = 'Arqueiro'
            arquivo = 'pov_archer'

            with open('.info', 'a') as save:
                save.write('Classe: Arqueiro\n')
                save.write('Arquivo: pov_archer\n')

            print('Você escolheu \033[33mArqueiro\033[m!')
            sleep(2)
            break

        # OPÇÃO 4 ─ EXPLICAÇÃO
        elif classe == '4':
            while True:
                narrativa('classes.', '.help')

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
    global attributes

    if perso_info['Classe'] == 'Feiticeiro':
        attributes = {'Vida': 50, 'Ataque': 5, 'Defesa': 10, 'Magia': 35, 'Energia': 210, 'Critico': 15}
    elif perso_info['Classe'] == 'Cavalheiro':
        attributes = {'Vida': 50, 'Ataque': 35, 'Defesa': 110, 'Han': 60, 'Escudo': 55, 'Energia': 30, 'Critico': 10}
    elif perso_info['Classe'] == 'Arqueiro':
        attributes = {'Vida': 75, 'Ataque': 35, 'Defesa': 15, 'Flecha': 5, 'Energia': 30, 'Critico': 20}


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
        elif d == 'Flecha':
            print(f'\033[33m{d:<7}\033[m: {attributes[d]:>0}')
        elif d == 'Energia':
            print(f'\033[95m{d:<7}\033[m: {attributes[d]:>0}')
        elif d == 'Critico':
            continue


# DELETAR ITEM NO ARQUIVO DO SAVE
def delet_item_inve(key):
    # DIMINUIR QUANTIDADE CASO FOR MAIS DE UM MESMO ITEM ────────────────────────────
    if inventario[key]['Quantidade'] > 1:
        with open('.save', 'r+') as save:
            list_l = save.readlines()

            for line in list_l:
                if key in line:
                    psc = list_l[3].find(key)
                    old_nmbr = int(list_l[2][psc + len(key)])

                    nmbr = old_nmbr - 1
                    old_nmbr = str(old_nmbr)
                    nmbr = str(nmbr)

                    listnew = list_l[3].replace(key+old_nmbr, key+nmbr)
                    list_l[3] = listnew

                    save = open('.save', 'w')
                    save.writelines(list_l)

    # # EXCLUIR ITEM DO INVENTARIO CASO SEJA APENAS UM ───────────────────────────────
    else:
        with open('.save') as save:
            list_l = save.readlines()

            for line in list_l:
                if key in line:
                    listnew = list_l[3].replace(key+'1, ', '')
                    list_l[3] = listnew

                    save = open('.save', 'w')
                    save.writelines(list_l)


# FUNÇÃO PARA VER INVENTÁRIO FORMATADO:
def show_inve():
    global inventario

    sleep(1)
    mapear = {}

    # SE INVENTÁRIO ESTIVER VAZIO ─────────────────────────────────────────────────────────────────
    if inventario == {}:
        print('\033[37mSeu inventário está vazio...\033[m')

    # CASO NÃO ESTEJA VAZIO ───────────────────────────────────────────────────────────────────────
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

                if inventario[decision]['Usavel'] == 'S':
                    while True:
                        sleep(1)
                        decisao = input('\nDeseja usar este item? [S/N] ').upper().strip()
                        if decisao not in 'SN':
                            sleep(1)
                            print('\033[31mNão é uma opção.\033[m')

                        else:
                            break

                else:
                    sleep(1)
                    print('\n\033[31mEsse item não é usável.\033[m')
                    continue

                # CASO NÃO QUEIRA USAR O ITEM ────────────────────────────────────────────
                if decisao == 'N':
                    return False

                # CASO USE O ITEM ───────────────────────────────────────────────────────
                else:
                    if inventario[decision]['Onde'] == 'E':
                        attributes['Energia'] += inventario[decision]['Efeito']

                        sleep(1)
                        print(f'\033[32mVocê usou \033[33m{decision}\033[32m!')
                        sleep(1)
                        print(f'Sua \033[95mEnergia\033[32m aumentou \033[31m{inventario[decision]["Efeito"]}\033[32m!\033[m\n')
                        sleep(1)

                        if inventario[decision]['Quantidade'] > 1:
                            inventario[decision]['Quantidade'] -= 1

                        elif inventario[decision]['Quantidade'] == 1:
                            del inventario[decision]
                        break


            elif decision in 'N':
                return False

            else:
                sleep(1)
                print('\033[31mNão é uma opção.\033[m')


# FUNÇÃO PARA TOMAR DECISÕES
def make_decision(escolhas, pergunta='O que você vai fazer?'):  # ESCOLHAS SEPARADOS POR '_'
    escolhas = escolhas.split('_')

    options = ''
    for i in range(1, len(escolhas) + 1):
        options += str(i)

    with open('.save') as save:
        file = save.read()
        if 'Inventario: True' in file:
            invent = True
        else:
            invent = False

    escolhas.append('VER ATRIBUTOS')
    options = options + str(len(options) + 1)

    if invent:
        escolhas.append('ABRIR INVENTÁRIO')
        options = options + str(len(options) + 1)

    while True:
        sleep(1)
        print()
        for n in range(len(escolhas)):
            pare = escolhas[n].find('-')

            if pare != -1:
                r_pare = escolhas[n].rfind('E')

                try:
                    energy = abs(int(escolhas[n][pare:r_pare]))
                except ValueError:
                    energy = None

            else:
                energy = None

            if energy is None:
                print(f'\033[33m[{n + 1}] {escolhas[n]}')
            elif energy is not None and attributes['Energia'] >= energy:
                print(f'\033[33m[{n + 1}] {escolhas[n][:pare - 1]}\033[36m(-{energy} E)')
            else:
                print(f'\033[31m[{n + 1}] {escolhas[n][:pare - 1]}\033[31m(-{energy} E)')

        dc = input(f'\n\033[m{pergunta} ').strip()
        if dc not in options or dc == '':
            sleep(1)
            print('\033[31mNão é uma opção.\033[m\n')
            continue

        if not invent:

            # VER attributes
            if dc == options[-1]:
                show_atri()
                continue
            else:
                break

        elif invent:

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
    global attributes

    if perso_info['Classe'] == 'Feiticeiro':
        attributes['Vida'], attributes['Energia'] = 50, 210

    elif perso_info['Classe'] == 'Cavalheiro':
        attributes['Vida'], attributes['Energia'] = 50, 50

    elif perso_info['Classe'] == 'Arqueiro':
        attributes['Vida'], attributes['Energia'] = 75, 50


# SALVAR ATRIBUTOS NO .SAVE
def save_atri():
    modi_file('Atributos\n', '.save', 7)

    for pos, k in enumerate(attributes):
        modi_file(f'{k}: {attributes[k]}\n', '.save', pos+8)


# ADICIONAR ITEM AO INVENTÁRIO DO JOGADOR
def add_inve(key, mode='add'):
    global inventario

    if mode == 'add':
        inventario[key] = itens[key]

    elif mode == 'm':
        with open('.save') as save:
            save = save.read()

            if key in save:
                return None
            elif key in inventario:
                modi_file(f' {key}{inventario[key]["Quantidade"]},', '.save', 3, 'a')


# SALVAR CONQUISTAS NO .INFO E PEGÁ-LAS DE VOLTA CASO PRECISE
def achieve(conquis):
    global achievements

    with open('.conq') as inform:
        file = inform.read()
        if conquis in file:
            return None

    if conquis in conquistas:
        modi_file(f' {conquis},', '.conq', 0, 'a')
        achievements[conquis] = conquistas[conquis]


def show_achieve():
    with open('.conq') as save:
        inform = save.read()
        if 'conquistas' in inform:

            for key in conquistas:
                if key in inform:
                    x = achievements.get(key, 0)

                    if x == 0:
                        achievements[key] = conquistas[key]

    print(f'\n\033[93m{"CONQUISTAS ":─<40}\033[m')
    sleep(1)
    for k in achievements:
        print(f'\033[93m{k}\033[m: \033[32m{achievements[k]}\033[m')

    tm = len(conquistas)
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

    if dth:
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
        modi_file('Mortes: 1\n', '.info', 4)
        deaths = 1

    if deaths == 1:
        achieve('Má decisão')
    elif deaths == 5:
        achieve('Péssima sorte')
    elif deaths == 10:
        achieve('A curiosidade matou o gato')
    elif deaths == 20:
        achieve('Masoquista')


# SETAR ATRIBUTOS PELO ARQUIVO
def setar_atri():
    with open('.save') as save:
        atri = save.readlines()

        for line in range(len(atri)):

            for k in attributes:
                if k in atri[line]:
                    value = int(atri[line][len(k)+1:])
                    attributes[k] = value


# SETAR INVENTARIO PELO ARQUIVO
def setar_inve():
    global inventario

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


# MENSAGEM DE MORTE
def mensagem_morte(forma_da_morte):
    death_count()

    forma_da_morte_modificada = flexao_genero_textos(forma_da_morte)

    sleep(1)
    print(f'\n\033[32m{forma_da_morte_modificada}\033[m')
    sleep(2)
    print(f'\033[31m{" VOCÊ PERDEU ":─^40}\033[m')


# FUNÇÕES GERAIS DO SISTEMA DE LUTA

# VERIFICAR ACCURACY ─
def verifica_accuracy(accuracy_rate):
    chance = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10)

    hit_chance = []

    count = 10 - accuracy_rate
    while count > 0:
        x = random.choice(chance)

        if x in hit_chance:
            continue

        hit_chance.append(x)

        count -= 1

    return chance, hit_chance


# MODIFICAR RODADA PARA QUE O FLUXO DO JOGO CONTINUE NORMAL ─
def modificar_rodada(rodada, vez2, vez3):
    if vez2 and vez3:
        if rodada == 4:
            rodada = 1

    elif vez2:
        if rodada == 3:
            rodada = 1

    elif vez3:
        if rodada == 2:
            rodada = 3
        elif rodada == 4:
            rodada = 1

    else:
        if rodada == 2:
            rodada = 1

    return rodada


# IMPRIMIR BARRINHA DE ATAQUE ESPECIAL ─
def imprimir_amount_ea(amount_ea):
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


# SE NÃO TIVER ENERGIA O SUFICIENTE PARA O ATAQUE ─
def if_not_enough_energy(limit):
    if attributes['Energia'] < limit:
        sleep(1)
        print(f'\n\033[31mVocê não tem energia suficiente para essa ação.\033[m')

    return attributes['Energia'] < limit


# MODIFICAR LISTA DE ATAQUE ANTERIOR ─
def modifi_ataque_anterior_list(decision_to_add, ataque_anterior_lista):
    ataque_anterior_lista.append(decision_to_add)

    if len(ataque_anterior_lista) > 2:
        ataque_anterior_lista.pop(0)

    return ataque_anterior_lista


# MODIFICAR O AMOUNT_EA QUANDO FAZER ALGUM MOVIMENTO ─
def ganhar_bonus_ea(amount_ea, pontos):
    bonus_ea = random.choice(pontos)

    if amount_ea != 36:
        if (amount_ea + bonus_ea) > 36:
            bonus_ea = (36 - amount_ea)

        return bonus_ea

    else:
        return 0


# MENSAGEM DE ALIADO DERROTADO ─
def mensagem_aliado_derrotado(nome_aliado):
    nome_aliado = nome_aliado.upper()

    art = 'e'
    if nome_aliado == 'NOELLE':
        art = 'a'

    sleep(1)
    print(f'\033[31mA VIDA DE {nome_aliado} CHEGOU A \033[33m0\033[m')
    sleep(1)
    print(f'\033[32mEl{art} não atacará mais durante a luta.\033[m')


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
