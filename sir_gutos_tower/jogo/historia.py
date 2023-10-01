from ..utils.exceptions.exceptions import ComportamentoInesperadoError


class Historia:
    INICIO = 'intro'
    PASSO = 'historia'
    TEXTO = 'texto'
    DECISOES = 'decisoes'

    def __init__(self, pov):
        self._pov = pov
        self._trecho = None
        self._passo = None

    @property
    def passo(self) -> dict:
        return self._passo

    @passo.setter
    def passo(self, novo_passo: dict):
        self._passo = novo_passo

    @property
    def texto(self) -> list:
        try:
            return self._passo[Historia.TEXTO]
        except KeyError:
            return []

    @property
    def decisoes(self) -> dict | bool:
        try:
            return self._passo[Historia.DECISOES]
        except KeyError:
            return False

    @property
    def proximo_ato(self) -> bool:
        if type(self._trecho) == dict:
            return False
        elif type(self._trecho) == str:
            return True
        else:
            raise ComportamentoInesperadoError()

    def iniciar(self, ato: str = None) -> None:
        if ato:
            self._trecho = self._pov[ato]
        else:
            self._trecho = self._pov[Historia.INICIO]
        self._passo = self._trecho[Historia.PASSO]

    def ir_para_proximo_ato(self):
        if self.proximo_ato:
            nome_proximo_ato = self._trecho
            self.iniciar(nome_proximo_ato)
