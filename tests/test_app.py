import pytest
from src.app import Sistema

def test_criar_tarefa():
    sistema = Sistema()
    tarefa = sistema.adicionar_tarefa("Estudar UML", "Fazer diagrama de casos de uso")
    assert tarefa.titulo == "Estudar UML"
    assert tarefa.descricao == "Fazer diagrama de casos de uso"

def test_listar_tarefas():
    sistema = Sistema()
    sistema.adicionar_tarefa("Login", "Implementar login simples")
    lista = sistema.listar_tarefas()
    assert ("Login", "Implementar login simples", 0) in lista

def test_remover_tarefa():
    sistema = Sistema()
    sistema.adicionar_tarefa("Teste", "Remover tarefa")
    sistema.remover_tarefa("Teste")
    assert ("Teste", "Remover tarefa", 0) not in sistema.listar_tarefas()
