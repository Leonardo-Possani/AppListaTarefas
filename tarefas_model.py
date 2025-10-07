import json
from pathlib import Path

class TarefasModel:
    def __init__(self, arquivo_json="tarefas.json"):
        base_dir = Path(__file__).resolve().parent # caminho de pasta do script
        self.arquivo = base_dir / "json" / arquivo_json
        self.tarefas = []
        self.carregar_tarefas()
    
    def carregar_tarefas(self):
        # --- Lê o arquivo JSON e carrega as tarefas ---
        if self.arquivo.exists():
            with open(self.arquivo, "r", encoding="utf-8") as f:
                self.tarefas = json.load(f)
                
        
        else:
            self.tarefas = []
    
    def salvar_tarefas(self):
        # --- Salva as tarefas no arquivo JSON ---
        with open(self.arquivo, "w", encoding="utf-8") as f:
            json.dump(self.tarefas, f, ensure_ascii=False, indent=4)
        
    def adicionar_tarefa(self, texto):
       
       # ---- Adicionar novas tarefas como pendente ----
        self.tarefas.append({"texto": texto, "status": "pendente"})
        self.salvar_tarefas()

    def remover_tarefa(self, indice):
        # ---- remover tarefa ----
        if 0 <= indice < len(self.tarefas):
            del self.tarefas[indice]
            self.salvar_tarefas()
 
    def alternar_status(self, indice):
        # --- marca tarefa como concluida/pendente ---
        if 0 <= indice < len(self.tarefas):
            tarefa = self.tarefas[indice]
            tarefa["status"] = (
                    "concluída" if tarefa["status"] == "pendente" else "pendente"
                    )
            self.salvar_tarefas()

    def edit_tarefa(self, indice, texto):
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice]["texto"] = texto.strip()            
            self.salvar_tarefas()

        
