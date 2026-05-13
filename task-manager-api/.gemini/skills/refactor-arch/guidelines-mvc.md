# Diretrizes para a Arquitetura MVC

Este guia define a responsabilidade de cada camada na nova estrutura do projeto. Siga estas definições rigorosamente durante a Fase 3.

## ## 1. Models (`src/models/`)
- **Responsabilidade:** Representação dos dados e interação com o banco de dados.
- **Regras:**
  - Toda query SQL ou chamada de ORM deve residir aqui.
  - Validações de formato de dados (ex: regex de e-mail, tipos de campos) ficam no Model.
  - Em Python, use classes ou Data Classes. Em Node, use Mongoose/Sequelize ou Classes simples.

## ## 2. Controllers (`src/controllers/`)
- **Responsabilidade:** Lógica de negócio e orquestração.
- **Regras:**
  - O Controller recebe os dados das rotas, processa a lógica de negócio e chama o Model.
  - Ele não deve saber detalhes de implementação do banco de dados.
  - Deve tratar exceções e decidir qual status HTTP retornar (200, 201, 400, etc).

## ## 3. Routes/Views (`src/routes/`)
- **Responsabilidade:** Definição dos endpoints e contratos da API.
- **Regras:**
  - Este arquivo deve ser "magro" (thin). A única função dele é mapear o Verbo HTTP + URL para uma função do Controller.
  - Nenhuma lógica de negócio ou de dados pode estar aqui.

## ## 4. Entry Point (`src/app.py` ou `src/index.js`)
- **Responsabilidade:** Inicialização da aplicação.
- **Regras:**
  - Configuração de middlewares (CORS, JSON parser).
  - Registro dos blueprints (Flask) ou routers (Express).
  - Inicialização do servidor e conexões.