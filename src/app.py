<<<<<<< HEAD
from flask import Flask, render_template, request, redirect
from sistema import Sistema
=======
from flask import Flask, render_template, request, redirect, session
from src.sistema_class import Sistema
>>>>>>> 1b9edfc (commit final: ajustes no app.py, sistema_class.py e templates (index, login, register) para fluxo completo de login, registro e gerenciamento de tarefas)

app = Flask(__name__)
app.secret_key = "chave-secreta-super-segura"
app.config["PROPAGATE_EXCEPTIONS"] = True
import logging
logging.basicConfig(level=logging.DEBUG)


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
        if usuario in usuarios:
            return "Usuário já existe!"
        usuarios[usuario] = senha
        return redirect("/login")
    return render_template("register.html")

# Rota de login
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        usuario = request.form.get("usuario")
        senha = request.form.get("senha")
        if usuario in usuarios and usuarios[usuario] == senha:
            session["usuario"] = usuario
            return redirect("/")
        else:
            return "Login inválido"
    return render_template("login.html")

# Rota principal
@app.route("/", methods=["GET"])
def home():
    return render_template(
        "index.html",
        tarefas=sistema.tarefas,
        usuario=session.get("usuario")  # garante que 'usuario' sempre existe
    )

# Criar nova tarefa
@app.route("/tasks", methods=["POST"])
def tasks():
    if "usuario" not in session:
        return redirect("/login")
    titulo = request.form.get("titulo")
    descricao = request.form.get("descricao")
    prioridade = request.form.get("prioridade")
    status = request.form.get("status")
    sistema.adicionar_tarefa(titulo, descricao, prioridade, status, session["usuario"])
    return redirect("/")

# Remover tarefa
@app.route("/remover/<titulo>")
def remover(titulo):
    sistema.remover_tarefa(titulo)
    return redirect("/")

<<<<<<< HEAD

@app.route("/editar", methods=["POST"])
def editar():
    titulo = request.form["titulo"]
    # Aqui você pode abrir um modal ou redirecionar para uma página
    # de edição. Para simplificar, vamos apenas marcar como concluída
    sistema.editar_tarefa(titulo, "Novo Título",
                          "Nova Desc", "Baixa", "Concluída")
=======
# Concluir tarefa
@app.route("/concluir/<titulo>")
def concluir(titulo):
    sistema.concluir_tarefa(titulo)
>>>>>>> 1b9edfc (commit final: ajustes no app.py, sistema_class.py e templates (index, login, register) para fluxo completo de login, registro e gerenciamento de tarefas)
    return redirect("/")

# Editar tarefa
@app.route("/editar/<titulo>", methods=["POST"])
def editar(titulo):
    novo_titulo = request.form.get("titulo")
    nova_descricao = request.form.get("descricao")
    nova_prioridade = request.form.get("prioridade")
    novo_status = request.form.get("status")
    sistema.editar_tarefa(titulo, novo_titulo, nova_descricao, nova_prioridade, novo_status)
    return redirect("/")

# Logout
@app.route("/logout")
def logout():
    session.pop("usuario", None)
    return redirect("/login")

if __name__ == "__main__":
    app.run(debug=True)
