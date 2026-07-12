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
