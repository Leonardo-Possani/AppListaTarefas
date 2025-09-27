from storage import load_tasks, save_tasks

# Carrega os dados na inicialização
tarefas = load_tasks()

def listar():
    return tarefas

def adicionar(nome):
    tarefas.append({"nome": nome, "status": "Pendente"})
    save_tasks(tarefas)

def concluir(indice):
    tarefas[indice]["status"] = "Concluída"
    save_tasks(tarefas)

def remover(indice):
    tarefas.pop(indice)
    save_tasks(tarefas)
    
    
