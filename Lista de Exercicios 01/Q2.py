import os
os.system("cls")

# 2. Escreva um programa que peça ao usuário
# para inserir sua idade. O programa deve
# classificar a pessoa em uma das seguintes
# categorias: "Criança" (0-12 anos),
# "Adolescente" (13-17 anos), "Adulto" (18-59
# anos), ou "Idoso" (60 anos ou mais).

idade = int(input("Informe a idade: "))

if idade <= 12:
    print("Criança")
elif idade < 18:
    print("Adolescente")
elif idade < 60:
    print("Adulto")
else:
    print("Idoso")