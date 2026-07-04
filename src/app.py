from flask import Flask, render_template, request, redirect
from sistema import Sistema  # supondo que você tenha a classe Sistema em sistema.py

app = Flask(__name__)
sistema = Sistema()


@app.route("/", methods=["GET"])
def index():
    status = request.args.get("status")
    if status:
        tarefas = [t for t in sistema.listar_tarefas() if t["status"]
                   == status]
    else:
        tarefas = sistema.listar_tarefas()
    return render_template("index.html", tarefas=tarefas)


@app.route("/adicionar", methods=["POST"])
def adicionar():
    titulo = request.form["titulo"]
    descricao = request.form["descricao"]
    prioridade = request.form["prioridade"]
    status = request.form["status"]
    sistema.adicionar_tarefa(titulo, descricao, prioridade, status)
    return redirect("/")


@app.route("/remover", methods=["POST"])
def remover():
    titulo = request.form["titulo"]
    sistema.remover_tarefa(titulo)
    return redirect("/")


@app.route("/editar", methods=["POST"])
def editar():
    titulo = request.form["titulo"]
    # Aqui você pode abrir um modal ou redirecionar para uma página de edição
    # Para simplificar, vamos apenas marcar como concluída
    sistema.editar_tarefa(titulo, "Novo Título",
                          "Nova Desc", "Baixa", "Concluída")
    return redirect("/")
