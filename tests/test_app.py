import pytest
from src.app import Sistema

@pytest.fixture
def sistema():
    s = Sistema()
    s.registrar_usuario("Felipe", "felipe@email.com", "1234")
    s.login("felipe@email.com", "1234")
    return s

def test_adicionar_tarefa(sistema):
    tarefa = sistema.adicionar_tarefa("Estudar UML", "Fazer diagrama de casos de uso", prioridade=2)
    assert tarefa.titulo == "Estudar UML"
    assert tarefa.descricao == "Fazer diagrama de casos de uso"
    assert tarefa.prioridade == 2

def test_listar_tarefas(sistema):
    sistema.adicionar_tarefa("CRUD", "Criar operações básicas")
    lista = sistema.listar_tarefas()
    assert len(lista) == 1
    assert lista[0][0] == "CRUD"

def test_editar_tarefa(sistema):
    sistema.adicionar_tarefa("CRUD", "Criar operações básicas")
    sistema.editar_tarefa("CRUD", nova_descricao="Atualizar operações", novo_prioridade=3)
    lista = sistema.listar_tarefas()
    assert lista[0][1] == "Atualizar operações"
    assert lista[0][2] == 3

def test_remover_tarefa(sistema):
    sistema.adicionar_tarefa("CRUD", "Criar operações básicas")
    sistema.remover_tarefa("CRUD")
    lista = sistema.listar_tarefas()
    assert len(lista) == 0
