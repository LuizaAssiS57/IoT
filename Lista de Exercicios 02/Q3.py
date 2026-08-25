import os
os.system("cls")

# 3) Escreva um programa que leia uma lista de 5 nomes e depois exiba esses
# nomes em ordem alfabética.

nomes = []

for i in range(5):
    nome = input(f"Informe o {i+1}º nome: ")
    nomes.append(nome)
    
nomes.sort()
print("+++++++ NOMES EM ORDEM ALFABÉTICA =======")
print(f"{nomes}")