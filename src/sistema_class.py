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
        self.usuarios.append(
            {"nome": nome, "email": email, "senha": senha}
        )

    def login(self, email, senha):
        for u in self.usuarios:
            if u["email"] == email and u["senha"] == senha:
                self.usuario_logado = type("Usuario", (), u)()
                return True
        return False

    def adicionar_tarefa(
        self, titulo, descricao, prioridade, status, autor=None
    ):
        if autor is None and self.usuario_logado:
            autor = self.usuario_logado.email
        
        tarefa = Tarefa(titulo, descricao, prioridade, status, autor)
        self.tarefas.append(tarefa)

    def listar_tarefas(self):
        return self.tarefas

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
