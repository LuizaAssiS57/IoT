# Crie uma lista vazia. Use w h i l e T r u e para cadastrar notas até que o usuário digite -1 . Depois do
# encerramento, utilize um for para mostrar cada nota cadastrada. Exiba também a quantidade, a
# média, a maior nota, a menor nota e as notas em ordem decrescente.

notas = []
qtd = 0

while True:
    qtd += 1
    nota = float(input(f"Informe a {qtd}ª nota: "))
    
    if nota == -1:
        print("Saindo...")
        break
    else:
        notas.append(nota)
        
notas.sort()
notas.reverse()
media = sum(notas) / len(notas)

print("TABELA")
for i in range(len(notas)):
    print(notas[i])
    
print(f"Quantidade: {len(notas)}")
print(f"Média: {media:.1f}")
print(f"Maior: {max(notas)}")
print(f"Menor: {min(notas)}")
print(f"Ordem decrescente: {notas}")