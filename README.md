# Monitor-de-Tarefas-TechFlow
um sistema de gerenciamento de tarefas baseado em metodologias ágeis. Acompanhar o fluxo de trabalho em tempo real, priorizar tarefas críticas e monitorar o desempenho da equipe.


-- Visão Geral --
Este projeto foi desenvolvido como parte da disciplina de Engenharia de Software da UniFECAF. O objetivo é aplicar metodologias ágeis (Scrum/Kanban) e boas práticas de desenvolvimento para criar um sistema simples de gerenciamento de tarefas.

A empresa fictícia TechFlow Solutions precisa de um sistema que permita organizar atividades, acompanhar progresso e garantir qualidade por meio de testes automatizados.

-- Objetivos do Projeto --
Criar um sistema funcional de CRUD de tarefas (criar, listar, editar, excluir).

Implementar login simples para usuários.

Utilizar GitHub Projects para planejar e acompanhar tarefas.

Configurar GitHub Actions para rodar testes automatizados.

Documentar todas as etapas em um README.md e em um relatório teórico.

Simular uma mudança de escopo e justificar sua inclusão.

-- Metodologia Ágil -- 
Foi escolhido o Kanban como método de gestão visual.

Colunas: A Fazer, Em Progresso, Concluído.

Cards: mínimo de 10 tarefas, incluindo documentação, código, testes e mudança de escopo.

Cada tarefa é movida conforme seu progresso.

-- Estrutura do Projeto --
Código
/src        -> Código fonte do sistema
/tests      -> Testes automatizados
/docs       -> Diagramas UML e documentação extra
.github/    -> Configuração de workflows (CI/CD)
README.md   -> Documentação principal

-- Como Executar -- 
Clone o repositório:
"it clone https://github.com/seuusuario/projeto-agil.git"

Instale dependências:
"pip install -r requirements.txt"

Rode o sistema:
"python src/app.py"

Execute os testes:
"pytest"


 -- Gestão de Mudanças --
Durante o desenvolvimento, foi adicionada a funcionalidade de priorização de tarefas.

Motivo: necessidade de destacar tarefas críticas para a equipe.

Impacto: alteração no escopo inicial, registrada no README.md e no Kanban.


-- Diagramas UML --

Casos de Uso:
Usuário faz login.

Usuário cria, edita, exclui e lista tarefas.

Usuário prioriza tarefas.

Classes:

Usuario: atributos de login.

Tarefa: título, descrição, prioridade.

Sistema: gerencia lista de tarefas e usuários.

-- Qualidade e Testes -- 
Testes automatizados configurados com GitHub Actions.

Workflow roda automaticamente em cada push ou pull request.

Testes garantem que CRUD e login funcionem corretamente.


-- Conclusão --
Este projeto demonstra como aplicar Engenharia de Software na prática, unindo:

Planejamento ágil com Kanban.

Desenvolvimento incremental com commits semânticos.

Controle de qualidade com testes automatizados.

Gestão de mudanças documentada e justificada.
