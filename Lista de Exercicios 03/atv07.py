# Gere um número aleatório entre 1 e 20. Em um w h i l e T r u e , peça palpites até que o usuário
# acerte. Informe se cada palpite foi maior ou menor que o número sorteado, conte as tentativas e
# encerre com break quando houver acerto.

import random

num_aleatorio = (1, 20)
tentativas = 0

while True:
    palpite = int(input("Digite um número entre 1 e 20: "))
    tentativas += 1
    
    if palpite < num_aleatorio:
        print("O número sorteado é maior.")
    elif palpite > num_aleatorio:
        print("O número sorteado é menor.")
    else:
        print(f"Parabens! Tu acertou o número {num_aleatorio}!")
        print(f"Tentativas {tentativas}")
        break