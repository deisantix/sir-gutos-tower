from utils.exceptions.exceptions import FimDeJogoError

def rodar_historia(historia):
    contar(historia['texto'])

    try:
        decisoes = historia['decisoes']
    except KeyError:
        return lidar_com_a_falta_de_decisoes(historia)

    imprimir_decisoes(decisoes)
    return tomar_decisao(decisoes)


def contar(texto):
    print()
    for linha in texto:
        print(linha)

    print()


def lidar_com_a_falta_de_decisoes(historia):
    fim = verificar_se_fim_de_jogo(historia)
    if fim:
        fim_de_jogo(historia)

    proximo_ato = verificar_se_existe_proximo_ato(historia)
    if proximo_ato:
        return proximo_ato

    raise NotImplementedError


def verificar_se_fim_de_jogo(historia):
    try:
        return historia['fim']

    except KeyError:
        return False


def fim_de_jogo(historia):
    print(historia['morte'])
    raise FimDeJogoError


def verificar_se_existe_proximo_ato(historia):
    try:
        return historia['proximo']

    except KeyError:
        return False


def imprimir_decisoes(decisoes):
    for decisao in decisoes:
        decisao_detalhes = decisoes[decisao]

        energia = decisao_detalhes['energia']
        if energia == -1:
            energia = '?'

        print(f'{decisao}) {decisao_detalhes["decisao"]} (-{energia} E)')


def tomar_decisao(decisoes):
    while True:
        escolha_usuario = input('O que você vai fazer? ')

        if escolha_usuario in decisoes:
            return decisoes[escolha_usuario]['historia']
        else:
            print('Decisão inválida. Escolha novamente.')
            continue
