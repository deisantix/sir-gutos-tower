from ..utils.exceptions.exceptions import ComportamentoInesperadoError


class Historia:

    INICIO = 'intro'
    PASSO = 'historia'
    TEXTO = 'texto'
    DECISOES = 'decisoes'
    COMBATE = 'combate'
    FIM = 'fim'
    MORTE = 'morte'
    PROXIMO = 'proximo'

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
    def combate(self) -> dict | bool:
        try:
            return self._passo[Historia.COMBATE]
        except KeyError:
            return False

    @property
    def fim(self) -> bool:
        try:
            return self._passo[Historia.FIM]
        except KeyError:
            return False

    @property
    def morte(self) -> str:
        try:
            return self._passo[Historia.MORTE]
        except KeyError:
            return ''

    @property
    def proximo_ato(self) -> bool:
        try:
            if self._passo[Historia.PROXIMO]:
                return True
        except KeyError:
            return False

    def iniciar(self, ato: str = None) -> None:
        if ato:
            self._trecho = self._pov[ato]
        else:
            self._trecho = self._pov[Historia.INICIO]
        self._passo = self._trecho[Historia.PASSO]

    def ir_para_proximo_ato(self):
        if self.proximo_ato:
            self.iniciar(self._passo[Historia.PROXIMO])
