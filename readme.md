Bem-vindo ao nosso desafio para a vaga de Desenvolvedor Python/Django FullStack! Este é um teste projetado para avaliar suas habilidades e conhecimentos técnicos. Antes de começar, certifique-se de configurar o ambiente de desenvolvimento conforme as instruções abaixo.

# Configuração do Ambiente

1. Crie um virtualenv
2. Instale as dependências do projeto
3. Migre o banco de dados
4. Rode o projeto

# Desafios

Desafio 1 - Verificação de Senha no Frontend
Na tela de cadastro de usuário (/accounts/singup/), adicione uma verificação via JavaScript no frontend para fornecer feedback em tempo real ao usuário, indicando se as senhas coincidem.

Desafio 2 - Redirecionamento para a Tela de Login
Ao acessar as telas de listagem, cadastro e edição de uma task (/, task/create/, task/int:pk/delete/), redirecione  para a tela de login caso o usuário não esteja autenticado.

Desafio 3 - Redirecionamento após login
Após a autenticação do usuário (/accounts/login/), o sistema deverá redirecionar para a listagem de tasks.

Desafio 4 - Ajuste no modelo
Herde as características do modelo BaseModel no app "core" no modelo Category no app "todo"

Desafio 5 - CRUD do Modelo "Category"
No app "todo", implemente as operações CRUD (listagem, cadastro, edição e exclusão) para o modelo "Category". Adicione o campo "category" no formulário de cadastro da Task (task/create/). Os usuário só poderam ver, editar e excluir as categorias criadas por si mesmo. Ao cadastrar uma task, no campo de categoria devem aparecer apenas as categorias criadas por ele.

Desafio 6 - Filtro de Tasks por Usuário Autenticado
Na listagem de Tasks, mostre apenas as tarefas criadas pelo usuário autenticado. Ou seja, um usuário X não deve visualizar as tarefas criadas pelo usuário Y. 

Desafio 7 - Implemente um recurso de filtro nas listagem de TASK (por title, category) e CATEGORY(por nome)

Desafio 8 - Implementação de Comentários nas Tasks
Adicione uma funcionalidade para que os usuários possam adicionar comentários nas tasks. Crie um modelo de comentários associado ao modelo de tasks e adicione a interface necessária para exibir e adicionar comentários na página de detalhes da task.

Desafio 9 - Rota de API (use Django Rest Framework) para Marcar uma Task como "Completa"
Crie uma rota de API para marcar uma Task como "Completa". Na listagem de tasks, implemente um checkbox que, ao ser clicado, envia uma requisição ao backend marcando a task como completada. Se desmarcar, a mesma rota deve ser chamada para desfazer a marcação.

Desafio 10 - Bloqueio para Remover Task Completada
Impedir a remoção de uma task marcada como completada a nível de backend, não apenas no frontend.

Desafio 11 - Redesign das Telas
Aplique um redesign nas telas do sistema utilizando o template Bootstrap disponível em https://adminlte.io/. Baixe os HTMLs do template e integre-os ao projeto, utilizando conceitos como templates, blocks e includes. Crie um sidebar com duas opções: categorias e tasks.

Desafio 12 - Adição de Testes Unitários
Implemente testes unitários para funcionalidades a sua escolha no projeto. Pelo menos 4 testes.

Desafio 13 - Crie um novo recurso
Use sua criatividade e adicione um novo recurso ao sistema, que ainda não existe. Crie pelo menos um novo modelo para esse novo recurso.

Desafio 14 - Paginação na Listagem de Tasks
Implemente a paginação na listagem de tasks para garantir uma melhor experiência do usuário, especialmente quando há um grande número de tarefas.

Desafio 15 - Containerização do Projeto com Docker
Containerize o seu projeto utilizando o Docker. Crie um Dockerfile que inclua todas as dependências necessárias para o seu projeto, configure a aplicação para rodar em um container. Considere também o uso do Docker Compose.

# Entrega do Projeto

1. Crie um repositório privado em seu GitHub.
2. Envie suas modificações para o projeto no GitHub.
3. Adicione o usuário franklindias como colaborador do projeto.
4. Marque a data desejada para a apresentação do projeto em https://calendar.app.google/moy5AsStjGd8vJTB6

Sinta-se à vontade para adicionar ou aprimorar funcionalidades, bem como melhorar as implementações existentes conforme julgar apropriado. Boa sorte!
