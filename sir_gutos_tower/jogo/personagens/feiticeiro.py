class Feiticeiro:

    def __init__(self):
        self.nome = 'Gustav'
        self.init_atributos()


    def init_atributos(self):
        self.vida = 50
        self.ataque = 5
        self.defesa = 10
        self.magia = 35
        self.energia = 210
        self.critico = 15


    def executar_acao(self, energia_gasta):
        self.energia -= energia_gasta


    def usar_magia(self):
        pass


    def ativar_escudo(self):
        pass


    def atacar_com_cajado(self):
        pass


    def usar_especial(self):
        pass


    def __str__(self):
        return f"Vida: {self.vida}\nAtaque: {self.ataque}\nDefesa: {self.defesa}\nMagia: {self.magia}\nEnergia: {self.energia}"
