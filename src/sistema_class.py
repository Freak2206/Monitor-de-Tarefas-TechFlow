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

<<<<<<< HEAD
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
        self, titulo, descricao, prioridade, status
    ):
        self.tarefas.append(
            {
                "titulo": titulo,
                "descricao": descricao,
                "prioridade": prioridade,
                "status": status,
                "autor": (
                    self.usuario_logado.email
                    if self.usuario_logado
                    else None
                ),
            }
        )

    def listar_tarefas(self):
        return self.tarefas

    def editar_tarefa(
        self,
        titulo_antigo,
        novo_titulo,
        nova_desc,
        nova_prioridade,
        novo_status,
    ):
        for t in self.tarefas:
            if t["titulo"] == titulo_antigo:
                t["titulo"] = novo_titulo
                t["descricao"] = nova_desc
                t["prioridade"] = nova_prioridade
                t["status"] = novo_status

    def remover_tarefa(self, titulo):
        self.tarefas = [
            t for t in self.tarefas if t["titulo"] != titulo
        ]
=======
    def adicionar_tarefa(self, titulo, descricao, prioridade, status, autor):
        tarefa = Tarefa(titulo, descricao, prioridade, status, autor)
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
>>>>>>> 1b9edfc (commit final: ajustes no app.py, sistema_class.py e templates (index, login, register) para fluxo completo de login, registro e gerenciamento de tarefas)
