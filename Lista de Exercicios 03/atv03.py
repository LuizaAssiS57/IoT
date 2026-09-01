# Peça seis números inteiros utilizando um laço for e armazene-os em uma lista. Depois, mostre a
# soma, o maior valor, o menor valor e os números em ordem crescente.

numeros = []

for i in range (6):
    numero = int(input(f"Informe o {i+1}º número: "))
    numeros.append(numero)
    
soma = sum(numeros)
maior = max(numeros)
menor = min(numeros)
numeros.sort()

print(f"A soma é: {soma}")
print(f"O maior número informado é: {maior}")
print(f"O menor número informado é: {menor}")
print(f"Números em ordem crescente: {numeros}")