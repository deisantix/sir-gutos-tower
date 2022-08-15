from time import sleep

# CRIAR UMA LISTA COM AS OPÇÕES DE ESCOLHA
def criar_lista_com_escolhas(escolhas):  # ESCOLHAS SEPARADOS POR '_'
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

    return escolhas, options


# IMPRIMIR AS ESCOLHAS E OPÇÕES
def imprimir_escolhas(escolhas):
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


# FUNÇÃO PARA TOMAR DECISÕES
def make_decision(escolhas, pergunta='O que você vai fazer?'):
    escolhas_e_opcoes = criar_lista_com_escolhas(escolhas)
    options = escolhas_e_opcoes[1]

    invent = False
    with open('.save') as save:
        save = save.read()
        if 'Inventario: True' in save:
            invent = True

    while True:
        sleep(1)
        print('')
        imprimir_escolhas(escolhas_e_opcoes[0])

        dc = input(f'\n\033[m{pergunta} ').strip()
        if not verifica_resposta(dc, options):
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


# VERIFICAR RESPOSTA
def verifica_resposta(op, options):
    if (op not in options) or (op == ''):
        sleep(1)
        print('\033[31mNão é uma opção.\033[m')
        return False

    return True

