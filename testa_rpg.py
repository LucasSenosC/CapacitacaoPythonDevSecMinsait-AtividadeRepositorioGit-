from servivo import SerVivo
from personagem import Personagem
from monstro import Monstro
from lobo import Lobo
from goblin import Goblin

personagem = Personagem(pontos_de_vida=100, pontos_de_ataque=20, nome="Herói")

goblin = Goblin(pontos_de_vida=50, pontos_de_ataque=10, tipo="Goblin", inteligencia=5)

print("Antes do ataque")
print(f"{personagem.nome}: {personagem.pontos_de_vida} pontos de vida")
print(f"{goblin.tipo}: {goblin.pontos_de_vida} pontos de vida")

goblin.atacar(personagem)

print("Depois do ataque")
# exibindo os pontos de vida depois do ataque
print(f"{personagem.nome}: {personagem.pontos_de_vida} pontos de vida")
print(f"{goblin.tipo}: {goblin.pontos_de_vida} pontos de vida")
