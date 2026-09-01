# Crie uma lista vazia e apresente continuamente o menu: 1 - Adicionar tarefa, 2 - Remover tarefa,
# 3 - Mostrar tarefas e 0 - Sair. Use w h i l e T r u e para manter o menu ativo, append() para
# adicionar, remove() para retirar e break para encerrar.

tarefas = []

while True:
    print("_-_--_ MENU DE TAREFAS _-_--_")
    print("1 - Adicionar tarefa")
    print("2 - Remover tarefa")
    print("3 - Mostrar tarefas")
    print("0 - Sair")
    op = int(input("ESCOLHA UMA OPÇÃO: "))
    
    match op:
        case 1:
            tarefa = input("Informe a tarefa: ")
            tarefas.append(tarefa)
            print("Tarefa adicionada com sucesso!")
        case 2:
            remover = input("Informe a tarefa para remover: ")
            for i in range(len(tarefas)-1):
                if (len(tarefas) == 0):
                    print("Nenhuma tarefa!")
                else:
                    tarefas.remove(remover)
                    print("Tarefa removida com sucesso!")
        case 3:
            if (len(tarefas) == 0):
                print("Nenhuma tarefa!")
            else:
                for i in range(len(tarefas)):
                    print(tarefas[i])
        case 0:
            print("Saindo...")
            break
        case _:
            print("Opção inválida!")
            break