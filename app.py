import sys

from PySide6.QtWidgets import (
        
    QApplication, QMainWindow, QWidget, QVBoxLayout, QHBoxLayout, QPushButton, QLineEdit, QListView, QMessageBox, QInputDialog
        
)
from PySide6.QtCore import Qt
from PySide6.QtGui import QStandardItemModel, QStandardItem, QColor

from tarefas_model import TarefasModel




class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        # config Mainwindow (Janela principal)
        self.setWindowTitle("Lista tarefas")
        self.setMinimumSize(750,450)
        


        # Modelo de dados
        self.modelo_dados = TarefasModel()

        # Modelo visual (para QListView)
        self.modelo_visual = QStandardItemModel()

        #  ---- botoes ----
        self.btn_add = QPushButton("Adicionar")
        self.btn_edit = QPushButton("Editar")
        self.btn_remove = QPushButton("Remover")
        self.btn_done = QPushButton("Concluir / Reabrir")
        
        # ----- entrada da lista -----
        self.input_tarefa = QLineEdit()
        self.input_tarefa.setPlaceholderText("Digite uma nova tarefas")
    
        #  ----- Lista -----

        # Lista principal a esquerda
        self.lista  = QListView()
        self.lista.setModel(self.modelo_visual)
        
        # Lista 

        # Layout
        layout_principal = QVBoxLayout()
        layout_botoes = QHBoxLayout()       
        
        layout_botoes.addWidget(self.btn_add)
        layout_botoes.addWidget(self.btn_edit)
        layout_botoes.addWidget(self.btn_remove)
        layout_botoes.addWidget(self.btn_done)
              
        
        # add widgets / layouts a janela principal
        layout_principal.addLayout(layout_botoes)
        layout_principal.addWidget(self.input_tarefa)
        layout_principal.addWidget(self.lista)


        # Container principal
        container = QWidget()
        container.setLayout(layout_principal)
        self.setCentralWidget(container)



        # Conectar eventos
    
        self.btn_add.clicked.connect(self.add_tarefa)
        self.btn_remove.clicked.connect(self.remove_tarefa)
        self.btn_done.clicked.connect(self.done_tarefa)
        self.btn_edit.clicked.connect(self.edit_tarefa)
    
        # Carrega as tarefas salvas
        self.atualizar_lista()

       


    # ----- Disparo de eventos -----

    def atualizar_lista(self):
        # --- Atualiza a QListView com as tarefas ---
        self.modelo_visual.clear()
        for tarefa in self.modelo_dados.tarefas:
            texto = tarefa["texto"]
            status = tarefa["status"]
            criado = tarefa["criado_em"]
            concluido = tarefa["concluido_em"]

            # monta o texto completo da linha
            if status == "Concluída":
                texto_final = f"{texto} | ✅  {status.upper()} ({concluido})"
                cor = "gray"
            
            else:
                texto_final = f"{texto} | ⏳ {status.upper()} (Criado: {criado})"
                cor = "black"


            item = QStandardItem(texto_final)
            item.setForeground(QColor(cor))
            self.modelo_visual.appendRow(item)



    def add_tarefa(self):
        texto = self.input_tarefa.text().strip()
        if texto:
            self.modelo_dados.adicionar_tarefa(texto)
            self.input_tarefa.clear()
            self.atualizar_lista()
        
        else:
            QMessageBox.warning(self, "Aviso", "Digite uma tarefa antes de adícionar")
            
    def remove_tarefa(self):
        indice = self.lista.currentIndex().row()
        if indice >= 0:
            self.modelo_dados.remover_tarefa(indice)
            self.atualizar_lista()
        else:
            QMessageBox.warning(self, "Aviso", "Selecione uma tarefa para remover.")
            

    def done_tarefa(self):
        indice = self.lista.currentIndex().row()
        if indice >= 0:
            self.modelo_dados.alternar_status(indice)
            self.atualizar_lista()
        else:
            QMessageBox.warning(self, "Aviso", "Selecione uma tarefa primeiro!")
 

    def edit_tarefa(self):
        indice = self.lista.currentIndex().row()
        if indice < 0:
            QMessageBox.warning(self, "Aviso", "Selecione uma tarefa para editar.")
            return
        tarefa_atual = self.modelo_dados.tarefas[indice]["texto"]

        # Abre o diálogo de texto

        novo_texto, ok = QInputDialog.getText(
               self, "Editar tarefa", "Novo texto", text=tarefa_atual
               )
        if ok and novo_texto.strip():
            # passa o novo texto para o modelo
            self.modelo_dados.edit_tarefa(indice, novo_texto)
            self.atualizar_lista()








if __name__ == "__main__":
    app = QApplication(sys.argv)
    janela = MainWindow()
    janela.show()
    app.exec()
