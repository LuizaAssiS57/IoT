import os
os.system("cls")

# 4. *Questão 4:* Defina duas variáveis, a e b, com valores inteiros. Use uma estrutura
# condicional para verificar se a é maior que b. Se for, imprima "A é maior que B", caso contrário,
# imprima "B é maior ou igual a A".

a = int(input("Informe o 1º número: "))
b = int(input("Informe o 2º número: "))

if a > b:
    print("A é maior que B")
elif a < b:
    print("B é maior que A")
else:
    print("Os números são iguais")
    