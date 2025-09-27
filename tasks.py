def add_task(tarefas, nome):
    tarefas.append({"nome": nome, "status": "Pendente"})

def list_tasks(tarefas):
    if not tarefas:
        print("Nenhuma tarefa encontrada.")
    else:
        print("\nTarefas:")
        for i, tarefa in enumerate(tarefas, start=1):
            print(f"{i}. {tarefa['nome']} - {tarefa['status']}")

def complete_task(tarefas, indice):
    tarefas[indice]["status"] = "Concluída"

def remove_task(tarefas, indice):
    del tarefas[indice]

