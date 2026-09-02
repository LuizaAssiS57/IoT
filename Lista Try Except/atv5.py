import os, time
os.system("cls")

while True:
    try:
        saldo = float(input("Digite seu saldo: "))
        saque = float(input("Digite o valor do saque: "))
        
        if (saque > saldo):
            print("Saldo insuficiente!")
            break
        else:
            valorRes = saldo - saque
            print("Saque realizado com sucesso!")
            print(f"Saldo restante: {valorRes:.2f}")
            break
    
    except:
        print("Digite apenas valores numéricos!")
        time.sleep(1)