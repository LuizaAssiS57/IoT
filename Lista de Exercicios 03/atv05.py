# Crie uma lista vazia e utilize w h i l e T r u e para receber nomes. Cada nome deve ser incluído com
# append() . Quando o usuário digitar 'fim' , encerre com break . Depois, organize os nomes em
# ordem alfabética e mostre a lista e sua quantidade.

nomes = []

while True:
    print("+=+++++++ LISTA DE NOMES ++++++=+")
    nome = input("Informe um nome: ")
    nomes.append(nome)
    
    if (nome == "fim"):
        break
    
nomes.sort()
qtd = len(nomes)

print("\n=+====== NOMES EM ORDEM ALFABÉTICA ======+=")
print(nomes)
print("\n=+====== NOMES INFORMADOS ======+=")
print(nomes)
print("\n=+====== QUANTIDADE DE NOMES ======+=")
print(qtd)
