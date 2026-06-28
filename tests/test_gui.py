# Commit: feat: adicionar testes automatizados para a GUI

import pytest
import tkinter as tk
from src.gui import AppGUI

@pytest.fixture
def app():
    root = tk.Tk()
    app = AppGUI(root)
    yield app
    root.destroy()

def test_login_sucesso(app):
    app.entry_email.insert(0, "felipe@email.com")
    app.entry_senha.insert(0, "1234")
    app.sistema.registrar_usuario("Felipe", "felipe@email.com", "1234")
    app.login()
    assert app.sistema.usuario_logado is not None

def test_adicionar_tarefa(app):
    app.sistema.registrar_usuario("Felipe", "felipe@email.com", "1234")
    app.sistema.login("felipe@email.com", "1234")

    app.entry_titulo.insert(0, "TarefaGUI")
    app.entry_desc.insert(0, "Teste via GUI")
    app.entry_prioridade.insert(0, "1")
    app.entry_status.insert(0, "pendente")

    app.adicionar_tarefa()
    tarefas = app.sistema.listar_tarefas()
    assert any(t[0] == "TarefaGUI" for t in tarefas)
