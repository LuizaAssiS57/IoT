import random, os

# 2) Crie um programa em Python que lê uma lista de 10 nomes e sorteia um
# nome entre eles.

nomes = []

for i in range (10):
    nome = input(f"Digite o {i+1}º nome: ")
    nomes.append(nome)
    os.system("cls" or "clear")
    
sortudo = random.choice(nomes)

print(f"Você {sortudo} foi o sorteado!")