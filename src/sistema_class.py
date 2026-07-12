class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha

class Tarefa:
    def __init__(self, titulo, descricao, prioridade, status, autor):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = status
        self.autor = autor

class Sistema:
    def __init__(self):
        self.tarefas = []
        self.usuarios = []
        self.usuario_logado = None

    def registrar_usuario(self, nome, email, senha):
        usuario = Usuario(nome, email, senha)
        self.usuarios.append(usuario)

    def login(self, email, senha):
        for usuario in self.usuarios:
            if usuario.email == email and usuario.senha == senha:
                self.usuario_logado = usuario
                return True
        return False

    def adicionar_tarefa(self, titulo, descricao, prioridade, status):
        if self.usuario_logado is None:
            raise Exception("Usuário não está logado")
        tarefa = Tarefa(titulo, descricao, prioridade, status, self.usuario_logado.nome)
        self.tarefas.append(tarefa)

    def remover_tarefa(self, titulo):
        self.tarefas = [t for t in self.tarefas if t.titulo != titulo]

    def concluir_tarefa(self, titulo):
        for t in self.tarefas:
            if t.titulo == titulo:
                t.status = "concluída"

    def editar_tarefa(self, titulo_antigo, novo_titulo, nova_descricao, nova_prioridade, novo_status):
        for t in self.tarefas:
            if t.titulo == titulo_antigo:
                t.titulo = novo_titulo
                t.descricao = nova_descricao
                t.prioridade = nova_prioridade
                t.status = novo_status

    def listar_tarefas(self):
        return [{"titulo": t.titulo, "descricao": t.descricao, "prioridade": t.prioridade, "status": t.status, "autor": t.autor} for t in self.tarefas]
