from flask import Flask, render_template, request, redirect, session
from src.sistema_class import Sistema

app = Flask(__name__)
app.secret_key = "chave-super-secreta-techflow"  # chave fixa para manter a sessão

# Instância do sistema
sistema = Sistema()
usuarios = {}  # dicionário simples para armazenar usuários {usuario: senha}


# Rota de registro
@app.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        if not usuario or not senha:
            return "Preencha todos os campos!"
        usuarios[usuario] = senha
        return redirect("/login")
    return render_template("register.html")


# Rota de login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        if usuarios.get(usuario) == senha:
            session["usuario"] = usuario
            return redirect("/")
        return "Usuário ou senha inválidos!"
    return render_template("login.html")


# Rota de logout
@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect("/login")


# Página inicial
@app.route("/")
def index():
    usuario = session.get("usuario")
    if not usuario:
        return redirect("/login")
    return render_template(
        "index.html", tarefas=sistema.tarefas, usuario=usuario
    )


# Criar tarefa
@app.route("/criar", methods=["POST"])
def criar_tarefa():
    titulo = request.form.get("titulo")
    descricao = request.form.get("descricao")
    prioridade = request.form.get("prioridade")
    autor = session.get("usuario")
    sistema.adicionar_tarefa(titulo, descricao, prioridade, "pendente", autor)
    return redirect("/")


# Concluir tarefa
@app.route("/concluir/<titulo>")
def concluir_tarefa(titulo):
    sistema.concluir_tarefa(titulo)
    return redirect("/")


# Remover tarefa
@app.route("/remover/<titulo>")
def remover_tarefa(titulo):
    sistema.remover_tarefa(titulo)
    return redirect("/")


# Editar tarefa
@app.route("/editar/<titulo>", methods=["POST"])
def editar_tarefa(titulo):
    novo_titulo = request.form.get("titulo")
    nova_descricao = request.form.get("descricao")
    nova_prioridade = request.form.get("prioridade")
    novo_status = request.form.get("status")
    sistema.editar_tarefa(
        titulo, novo_titulo, nova_descricao, nova_prioridade, novo_status
    )
    return redirect("/")
