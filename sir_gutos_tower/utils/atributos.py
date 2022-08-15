from time import sleep

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


# SALVAR ATRIBUTOS NO .SAVE
def save_atri():
    modi_file('Atributos\n', '.save', 7)

    for pos, k in enumerate(attributes):
        modi_file(f'{k}: {attributes[k]}\n', '.save', pos+8)


# VOLTAR ATRIBUTOS PARA OS VALORES INICIAIS
def reset_atri():
    global attributes

    if perso_info['Classe'] == 'Feiticeiro':
        attributes['Vida'], attributes['Energia'] = 50, 210

    elif perso_info['Classe'] == 'Cavalheiro':
        attributes['Vida'], attributes['Energia'] = 50, 50

    elif perso_info['Classe'] == 'Arqueiro':
        attributes['Vida'], attributes['Energia'] = 75, 50


# SETAR ATRIBUTOS PELO ARQUIVO
def setar_atri():
    with open('.save') as save:
        atri = save.readlines()

        for line in range(len(atri)):

            for k in attributes:
                if k in atri[line]:
                    value = int(atri[line][len(k)+1:])
                    attributes[k] = value
