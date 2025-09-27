import tkinter as tk
import tasks # aqui importamos as funções e a lista

def atualizar_lista():

    # Recarrega ListBox a partir da lista 'Tarefas' em memória
    lista.delete(0, tk.END) # limpa todos os itens da listbox
    for i, tarefa in enumerate(tasks.listar(), start=1):               
        lista.insert(tk.END, f"{i}. {tarefa["nome"]} - {tarefa["status"]}")
        
def adicionar_tarefa():

    nome = entrada.get().strip()
    if nome:
        tasks.adicionar(nome)
        atualizar_lista()
        entrada.delete(0, tk.END)
  
def remover_tarefa():

    selecao = lista.curselection()
    if selecao:
        tasks.remover(selecao[0])
        atualizar_lista()

def concluir_tarefa():

    selecao = lista.curselection()
    if selecao:
        tasks.concluir(selecao[0])
        atualizar_lista()
        

# -------  Interface Gráfica

janela = tk.Tk()
janela.title("Lista de Tarefas")

entrada = tk.Entry(janela, width=30)
entrada.pack(pady=10)

tk.Button(janela, text="Adicionar", command=adicionar_tarefa).pack(pady=5)
tk.Button(janela, text="Concluir", command=concluir_tarefa).pack(pady=5)
tk.Button(janela, text="Remover", command=remover_tarefa).pack(pady=5)

lista = tk.Listbox(janela, width=50, height=15)
lista.pack(pady=10)

atualizar_lista()

janela.mainloop()


        
