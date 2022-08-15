from time import sleep

# FUNÇÃO PARA DEFINIR VELOCIDADE DE NARRATIVA
def velo_narrativa():
    global tempo

    while True:
        print('\n\033[mQUAL A VELOCIDADE QUE VOCÊ PREFERE O TEXTO?')
        print('\033[33m[1] NORMAL (Recomendado)')
        print('[2] RÁPIDO')
        print('[3] INSTANTÂNEO\033[m')
        sleep(1)

        escolha = input('Digite o número da velocidade: ')
        if not verifica_resposta(escolha, '123'):
            continue
        else:
            break

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
