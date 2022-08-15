from time import sleep
import random

# VERIFICAR ACCURACY
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


# MODIFICAR RODADA PARA QUE O FLUXO DO JOGO CONTINUE NORMAL
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


# IMPRIMIR BARRINHA DE ATAQUE ESPECIAL
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


# SE NÃO TIVER ENERGIA O SUFICIENTE PARA O ATAQUE
def if_not_enough_energy(limit):
    if attributes['Energia'] < limit:
        sleep(1)
        print(f'\n\033[31mVocê não tem energia suficiente para essa ação.\033[m')

    return attributes['Energia'] < limit


# MODIFICAR LISTA DE ATAQUE ANTERIOR
def modifi_ataque_anterior_list(decision_to_add, ataque_anterior_lista):
    ataque_anterior_lista.append(decision_to_add)

    if len(ataque_anterior_lista) > 2:
        ataque_anterior_lista.pop(0)

    return ataque_anterior_lista


# MODIFICAR O AMOUNT_EA QUANDO FAZER ALGUM MOVIMENTO
def ganhar_bonus_ea(amount_ea, pontos):
    bonus_ea = random.choice(pontos)

    if amount_ea != 36:
        if (amount_ea + bonus_ea) > 36:
            bonus_ea = (36 - amount_ea)

        return bonus_ea

    else:
        return 0


# MENSAGEM DE ALIADO DERROTADO
def mensagem_aliado_derrotado(nome_aliado):
    nome_aliado = nome_aliado.upper()

    art = 'e'
    if nome_aliado == 'NOELLE':
        art = 'a'

    sleep(1)
    print(f'\033[31mA VIDA DE {nome_aliado} CHEGOU A \033[33m0\033[m')
    sleep(1)
    print(f'\033[32mEl{art} não atacará mais durante a luta.\033[m')
