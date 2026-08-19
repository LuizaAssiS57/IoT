numeros = [33,11,22,54,51,52,17,33]
nomes = ["Julia", "Maria", "Luiza", "Enzo"]

#append - Insere um novo valor no vetor, sempre na ultima posição
numeros.append(67)

#insert - Insere um novo valor na posição desejada
numeros.insert(3,50)

#pop - Deleta um valor pela sua posição
numeros.pop(0)

#remove - Deleta um valor pelo seu conteudo
numeros.remove(54)
nomes.remove("Enzo")

print(nomes)
#sort - Ordena o vetor
numeros.sort()

#reverse - Inverte as posições do vetor
numeros.reverse()
print(numeros)

#len - Informar quantos valores existem dentro de um vetor
quantidade = len(numeros)
print(f"A quantidade de números é {quantidade}")

#Count - Informa a quantidade de um valor especifico
quantidade = nomes.count("Luiza")
print(f"A quantidade de números é {quantidade}")

#sum() - Soma todos os valores de um vetor
total = sum(numeros)
print(f"A soma de todos os valores é {total}")

#max - min - 
maior = max(numeros)
menor = min(numeros)
print(f"O maior é {maior} e o menor é {menor}")