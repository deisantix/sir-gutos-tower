from time import sleep

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

                    newline = inform[4].replace(f'Mortes: {old_number}\n', f'Mortes: {deaths}\n')
                    inform[4] = newline

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


# MENSAGEM DE MORTE
def mensagem_morte(forma_da_morte):
    death_count()

    forma_da_morte_modificada = flexao_genero_textos(forma_da_morte)

    sleep(1)
    print(f'\n\033[32m{forma_da_morte_modificada}\033[m')
    sleep(2)
    print(f'\033[31m{" VOCÊ PERDEU ":─^40}\033[m')
