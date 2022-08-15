from time import sleep

achievements = {}
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


# MOSTRAR CONQUISTAS NA TELA
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
    print(f'{tm_nw} de {tm} alcançadas')

