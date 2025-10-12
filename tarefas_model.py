import json
from datetime import datetime
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
        agora = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.tarefas.append({
            "texto": texto,
            "status": "Pendente",
            "criado_em": agora,
            "concluido_em": None
                
        })
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
            if tarefa["status"] == "Pendente":
                tarefa["status"] = "Concluída"
                tarefa["concluido_em"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            else:
                tarefa["status"] = "Pendente"
                tarefa["concluido_em"] = None
        self.salvar_tarefas()

    def edit_tarefa(self, indice, novo_texto):
        # Atualiza o texto de uma tarefa existente
        if 0 <= indice < len(self.tarefas):
            self.tarefas[indice]["texto"] = novo_texto.strip()
            self.salvar_tarefas()


