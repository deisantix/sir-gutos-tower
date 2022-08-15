from time import sleep

inventario = {}

itens = {
    'Barrinha Protein': {
        'Quantidade': 1, 
        'Descricao': 'Parece uma boa fonte de Energia, e um ótimo petisco...',
        'Usavel': 'S', 
        'Efeito': 35, 
        'Onde': 'E'
    },
    'Cogumelo Vermelho': {
        'Quantidade': 1, 
        'Descricao': 'Não é muito apetitoso, mas é uma boa fonte de Energia',
        'Usavel': 'S', 
        'Efeito': 35, 
        'Onde': 'E'
    }
}

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
