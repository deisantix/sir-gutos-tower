class Decisao:

    DECISAO_OBRIGATORIA = '0'

    def __init__(self, codigo: str, descricao: str, energia: int = None):
        self._codigo = codigo
        self._descricao = descricao

        if energia is not None:
            self._energia = energia

    @property
    def codigo(self):
        return self._codigo

    @property
    def descricao(self):
        return self._descricao

    @property
    def energia(self):
        return self._energia

    @property
    def decisao_obrigatoria(self):
        if self._codigo == Decisao.DECISAO_OBRIGATORIA:
            return True
        return False

    def __str__(self):
        return self._descricao
