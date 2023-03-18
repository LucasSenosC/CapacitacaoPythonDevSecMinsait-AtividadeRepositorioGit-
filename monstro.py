from servivo import SerVivo

class Monstro(SerVivo):
    def __init__(self, pontos_de_vida, pontos_de_ataque, tipo):
        super().__init__(pontos_de_vida, pontos_de_ataque)
        self.tipo = tipo

    def atacar(self, personagem):
        personagem.pontos_de_vida -= self.pontos_de_ataque