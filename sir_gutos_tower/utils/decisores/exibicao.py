from ...config.var import GASTO_MISTERIOSO, ATAQUE_ESPECIAL
from ...jogo.decisores.decisao import Decisao


def definir_gasto_energia(decisao: Decisao):
    try:
        energia = decisao.energia
        if energia == ATAQUE_ESPECIAL:
            return '(-AE)'
        elif energia == GASTO_MISTERIOSO:
            energia = '?'

        return f'(-{energia} E)'
    except AttributeError:
        return ''
