import pytest
from src.app import Sistema

@pytest.fixture
def sistema():
    return Sistema()

def test_login_sucesso(sistema):
    sistema.registrar_usuario("Felipe", "felipe@email.com", "1234")
    assert sistema.login("felipe@email.com", "1234") is True
    assert sistema.usuario_logado is not None

def test_login_falha(sistema):
    sistema.registrar_usuario("Felipe", "felipe@email.com", "1234")
    assert sistema.login("felipe@email.com", "senha_errada") is False
    assert sistema.usuario_logado is None

def test_logout(sistema):
    sistema.registrar_usuario("Felipe", "felipe@email.com", "1234")
    sistema.login("felipe@email.com", "1234")
    sistema.logout()
    assert sistema.usuario_logado is None

def test_crud_sem_login(sistema):
    # Não loga usuário
    with pytest.raises(Exception) as e:
        sistema.adicionar_tarefa("Teste", "Tarefa sem login")
    assert "É necessário estar logado" in str(e.value)
