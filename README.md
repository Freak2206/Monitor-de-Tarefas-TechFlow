# Monitor-de-Tarefas-TechFlow
# Construindo um Projeto Ágil no GitHub: Da Gestão ao Controle de Qualidade

Este projeto foi desenvolvido como parte da atividade da disciplina de Engenharia de Software da UniFECAF.  
A empresa fictícia **TechFlow Solutions** foi contratada para criar um sistema de gerenciamento de tarefas com foco em práticas ágeis, testes automatizados e qualidade de software.

---

##  Funcionalidades Implementadas

### Commit 1 — *feat: criar estrutura inicial do projeto*
- Criação da pasta `src/` e arquivo `app.py`.
- Classe `Sistema` com estrutura básica.

### Commit 2 — *feat: adicionar CRUD de tarefas*
- Implementação das operações de adicionar, listar, editar e remover tarefas.

### Commit 3 — *test: adicionar testes para CRUD*
- Arquivo `tests/test_app.py` com testes unitários para o CRUD.

### Commit 4 — *test: adicionar testes para login*
- Arquivo `tests/test_login.py` validando login, logout e bloqueio de CRUD sem login.

### Commit 5 — *refactor: melhorar mensagens de erro*
- Mensagens de erro mais claras e amigáveis.
- Validações adicionais: email duplicado, título duplicado de tarefa.

### Commit 6 — *feat: adicionar prioridade e status às tarefas*
- Cada tarefa possui prioridade e status (pendente, em andamento, concluída).

### Commit 7 — *feat: adicionar filtro de tarefas por status e prioridade*
- Métodos para filtrar tarefas por status ou prioridade.

### Commit 8 — *feat: adicionar persistência em arquivo (salvar e carregar tarefas)*
- Salvamento das tarefas em `tarefas.json`.
- Carregamento automático das tarefas ao reiniciar o sistema.

### Commit 9 — *feat: adicionar interface de linha de comando (CLI)*
- Interação via terminal com comandos como `adicionar`, `listar`, `editar`, `remover`, `salvar`, `carregar`.

### Commit 10 — *test: adicionar testes automatizados para a CLI*
- Arquivo `tests/test_cli.py` simulando comandos e validando saídas da CLI.

### Commit 11 — *feat: adicionar interface gráfica simples (GUI com Tkinter)*
- Arquivo `src/gui.py` com interface gráfica para login e gerenciamento de tarefas.

### Commit 12 — *test: adicionar testes automatizados para a GUI*
- Arquivo `tests/test_gui.py` validando login e adicionar tarefas via GUI.

### Commit 13 — *feat: documentação do projeto (README detalhado)*
- Criação deste README com histórico dos commits e funcionalidades.

---

##  Tecnologias Utilizadas
- **Python 3.13**
- **Pytest** para testes automatizados
- **Tkinter** para GUI
- **JSON** para persistência de dados
- **Git/GitHub** para versionamento e colaboração

---

## 📂 Estrutura do Projeto
TECHFLOW/
│
├── src/
│   ├── app.py        # Lógica principal do sistema
│   └── gui.py        # Interface gráfica (Tkinter)
│
├── tests/
│   ├── test_app.py   # Testes do CRUD
│   ├── test_login.py # Testes de login/logout
│   ├── test_cli.py   # Testes da CLI
│   └── test_gui.py   # Testes da GUI
│
├── tarefas.json      # Persistência das tarefas
└── README.md         # Documentação do projeto

Código

---

##  Como Executar
1. Clone o repositório:
   ```bash
   git clone <url-do-repo>
   cd TECHFLOW
Instale as dependências:

bash
python -m pip install pytest
Execute os testes:

bash
python -m pytest -v
Rode a CLI:

bash
python src/app.py
Rode a GUI:

bash
python src/gui.py
 Conclusão
Este projeto demonstra a aplicação de práticas ágeis, versionamento semântico de commits e integração de testes automatizados em diferentes camadas (CRUD, login, CLI e GUI).
A documentação garante rastreabilidade das alterações conforme solicitado na atividade.

Código

---

##  Comandos Git para subir o commit

```bash
git add README.md
git commit -m "feat: documentação do projeto (README detalhado)"
git push origin main