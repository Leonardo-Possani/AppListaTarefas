import json
from pathlib import Path

ARQUIVO = Path("data.json")

def load_tasks():
    #Carrega as tarefas do arquivo JSON
    if ARQUIVO.exists():
        try:
            with open(ARQUIVO, "r", encoding="utf-8") as f:

                return json.load(f)

        except json.JSONDecodeError:
                # Se o arquivo estiver vazio ou inválido, volta com lista vazia
            return []

    return [] # se o arquivo não existir, começa vazio


def save_tasks(tarefas):
    # Salva as tarefas no arquivo JSON

    with open(ARQUIVO, "w", encoding="utf-8") as f:
        json.dump(tarefas, f, indent=4, ensure_ascii=False)
