from storage import load_tasks, save_tasks
from tasks import add_task, list_tasks, complete_task, remove_task

def main():
    tarefas = load_tasks()  # carrega ao iniciar

    while True:
        print("\n--- Gerenciador de Tarefas ---")
        print("1. Adicionar tarefa")
        print("2. Listar tarefas")
        print("3. Marcar tarefa como concluída")
        print("4. Remover tarefa")
        print("0. Sair")

        opcao = input("Escolha uma opção: ")

        if opcao == "1":
            nome = input("Digite o nome da tarefa: ")
            add_task(tarefas, nome)
            save_tasks(tarefas)

        elif opcao == "2":
            list_tasks(tarefas)

        elif opcao == "3":
            list_tasks(tarefas)
            numero = int(input("Digite o número da tarefa: ")) - 1
            if 0 <= numero < len(tarefas):
                complete_task(tarefas, numero)
                save_tasks(tarefas)

        elif opcao == "4":
            list_tasks(tarefas)
            numero = int(input("Digite o número da tarefa: ")) - 1
            if 0 <= numero < len(tarefas):
                remove_task(tarefas, numero)
                save_tasks(tarefas)

        elif opcao == "0":
            print("Saindo...")
            break

        else:
            print("Opção inválida!")

if __name__ == "__main__":
    main()

