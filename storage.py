import json
from pathlib import Path

ARQUIVO = Path("data.json")

def load_tasks():
    #Carrega as tarefas do aquivo .Json
    if ARQUIVO.exists():
        with open(ARQUIVO, "r", encoding="utf-8") as f:
            return json.load(f)
    return [] #se não existir, comela com lista vazia

def save_tasks(tarefas):
    #Salva as tarefas no arquivo .Json
    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)


