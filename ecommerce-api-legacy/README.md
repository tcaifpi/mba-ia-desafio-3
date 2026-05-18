# Ecommerce API Legacy - Modernização e Refatoração MVC

**Responsável:** Tiago Aragão (Analista de TI)
**Projeto:** Refatoração, Auditoria de Segurança e Migração de API
**Tecnologias:** Node.js, Express, SQLite, Bcryptjs, Dotenv.

## 🚀 Visão Geral
Este projeto consistiu na modernização de uma API de e-commerce legada que apresentava graves riscos de segurança e débitos técnicos estruturais. A aplicação foi totalmente reestruturada utilizando o padrão **MVC (Model-View-Controller)**, garantindo a separação de preocupações e a preparação para escalabilidade futura.

## 🛠️ Intervenções Técnicas e Melhorias

### 1. Arquitetura MVC e Clean Code
* **Separação de Preocupações (SoC):** A lógica que antes era centralizada em um "God Object" (`AppManager.js`) foi distribuída entre Controllers, Models e Rotas.
* **Models Abstratas:** Criação da classe `User.js` para gerir a persistência e lógica de dados de forma isolada.
* **Controllers Especializados:** Implementação de controladores específicos para Checkout, Relatórios e Usuários, eliminando o acoplamento forte.

### 🛡️ Segurança e Blindagem
* **Mitigação de SQL Injection:** Substituição da concatenação de strings por **Prepared Statements** em todas as interações com o banco de dados.
* **Criptografia de Senhas:** Substituição de métodos obsoletos pelo **bcryptjs** (10 rounds), garantindo proteção contra ataques de dicionário e Timing Attacks.
* **Gestão de Segredos:** Migração de chaves de API e caminhos de banco para variáveis de ambiente via **`.env`**, evitando a exposição de dados sensíveis no código-fonte.

### ⚡ Performance e Escalabilidade
* **Otimização de Consultas:** Refatoração do relatório financeiro para utilizar um **JOIN SQL único**, eliminando o problema de performance **N+1 Query** que causava latência no sistema legado.
* **Padronização RESTful:** Endpoints reestruturados para seguir os métodos HTTP corretos (GET, POST, DELETE) e retornar status codes apropriados.

## 📂 Estrutura do Projeto
- `src/controllers/`: Lógica de requisição e resposta.
- `src/models/`: Camada de abstração de dados e regras de segurança SQL.
- `src/routes/`: Definição de endpoints e roteamento.
- `src/config/`: Configurações de conexão e banco de dados.
- `api.http`: Documentação e testes rápidos de endpoints.

## 🚦 Como Executar

1. **Instalar Dependências:**
   ```bash
   npm install