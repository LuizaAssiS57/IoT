import os
os.system("cls")

# 1) Crie um programa que lê uma lista de 10 números e conta a quantidade de números positivos e a quantidade de números negativos, e mostra o vetor com os negativos e o a soma dos positivos?

negativos = []
positivos = []

for i in range (10):
    num = int(input(f"Informe o {i+1}º número: "))
    
    if (num > 0):
        positivos.append(num)
    elif (num < 0):
        negativos.append(num)
    else:
        print("0")
        
qtd_positivo = len(positivos)
qtd_negativo = len(negativos)
soma = sum(positivos)

print(f"A quantidade de números positivos é: {qtd_positivo}")
print(f"A quantidade de números negativos é: {qtd_negativo}")
print(f"Os números negativos informados foram: {negativos}")
print(f"A soma dos números positivos é: {soma}")
