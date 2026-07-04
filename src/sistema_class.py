class Sistema:
    def __init__(self):
        self.usuarios = []
        self.usuario_logado = None
        self.tarefas = []

    def registrar_usuario(self, nome, email, senha):
        self.usuarios.append({"nome": nome, "email": email, "senha": senha})

    def login(self, email, senha):
        for u in self.usuarios:
            if u["email"] == email and u["senha"] == senha:
                self.usuario_logado = type("Usuario", (), u)()
                return True
        return False

    def adicionar_tarefa(self, titulo, descricao, prioridade, status):
        self.tarefas.append({
            "titulo": titulo,
            "descricao": descricao,
            "prioridade": prioridade,
            "status": status,
            "autor": self.usuario_logado.email if self.usuario_logado else None
        })

    def listar_tarefas(self):
        return self.tarefas

    def editar_tarefa(self, titulo_antigo, novo_titulo, nova_desc, nova_prioridade, novo_status):
        for t in self.tarefas:
            if t["titulo"] == titulo_antigo:
                t["titulo"] = novo_titulo
                t["descricao"] = nova_desc
                t["prioridade"] = nova_prioridade
                t["status"] = novo_status

    def remover_tarefa(self, titulo):
        self.tarefas = [t for t in self.tarefas if t["titulo"] != titulo]
