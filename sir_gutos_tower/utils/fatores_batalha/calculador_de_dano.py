from random import randrange


def calcular_dano(ataque_atacante, defesa_vitima):
    return round(ataque_atacante * (100 / (100 + defesa_vitima)))


def calcular_precisao(precisao, margem_erro):
    def nao_ha_mais_margem_erro():
        return False not in precisao_ataque

    def definir_casa_acerto_aleatoria():
        return randrange(0, len(precisao_ataque))

    def casa_acerto_ja_foi_alterada(casa_acerto):
        return precisao_ataque[casa_acerto]

    def alterar_casa_acerto(casa_acerto):
        precisao_ataque[casa_acerto] = True

    precisao_ataque = [False for i in range(margem_erro)]

    i = 0
    while i < precisao:
        if nao_ha_mais_margem_erro():
            break
        casa_acerto = definir_casa_acerto_aleatoria()

        if casa_acerto_ja_foi_alterada(casa_acerto):
            continue
        else:
            i += 1

        alterar_casa_acerto(casa_acerto)
    return precisao_ataque


if __name__ == '__main__':
    print(calcular_precisao(10, 15))
