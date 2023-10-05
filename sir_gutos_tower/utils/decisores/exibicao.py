from ...config.var import GASTO_MISTERIOSO, ATAQUE_ESPECIAL


def definir_gasto_energia(detalhes):
    try:
        energia = detalhes['energia']

        if energia == ATAQUE_ESPECIAL:
            return '(-AE)'
        elif energia == GASTO_MISTERIOSO:
            energia = '?'

        return f'(-{energia} E)'
    except KeyError:
        return ''
