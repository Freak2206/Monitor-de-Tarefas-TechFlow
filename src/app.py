class Tarefa:
    def __init__(self, titulo, descricao, prioridade=0):
        self.titulo = titulo
        self.descricao = descricao
        self.prioridade = prioridade

    def editar(self, novo_titulo=None, nova_descricao=None, nova_prioridade=None):
        if novo_titulo:
            self.titulo = novo_titulo
        if nova_descricao:
            self.descricao = nova_descricao
        if nova_prioridade is not None:
            self.prioridade = nova_prioridade


class Sistema:
    def __init__(self):
        self.tarefas = []

    # CREATE
    def adicionar_tarefa(self, titulo, descricao, prioridade=0):
        tarefa = Tarefa(titulo, descricao, prioridade)
        self.tarefas.append(tarefa)
        return tarefa

    # READ
    def listar_tarefas(self):
        return [(t.titulo, t.descricao, t.prioridade) for t in self.tarefas]

    # UPDATE
    def editar_tarefa(self, titulo, novo_titulo=None, nova_descricao=None, novo_prioridade=None):
        for t in self.tarefas:
            if t.titulo == titulo:
                t.editar(novo_titulo, nova_descricao, novo_prioridade)
                return t
        return None

    # DELETE
    def remover_tarefa(self, titulo):
        self.tarefas = [t for t in self.tarefas if t.titulo != titulo]
