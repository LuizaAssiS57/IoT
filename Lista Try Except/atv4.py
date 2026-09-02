import os, time
os.system("cls")

notas = []

while True:
    try:
        notas.clear()
        for i in range(3):
            nota = float(input(f"Informe a {i+1}ª nota: "))
            notas.append(nota)
            
            
        media = sum(notas) / len(notas)
            
        if (media >= 7):
            situacao = "Aprovado"
        elif (media < 5):
            situacao = "Reprovado"
        else:
            situacao = "Recuperação"
                
        print("\n========= BOLETIM ==========")
        print(f"\nMédia: {media:.2f}")
        print(f"Situação: {situacao}")
        break
    except:
        print("Digite apenas números!")
        time.sleep(1)