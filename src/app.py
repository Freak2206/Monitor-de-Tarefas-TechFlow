# src/app.py
class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


class Tarefa:
    def __init__(self, titulo, descricao, prioridade, status="pendente", autor=None):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = status
        self.autor = autor


class Sistema:
    def __init__(self):
        self.usuarios = []
        self.tarefas = []
        self.usuario_logado = None

    # ---------------- Usuários ----------------
    def registrar_usuario(self, nome, email, senha):
        if any(u.email == email for u in self.usuarios):
            raise Exception("Usuário já existe")
        usuario = Usuario(nome, email, senha)
        self.usuarios.append(usuario)
        return usuario

    def login(self, email, senha):
        usuario = next((u for u in self.usuarios if u.email == email and u.senha == senha), None)
        if not usuario:
            raise Exception("Credenciais inválidas")
        self.usuario_logado = usuario
        return usuario

    def logout(self):
        self.usuario_logado = None

    # ---------------- Tarefas ----------------
    def adicionar_tarefa(self, titulo, descricao, prioridade, status="pendente"):
        if not self.usuario_logado:
            raise Exception("É necessário estar logado para adicionar tarefas")
        tarefa = Tarefa(titulo, descricao, prioridade, status, autor=self.usuario_logado.email)
        self.tarefas.append(tarefa)
        return tarefa

    def listar_tarefas(self):
        return [{
            "titulo": t.titulo,
            "descricao": t.descricao,
            "prioridade": t.prioridade,
            "status": t.status,
            "autor": t.autor
        } for t in self.tarefas]

    def editar_tarefa(self, titulo, novo_titulo=None, nova_descricao=None, nova_prioridade=None, novo_status=None):
        tarefa = next((t for t in self.tarefas if t.titulo == titulo), None)
        if not tarefa:
            raise Exception("Tarefa não encontrada")
        if novo_titulo: tarefa.titulo = novo_titulo
        if nova_descricao: tarefa.descricao = nova_descricao
        if nova_prioridade: tarefa.prioridade = nova_prioridade
        if novo_status: tarefa.status = novo_status
        return tarefa

    def remover_tarefa(self, titulo):
        tarefa = next((t for t in self.tarefas if t.titulo == titulo), None)
        if not tarefa:
            raise Exception("Tarefa não encontrada")
        self.tarefas.remove(tarefa)
        return tarefa
