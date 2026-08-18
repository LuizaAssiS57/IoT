import os
os.system("cls")

# 8. Crie um programa que peça ao usuário para inserir dois números e uma operação (adição,
# subtração, multiplicação ou divisão). Realize a operação solicitada e exiba o resultado.

a = float(input("Informe o 1º número: "))
b = float(input("Informe o 2º número: "))
operador = input("Informe a operação: ")

if operador == "+":
    resultado = a + b
    print(f"{a} + {b} = {resultado:.2f}")
elif operador == "-":
    resultado = a - b
    print(f"{a} + {b} = {resultado:.2f}")
elif operador == "*":
    resultado = a * b
    print(f"{a} + {b} = {resultado:.2f}")
elif operador == "/":
    if a == 0:
        print("Divisão por 0, escolha outro número!")
    elif b == 0:
        print("Divisão por 0, escolha outro número!")
    else:
        resultado = a / b
        print(f"{a} + {b} = {resultado:.2f}")
else:
    print("Operação inválida!")
