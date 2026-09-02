import os
os.system("cls")

while True:
    try:
        a = int(input("Digite o primeiro número: "))
        b = int(input("Digite o segundo número: "))
        soma = a + b
        
        print("\n+++++++ RESULTADO +++++++")
        print(f"{a} + {b} = {soma}")
        print("+++++++++++++++++++++++++++")
        break
    except:
        print("Dado inválido, somente números!")