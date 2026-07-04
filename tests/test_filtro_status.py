from sistema_class import Sistema
import pytest
import sys
import os

# Garante que a pasta src está no caminho
import sys
import os

sys.path.insert(
    0, os.path.abspath(os.path.join(os.path.dirname(__file__), "..", "src"))
)


def test_filtro_status():
    sistema = Sistema()
    sistema.registrar_usuario("Felipe", "felipe@email.com", "1234")
    sistema.login("felipe@email.com", "1234")

    # Adiciona duas tarefas com status diferentes
    sistema.adicionar_tarefa("Tarefa 1", "Desc 1", "Alta", "Pendente")
    sistema.adicionar_tarefa("Tarefa 2", "Desc 2", "Baixa", "Concluída")

    # Filtra apenas as pendentes
    tarefas_pendentes = [
        t for t in sistema.listar_tarefas() if t["status"] == "Pendente"
    ]
    assert len(tarefas_pendentes) == 1
    assert tarefas_pendentes[0]["titulo"] == "Tarefa 1"

    # Filtra apenas as concluídas
    tarefas_concluidas = [
        t for t in sistema.listar_tarefas() if t["status"] == "Concluída"
    ]
    assert len(tarefas_concluidas) == 1
    assert tarefas_concluidas[0]["titulo"] == "Tarefa 2"
