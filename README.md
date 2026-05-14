# MBA Engenharia de Software com IA - Portfólio de Refatoração

**Responsável:** Tiago Aragão (Analista de TI - IFPI)  
**Objetivo:** Demonstração de competências em saneamento de dívida técnica, segurança cibernética e otimização de performance.

## 📂 Estrutura do Repositório

Este repositório está dividido em três frentes de trabalho complementares:

### 1. [Task Manager API](./task-manager-api)
Foco em **Segurança e Performance**.
- Implementação de autenticação JWT e correção de falhas IDOR.
- Otimização de queries (N+1) e agregação SQL.
- Documentação detalhada em `audit-project-3.md`.

### 2. [Code Smells Project](./code-smells-project)
Foco em **Qualidade de Código e SOLID**.
- Identificação de *God Objects* e *Long Methods*.
- Aplicação de padrões de projeto para reduzir a complexidade ciclomática.
- Refatoração de lógica de negócio para maior testabilidade.

### 3. [Ecommerce API Legacy](./ecommerce-api-legacy)
Foco em **Modernização e Padrões REST**.
- Reestruturação de uma API legada em Node.js.
- Padronização de endpoints e separação de preocupações (SoC).
- Documentação de integração via arquivos `.http`.

## 🛠️ Tecnologias Utilizadas
- **Linguagens:** Python, JavaScript (Node.js).
- **Frameworks:** Flask, Express.
- **Banco de Dados:** SQLite, SQLAlchemy.
- **Segurança:** PyJWT, Werkzeug (Hashing).

## 📊 Relatórios de Auditoria
Todos os projetos contêm relatórios específicos dentro da pasta `/reports` (ou na raiz de cada projeto), detalhando o "antes e depois" de cada intervenção técnica.

---
*Este repositório reflete as melhores práticas de Engenharia de Software aplicadas a sistemas institucionais.*