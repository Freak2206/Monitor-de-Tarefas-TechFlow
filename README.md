TechFlow - Sistema de Tarefas
 Visão Geral
O TechFlow é um sistema de gerenciamento de tarefas desenvolvido em Flask com interface única em Bootstrap, permitindo registro, login e CRUD completo de tarefas. O projeto segue práticas ágeis e inclui testes automatizados e pipeline de integração contínua.

 Como executar o projeto
Clone o repositório:

bash
git clone https://github.com/seuusuario/techflow.git
cd techflow
Crie e ative um ambiente virtual:

bash
python -m venv venv
source venv/bin/activate   # Linux/Mac
venv\Scripts\activate      # Windows
Instale as dependências:

bash
pip install -r requirements.txt
Execute o servidor Flask:

bash
flask run
Acesse no navegador:

Código
http://127.0.0.1:5000

 Testes Automatizados
Os testes foram implementados com Pytest e estão localizados na pasta tests/.

Rodando os testes localmente
bash
pytest
Estrutura de testes
Registro e login de usuários

Adição de tarefas

Edição de tarefas

Remoção de tarefas

 Integração Contínua (CI/CD)
O projeto utiliza GitHub Actions para rodar testes e validar qualidade a cada push.

Pipeline configurado em .github/workflows/ci.yml
Instala dependências

Executa testes com Pytest

Valida qualidade do código com Flake8

Resultado:

✅ Se tudo passar, aparece verde na aba Actions

❌ Se falhar, aparece vermelho com log detalhado

 Commits Semânticos
O projeto segue o padrão Conventional Commits:

feat: nova funcionalidade

fix: correção de bug

refactor: melhoria sem alterar comportamento

docs: mudanças em documentação

test: criação ou alteração de testes

ci: configuração de integração contínua

Exemplo de histórico:

feat: implementar modal de edição de tarefas

fix: corrigir variável sistema não definida

test: adicionar testes para login e CRUD

ci: configurar pipeline GitHub Actions

 Mudança de Escopo Simulada
Durante o desenvolvimento, foi simulada uma mudança de escopo:

Novo card no Kanban: "Adicionar filtro de status nas tarefas"

Commit semântico: feat: adicionar filtro de status nas tarefas

Implementação: inclusão de um campo select para filtrar tarefas por status

Documentação: este README foi atualizado para registrar a mudança

Essa prática demonstra adaptação ágil e registro transparente de alterações.

 Conclusão
O TechFlow cumpre os requisitos do trabalho:

Commits semânticos e frequentes

Testes automatizados com Pytest

Pipeline CI/CD com GitHub Actions

Simulação de mudança de escopo documentada

Pronto para entrega e evolução futura.