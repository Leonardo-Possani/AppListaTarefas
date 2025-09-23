# Exibe o menu

def show_menu():
    print("\nMenu Lista de Tarefas.")
    print("\n- 1 - Adicionar uma nova tarefa")
    print("- 2 - Listar tarefas")
    print("- 3 - Marcar tarefas como concluidas")
    print("- 4 - Remover tarefas")
    print("- 0 - Sair...")


# Adiciona uma nova tarefa

def add_task(tarefas):
    nome = input("\nDigite a nova tarefa: ").strip()
    if not nome:
        print("Nome de tarefa vazio - tarefa não adicionada.")
        return
    tarefa = {"nome": nome, "status": "Pendente"}
    tarefas.append(tarefa)
    print("\nTarefa adicionada com sucesso ! ")


# Listar itens da lista 

def list_tasks(tarefas):
    if not tarefas: # equivalente a len(tarefas) == 0
        print("Lista vazia")
        return
    print("\nTarefas:")
    for i, tarefa in enumerate(tarefas, start=1):
        print(f"{i}. {tarefa['nome']} - {tarefa['status']}")


'''
Mostra a lista (se houver) e pede que o usuário digite um número 
retornao índice 0-based da tarefa escolhida ou None se inválido

'''

def choose_task_index(tarefas, action="selecionar"):
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
        return None
    
    list_tasks(tarefas) # reaproveita a função que já imprime a lista
    entrada = input(f"Digite o número da tarefa a {action}:").strip()
    if not entrada.isdigit():
        print("Por favor digite um número.")
        return None
    numero = int(entrada)
    if 1 <= numero <= len(tarefas):
        return numero - 1 # converte para índice 0-based
    else:
        print("Número inválido.")
        return None

    
# Marca a tarefa como concluida usando a função choose_task_index() para recuperar o index

def mark_task_completed(tarefas):
    idx = choose_task_index(tarefas, action="marcar como concluída")
    if idx is None:
        return
    if tarefas[idx]["status"] == "concluída":
        print(f"Tarefa '{tarefas[idx]['nome']}' já está concluída.")
    else:
        tarefas[idx]["status"] = "concluída"
        print(f"tarefa '{tarefas[idx]['nome']}' marcada como comcluída.")


# função que remove itens da lista usando choose_task_index para recuperar o index

def remove_task(tarefas):
    idx = choose_task_index(tarefas, action="remover")
    if idx is None:
        return
    nome = tarefas[idx]["nome"]
    del tarefas[idx]
    print(f"Tarefa '{nome}' removida.")
    

# Função principal

def main():

    tarefas = []

    while True:
        show_menu()
        opcao = input("\nDigite uma opção: ")

        if opcao == "0":
            print("Saindo...")
            break
        
        elif opcao == "1":
             add_task(tarefas)           
        
        elif opcao == "2":
            list_tasks(tarefas)

        elif opcao == "3":
            mark_task_completed(tarefas)

        elif opcao == "4":
            remove_task(tarefas)



# Assim que o aquivo listaTarefas.py for executado chama a função main()

if __name__ == "__main__":
    main()
