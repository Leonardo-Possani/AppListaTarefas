# Lista de Tarefas em Python 📝

Um aplicativo simples de **lista de tarefas** desenvolvido em **Python 3** com interface gráfica em **PySide6** e armazenamento de dados em **JSON**.  

Permite adicionar, remover e marcar tarefas como concluídas, com persistência automática.

---

## 🛠 Tecnologias Utilizadas

- Python 3.13+
- PySide6 (Interface Gráfica)
- JSON (Persistência de dados)

---

## 💡 Funcionalidades

- Adicionar novas tarefas
- Marcar tarefas como concluídas
- Remover tarefas
- Lista de tarefas armazenada no arquivo `tarefas.json`
- Interface gráfica intuitiva

---

## 🚀 Como Rodar o Projeto

1. **Clone o repositório:**

```bash
git clone https://github.com/seu-usuario/lista-tarefas.git
cd lista-tarefas
```

## Arch Linux / WSL Arch:

```bash
sudo pacman -S Pyside6
```
## Ubuntu / WSL Ubuntu:
```bash
sudo apt update
sudo apt install python3-tk
```

## Execute o aplicativo:
```bash
python3 app.py
```

## 🗂 Estrutura do Projeto
```bash
AppListaTarefas/
│── app.py        # Interface gráfica
│── tarefas_model.py      # Lógica de tarefas (adicionar, remover, concluir)Persistência em JSON (salvar e carregar tarefas)
    │── json/
       │── tarefas.json     # Arquivo de armazenamento das tarefas
│── README.md     # Documentação do projeto
```

---

## 📝 Como Funciona

- 1 Ao iniciar, o programa carrega as tarefas do data.json.

- 2 Para adicionar uma tarefa:

  - Digite o nome no campo de entrada.
  
  - Clique em Adicionar.
  
- 3 Para concluir ou remover:

  - Selecione a tarefa na lista.
  
  - Clique em Concluir ou Remover.
  
- 4 Todas as alterações são salvas automaticamente no arquivo JSON.

---

## 🔧 Melhorias Futuras

- Filtrar tarefas por status (pendentes/concluídas)

- Confirmação antes de remover tarefas

- Suporte a múltiplos usuários

- Interface mais moderna usando Kivy ou PyQt

- Trocar JSON por SQLite ou outro banco de dados

---
