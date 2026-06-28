# Commit: feat: adicionar persistência em arquivo (salvar e carregar tarefas)

import json

class Usuario:
    def __init__(self, nome, email, senha):
        self.nome = nome
        self.email = email
        self.senha = senha


class Tarefa:
    def __init__(self, titulo, descricao, prioridade=0, status="pendente"):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade
        self.status = status

    def editar(self, novo_titulo=None, nova_descricao=None, novo_prioridade=None, novo_status=None):
        if novo_titulo:
            self.titulo = novo_titulo
        if nova_descricao:
            self.descricao = nova_descricao
        if novo_prioridade is not None:
            self.prioridade = novo_prioridade
        if novo_status:
            self.status = novo_status

    def to_dict(self):
        return {
            "titulo": self.titulo,
            "descricao": self.descricao,
            "prioridade": self.prioridade,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        return Tarefa(data["titulo"], data["descricao"], data["prioridade"], data["status"])


class Sistema:
    def __init__(self):
        self.tarefas = []
        self.usuarios = []
        self.usuario_logado = None

    # ---------------- LOGIN ----------------
    def registrar_usuario(self, nome, email, senha):
        if any(u.email == email for u in self.usuarios):
            raise Exception(f"⚠️ Já existe um usuário registrado com o email: {email}")
        usuario = Usuario(nome, email, senha)
        self.usuarios.append(usuario)
        return usuario

    def login(self, email, senha):
        for u in self.usuarios:
            if u.email == email and u.senha == senha:
                self.usuario_logado = u
                return True
        raise Exception("❌ Falha no login: email ou senha incorretos.")

    def logout(self):
        if not self.usuario_logado:
            raise Exception("⚠️ Nenhum usuário está logado no momento.")
        self.usuario_logado = None

    # ---------------- CRUD ----------------
    def adicionar_tarefa(self, titulo, descricao, prioridade=0, status="pendente"):
        if not self.usuario_logado:
            raise Exception("🚫 É necessário estar logado para adicionar tarefas.")
        if any(t.titulo == titulo for t in self.tarefas):
            raise Exception(f"⚠️ Já existe uma tarefa com o título: {titulo}")
        tarefa = Tarefa(titulo, descricao, prioridade, status)
        self.tarefas.append(tarefa)
        return tarefa

    def listar_tarefas(self):
        if not self.tarefas:
            raise Exception("📭 Nenhuma tarefa encontrada.")
        return [(t.titulo, t.descricao, t.prioridade, t.status) for t in self.tarefas]

    def editar_tarefa(self, titulo, novo_titulo=None, nova_descricao=None, novo_prioridade=None, novo_status=None):
        for t in self.tarefas:
            if t.titulo == titulo:
                t.editar(novo_titulo, nova_descricao, novo_prioridade, novo_status)
                return t
        raise Exception(f"❌ Não foi possível editar: tarefa '{titulo}' não encontrada.")

    def remover_tarefa(self, titulo):
        if not any(t.titulo == titulo for t in self.tarefas):
            raise Exception(f"❌ Não foi possível remover: tarefa '{titulo}' não encontrada.")
        self.tarefas = [t for t in self.tarefas if t.titulo != titulo]

    # ---------------- PERSISTÊNCIA ----------------
    def salvar_tarefas(self, arquivo="tarefas.json"):
        with open(arquivo, "w", encoding="utf-8") as f:
            json.dump([t.to_dict() for t in self.tarefas], f, ensure_ascii=False, indent=4)

    def carregar_tarefas(self, arquivo="tarefas.json"):
        try:
            with open(arquivo, "r", encoding="utf-8") as f:
                dados = json.load(f)
                self.tarefas = [Tarefa.from_dict(d) for d in dados]
        except FileNotFoundError:
            self.tarefas = []


# -----------------------------
# Exemplo de uso
# -----------------------------
if __name__ == "__main__":
    sistema = Sistema()

    try:
        sistema.registrar_usuario("Felipe", "felipe@email.com", "1234")
        sistema.login("felipe@email.com", "1234")

        sistema.adicionar_tarefa("Estudar UML", "Fazer diagrama de casos de uso", prioridade=2, status="pendente")
        sistema.adicionar_tarefa("Implementar login", "Criar autenticação básica", prioridade=1, status="em andamento")

        print("\n📌 Lista de tarefas antes de salvar:")
        print(sistema.listar_tarefas())

        sistema.salvar_tarefas()

        # Simula novo sistema carregando tarefas
        novo_sistema = Sistema()
        novo_sistema.carregar_tarefas()
        print("\n📂 Lista de tarefas carregadas do arquivo:")
        print(novo_sistema.listar_tarefas())

    except Exception as e:
        print(str(e))
