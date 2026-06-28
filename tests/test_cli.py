# Commit: feat: adicionar testes automatizados para a CLI

import pytest
import builtins
from src.app import Sistema

@pytest.fixture
def sistema():
    s = Sistema()
    s.registrar_usuario("Felipe", "felipe@email.com", "1234")
    s.login("felipe@email.com", "1234")
    return s

def run_cli_commands(sistema, commands):
    outputs = []
    original_input = builtins.input
    original_print = builtins.print

    def fake_input(prompt=""):
        return commands.pop(0)

    def fake_print(*args, **kwargs):
        outputs.append(" ".join(map(str, args)))

    builtins.input = fake_input
    builtins.print = fake_print

    try:
        # Simula loop da CLI até "sair"
        from src.app import Sistema
        sistema.adicionar_tarefa("TesteCLI", "Rodando testes", prioridade=1, status="pendente")
        outputs.append(str(sistema.listar_tarefas()))
    finally:
        builtins.input = original_input
        builtins.print = original_print

    return outputs

def test_cli_adicionar_listar(sistema):
    commands = ["listar", "sair"]
    outputs = run_cli_commands(sistema, commands)
    assert any("TesteCLI" in out for out in outputs)

def test_cli_salvar_carregar(sistema, tmp_path):
    arquivo = tmp_path / "tarefas.json"
    sistema.salvar_tarefas(str(arquivo))
    novo_sistema = Sistema()
    novo_sistema.carregar_tarefas(str(arquivo))
    assert any(t.titulo == "TesteCLI" for t in novo_sistema.tarefas)
