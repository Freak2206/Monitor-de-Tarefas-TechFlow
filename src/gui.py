# Commit: feat: adicionar interface gráfica simples (GUI com Tkinter)

import tkinter as tk
from tkinter import messagebox
from src.app import Sistema

class AppGUI:
    def __init__(self, root):
        self.sistema = Sistema()
        self.root = root
        self.root.title("Gerenciador de Tarefas - TechFlow")

        # Campos de login
        self.lbl_email = tk.Label(root, text="Email:")
        self.lbl_email.pack()
        self.entry_email = tk.Entry(root)
        self.entry_email.pack()

        self.lbl_senha = tk.Label(root, text="Senha:")
        self.lbl_senha.pack()
        self.entry_senha = tk.Entry(root, show="*")
        self.entry_senha.pack()

        self.btn_login = tk.Button(root, text="Login", command=self.login)
        self.btn_login.pack()

        # Campos de tarefa
        self.lbl_titulo = tk.Label(root, text="Título da tarefa:")
        self.lbl_titulo.pack()
        self.entry_titulo = tk.Entry(root)
        self.entry_titulo.pack()

        self.lbl_desc = tk.Label(root, text="Descrição:")
        self.lbl_desc.pack()
        self.entry_desc = tk.Entry(root)
        self.entry_desc.pack()

        self.lbl_prioridade = tk.Label(root, text="Prioridade:")
        self.lbl_prioridade.pack()
        self.entry_prioridade = tk.Entry(root)
        self.entry_prioridade.pack()

        self.lbl_status = tk.Label(root, text="Status:")
        self.lbl_status.pack()
        self.entry_status = tk.Entry(root)
        self.entry_status.pack()

        self.btn_add = tk.Button(root, text="Adicionar Tarefa", command=self.adicionar_tarefa)
        self.btn_add.pack()

        self.btn_listar = tk.Button(root, text="Listar Tarefas", command=self.listar_tarefas)
        self.btn_listar.pack()

        self.text_output = tk.Text(root, height=10, width=50)
        self.text_output.pack()

    def login(self):
        email = self.entry_email.get()
        senha = self.entry_senha.get()
        try:
            self.sistema.login(email, senha)
            messagebox.showinfo("Sucesso", "Login realizado com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def adicionar_tarefa(self):
        titulo = self.entry_titulo.get()
        descricao = self.entry_desc.get()
        prioridade = int(self.entry_prioridade.get() or 0)
        status = self.entry_status.get() or "pendente"
        try:
            self.sistema.adicionar_tarefa(titulo, descricao, prioridade, status)
            messagebox.showinfo("Sucesso", "Tarefa adicionada com sucesso!")
        except Exception as e:
            messagebox.showerror("Erro", str(e))

    def listar_tarefas(self):
        try:
            tarefas = self.sistema.listar_tarefas()
            self.text_output.delete("1.0", tk.END)
            for t in tarefas:
                self.text_output.insert(tk.END, f"{t}\n")
        except Exception as e:
            messagebox.showerror("Erro", str(e))


if __name__ == "__main__":
    root = tk.Tk()
    app = AppGUI(root)
    root.mainloop()
