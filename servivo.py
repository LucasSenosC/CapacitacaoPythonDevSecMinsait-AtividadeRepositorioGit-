class SerVivo:  
    def __init__(self, pontos_de_vida, pontos_de_ataque):
        # Atributo extra.
        # pontos_de_vida_máxima é a vida máxima que esse ser vivo pode ter
        self.pontos_de_vida_maxima: int = pontos_de_vida
        self.pontos_de_vida: int = pontos_de_vida
        self.pontos_de_ataque: int = pontos_de_ataque
    
    # Ataque de um monstro a um outro ser vivo
    # Subtrai os pontos de ataque de um ser vivo A dos pontos de vida de um outro ser vivo B
    def atacar(self, outro_ser_vivo):
        outro_ser_vivo.pontos_de_vida -= self.pontos_de_ataque

    # Metodo extra.
    # O ser vivo pode achar uma cura e se curar um determinado valor
    # A cura é limitada aos pontos de vida máxima
    def cura(self, valor_da_cura):
        if self.pontos_de_vida + valor_da_cura <= self.pontos_de_vida_maxima:
            self.pontos_de_vida += valor_da_cura
        else:
            self.pontos_de_vida = self.pontos_de_vida_maxima
    
    # Metodo extra.
    # O ser vivo pode achar um elixir de vida ou ataque
    # O elixir de vida aumenda os pontos de vida máxima e completa a vida restante
    # O elixir de ataque aumenta os pontos de ataque do ser vivo
    def elixir(self, tipo, valor):
        if tipo == "vida":
            self.pontos_de_vida_maxima+= valor
            self.pontos_de_vida = self.pontos_de_vida_maxima
        if tipo == "ataque":
            self.pontos_de_ataque += valor
