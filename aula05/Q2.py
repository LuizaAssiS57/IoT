import os
os.system("cls")

# 2) O Somador Infinito (while True + append)
# Crie um programa que peça números ao usuário indefinidamente.
# Se o usuário digitar 0, o programa para.
# Cada número digitado (exceto o 0) deve ser guardado em uma lista.
# No final, mostre a lista completa e a soma de todos os itens usando sum().

numeros = []

while True:
    num = int(input("Digite o número: "))
    
    if (num != 0):
        numeros.append(num)
    else:
        break
    
soma = sum(numeros)

print("\n======== SOMADOR INFINITO =========")
print(f"A soma de todos os números digitados é {soma}")
print(f"Os números ditados foram: {numeros}")