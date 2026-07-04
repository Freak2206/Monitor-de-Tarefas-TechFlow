from flask import Flask, request, render_template, redirect, url_for
from src.app import Sistema

app = Flask(__name__)
sistema = Sistema()


@app.route("/")
def index():
    tarefas = sistema.listar_tarefas()
    return render_template("index.html", tarefas=tarefas, sistema=sistema)


# --- Registro ---
@app.route("/register", methods=["POST"])
def register():
    nome = request.form["nome"]
    email = request.form["email"]
    senha = request.form["senha"]
    try:
        sistema.registrar_usuario(nome, email, senha)
    except Exception as e:
        return str(e)
    return redirect(url_for("index"))


# --- Login / Logout ---
@app.route("/login", methods=["POST"])
def login():
    email = request.form["email"]
    senha = request.form["senha"]
    try:
        sistema.login(email, senha)
    except Exception as e:
        return str(e)
    return redirect(url_for("index"))


@app.route("/logout")
def logout():
    sistema.logout()
    return redirect(url_for("index"))


# --- Tarefas ---
@app.route("/tasks", methods=["POST"])
def adicionar_tarefa():
    titulo = request.form["titulo"]
    descricao = request.form["descricao"]
    prioridade = request.form["prioridade"]
    status = request.form["status"]
    try:
        sistema.adicionar_tarefa(titulo, descricao, prioridade, status)
    except Exception as e:
        return str(e)
    return redirect(url_for("index"))


@app.route("/editar/<titulo>", methods=["POST"])
def editar_tarefa(titulo):
    novo_titulo = request.form["titulo"]
    nova_descricao = request.form["descricao"]
    nova_prioridade = request.form["prioridade"]
    novo_status = request.form["status"]
    try:
        sistema.editar_tarefa(
            titulo, novo_titulo, nova_descricao, nova_prioridade, novo_status
        )
    except Exception as e:
        return str(e)
    return redirect(url_for("index"))


@app.route("/remover/<titulo>")
def remover_tarefa(titulo):
    try:
        sistema.remover_tarefa(titulo)
    except Exception as e:
        return str(e)
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
