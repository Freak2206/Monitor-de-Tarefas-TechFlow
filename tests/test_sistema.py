import pytest
import sys, os
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src")))
from app import Sistema


def test_registro_e_login():
    sistema = Sistema()
    sistema.registrar_usuario("Felipe", "felipe@email.com", "1234")
    sistema.login("felipe@email.com", "1234")
    assert sistema.usuario_logado.email == "felipe@email.com"

def test_adicionar_tarefa():
    sistema = Sistema()
    sistema.registrar_usuario("Felipe", "felipe@email.com", "1234")
    sistema.login("felipe@email.com", "1234")
    sistema.adicionar_tarefa("Teste", "Descrição", "Alta", "Pendente")
    tarefas = sistema.listar_tarefas()
    assert len(tarefas) == 1
    assert tarefas[0]["titulo"] == "Teste"

def test_editar_tarefa():
    sistema = Sistema()
    sistema.registrar_usuario("Felipe", "felipe@email.com", "1234")
    sistema.login("felipe@email.com", "1234")
    sistema.adicionar_tarefa("Teste", "Descrição", "Alta", "Pendente")
    sistema.editar_tarefa("Teste", "Novo Título", "Nova Desc", "Baixa", "Concluída")
    tarefas = sistema.listar_tarefas()
    assert tarefas[0]["titulo"] == "Novo Título"
    assert tarefas[0]["status"] == "Concluída"

def test_remover_tarefa():
    sistema = Sistema()
    sistema.registrar_usuario("Felipe", "felipe@email.com", "1234")
    sistema.login("felipe@email.com", "1234")
    sistema.adicionar_tarefa("Teste", "Descrição", "Alta", "Pendente")
    sistema.remover_tarefa("Teste")
    tarefas = sistema.listar_tarefas()
    assert len(tarefas) == 0
