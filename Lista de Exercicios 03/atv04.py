# Use a lista n u m e r o s = [ 1 2 , 7 , 9 , 2 0 , 3 1 , 4 4 , 1 8 , 5 ] . Percorra os valores com for e conte
# quantos são pares e quantos são ímpares. Mostre as duas quantidades ao final.

numeros = [12 , 7 , 9 , 20 , 31 , 44 , 18 , 5 ]

par = 0
impar = 0

qtd = len(numeros)

for i in range (qtd):
    if (numeros[i] %2 == 0):
        par += 1
    else:
        impar += 1
        
print("\n==== Números par ====")
print(par)
print("\n==== Números impar ====")
print(impar)