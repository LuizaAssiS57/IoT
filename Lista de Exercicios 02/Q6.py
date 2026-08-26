# 6) Filtragem e Média de Dados (Processamento de Vetores)
# Enunciado: Desenvolva um programa que peça ao usuário para digitar a nota de 8
# alunos e armazene-as em uma lista. O programa deve:
# 1. Calcular e mostrar a média aritmética da turma.
# 2. Criar e exibir uma nova lista contendo apenas as notas que ficaram acima
# da média calculada.

notas = []

for i in range(8):
    n = float(input(f"Digite a {i+1}ª nota: "))
    notas.append(n)
    
media = sum(notas) / len(notas)

for espiao in notas:
    if (espiao >= media):
        print(espiao, end="-")
        
print(f"\nA média da turma é {media:.1f}")