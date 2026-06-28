class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


class Tarefa:
    def __init__(self, titulo, descricao, prioridade=0):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade

    def editar(self, novo_titulo=None, nova_descricao=None, novo_prioridade=None):
        if novo_titulo:
            self.titulo = novo_titulo
        if nova_descricao:
            self.descricao = nova_descricao
        if novo_prioridade is not None:
            self.prioridade = novo_prioridade


class Sistema:
    def __init__(self):
        self.tarefas = []
        self.usuarios = []
        self.usuario_logado = None

    # ---------------- LOGIN ----------------
    def registrar_usuario(self, nome, email, senha):
        usuario = Usuario(nome, email, senha)
        self.usuarios.append(usuario)
        return usuario

    def login(self, email, senha):
        for u in self.usuarios:
            if u.email == email and u.senha == senha:
                self.usuario_logado = u
                return True
        return False

    def logout(self):
        self.usuario_logado = None

    # ---------------- CRUD ----------------
    def adicionar_tarefa(self, titulo, descricao, prioridade=0):
        if not self.usuario_logado:
            raise Exception("É necessário estar logado para adicionar tarefas.")
        tarefa = Tarefa(titulo, descricao, prioridade)
        self.tarefas.append(tarefa)
        return tarefa

    def listar_tarefas(self):
        return [(t.titulo, t.descricao, t.prioridade) for t in self.tarefas]

    def editar_tarefa(self, titulo, novo_titulo=None, nova_descricao=None, novo_prioridade=None):
        for t in self.tarefas:
            if t.titulo == titulo:
                t.editar(novo_titulo, nova_descricao, novo_prioridade)
                return t
        return None

    def remover_tarefa(self, titulo):
        self.tarefas = [t for t in self.tarefas if t.titulo != titulo]


# -----------------------------
# Exemplo de uso
# -----------------------------
if __name__ == "__main__":
    sistema = Sistema()

    # Registrar e logar usuário
    sistema.registrar_usuario("Felipe", "felipe@email.com", "1234")
    login_ok = sistema.login("felipe@email.com", "1234")

    if login_ok:
        print("✅ Login realizado com sucesso!")

        # Criar tarefas
        sistema.adicionar_tarefa("Estudar UML", "Fazer diagrama de casos de uso", prioridade=2)
        sistema.adicionar_tarefa("Implementar login", "Criar autenticação básica", prioridade=1)

        print("\n📌 Lista inicial de tarefas:")
        print(sistema.listar_tarefas())

        # Editar tarefa
        sistema.editar_tarefa("Estudar UML", nova_descricao="Fazer diagrama de classes", novo_prioridade=3)

        print("\n✏️ Após edição da tarefa:")
        print(sistema.listar_tarefas())

        # Remover tarefa
        sistema.remover_tarefa("Implementar login")

        print("\n🗑️ Após remover tarefa:")
        print(sistema.listar_tarefas())
    else:
        print("❌ Falha no login!")
