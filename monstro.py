from servivo import SerVivo

class Monstro(SerVivo):
    def __init__(self, pontos_de_vida, pontos_de_ataque, tipo):
        super().__init__(pontos_de_vida, pontos_de_ataque)
        self.tipo: str = tipo

    # Ataque de um monstro a um outro ser vivo
    # Subtrai os pontos de ataque de um ser vivo A dos pontos de vida de um outro ser vivo B
    def atacar(self, personagem):
        personagem.pontos_de_vida -= self.pontos_de_ataque
