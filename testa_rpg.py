from servivo import SerVivo
from personagem import Personagem
from monstro import Monstro
from lobo import Lobo
from goblin import Goblin

personagem = Personagem(pontos_de_vida=100, pontos_de_ataque=20, nome="Herói")
goblin = Goblin(pontos_de_vida=50, pontos_de_ataque=10, tipo="Goblin", inteligencia=5)

print("Início")
print(f"{personagem.nome}: {personagem.pontos_de_vida} pontos de vida, {personagem.pontos_de_ataque} pontos de ataque")
print(f"{goblin.tipo}: {goblin.pontos_de_vida} pontos de vida, {goblin.pontos_de_ataque} pontos de ataque")

goblin.atacar(personagem)
print("Depois do ataque do goblin")
print(f"{personagem.nome}: {personagem.pontos_de_vida} pontos de vida, {personagem.pontos_de_ataque} pontos de ataque")
print(f"{goblin.tipo}: {goblin.pontos_de_vida} pontos de vida, {goblin.pontos_de_ataque} pontos de ataque")

personagem.cura(valor_da_cura=5)
print("Depois da cura do heroi")
print(f"{personagem.nome}: {personagem.pontos_de_vida} pontos de vida, {personagem.pontos_de_ataque} pontos de ataque")
print(f"{goblin.tipo}: {goblin.pontos_de_vida} pontos de vida, {goblin.pontos_de_ataque} pontos de ataque")

personagem.elixir(tipo="vida", valor=20)
print("Depois do elixir de vida no personagem")
print(f"{personagem.nome}: {personagem.pontos_de_vida} pontos de vida, {personagem.pontos_de_ataque} pontos de ataque")
print(f"{goblin.tipo}: {goblin.pontos_de_vida} pontos de vida, {goblin.pontos_de_ataque} pontos de ataque")

goblin.elixir(tipo="ataque", valor=40)
print("Depois do elixir de ataque no goblin")
print(f"{personagem.nome}: {personagem.pontos_de_vida} pontos de vida, {personagem.pontos_de_ataque} pontos de ataque")
print(f"{goblin.tipo}: {goblin.pontos_de_vida} pontos de vida, {goblin.pontos_de_ataque} pontos de ataque")

goblin.atacar(personagem)
print("Depois do ataque melhorado do goblin")
print(f"{personagem.nome}: {personagem.pontos_de_vida} pontos de vida, {personagem.pontos_de_ataque} pontos de ataque")
print(f"{goblin.tipo}: {goblin.pontos_de_vida} pontos de vida, {goblin.pontos_de_ataque} pontos de ataque")
