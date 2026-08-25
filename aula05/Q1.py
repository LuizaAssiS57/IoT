import os
os.system("cls")

# 1) Peça ao usuário para digitar 5 temperaturas (uma por uma) e guarde-as em uma lista.
# Use um laço para a entrada de dados.
# Após a leitura, exiba:
# A maior temperatura registrada (max).
# A menor temperatura registrada (min).
# A média das temperaturas.

temperaturas = []

for i in range(5):
    temp = float(input(f"Digite a {i+1}ª temperatura: "))
    temperaturas.append(temp)
    
media = sum(temperaturas) / len(temperaturas)
menor = min(temperaturas)
maior = max(temperaturas)

print("\n================= TEMPERATURAS ==================")
print(f"A maior temperatura do dia foi {maior}°C ")
print(f"A menor temperatura do dia foi {menor}°C ")
print(f"A média de temperatura do dia foi {media:.1f}°C ")
