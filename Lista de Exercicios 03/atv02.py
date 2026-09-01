# Crie uma lista vazia. Utilize for com range(5) para pedir cinco produtos ao usuário e adicionar
# cada um com append() . Ao final, exiba a lista completa e a quantidade de produtos cadastrados.

produtos = []

for i in range (5):
    produto = input(f"Informe o {i+1}º produto: ")
    produtos.append(produto)
    
qtd = len(produtos)

print("\nProdutos informados:")
print(produtos)
print(f"\nQuantidade de produtos informada foi {qtd}.")