import os, time
os.system("cls")

while True:
    try:
        numero = int(input("Informe um número: "))
        
        print("********** TABUADA ***********")
        for i in range(11):
            i+1
            print(f"{numero} x {i} = {numero * i}")
            print("******************************")
        break
    except:
        print("Entrada inválida!")
        time.sleep(1)