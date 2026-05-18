# Relatório de Auditoria Técnica e Refatoração - Ecommerce API Legacy

**Responsável:** Tiago Aragão (Analista de TI)
**Projeto:** ecommerce-api-legacy (Node.js/Express)
**Data de Conclusão:** 18 de maio de 2026
**Status:** Auditoria e Refatoração Concluídas ✅

## 1. Resumo Executivo
Esta auditoria analisou a API de e-commerce legada, identificando que o projeto operava sob o padrão de "Big Ball of Mud". A lógica de negócio, persistência de dados e roteamento estavam centralizadas num único ficheiro (`AppManager.js`), o que comprometia severamente a manutenibilidade e a segurança da aplicação. O objetivo da Fase 3 foi a migração total para uma arquitetura **MVC (Model-View-Controller)**.

## 2. Diagnóstico de Anti-padrões e Vulnerabilidades

| Anti-padrão | Severidade | Descrição e Impacto | Solução Aplicada (Fase 3) |
| :--- | :--- | :--- | :--- |
| **SQL Injection** | **CRITICAL** | Parâmetros de URL concatenados diretamente em strings SQL, permitindo a deleção não autorizada de dados. | Implementação de **Prepared Statements** (`?`) na Model `User.js`. |
| **Hardcoded Secrets** | **CRITICAL** | Chaves de API e caminhos de base de dados expostos no código (`utils.js`). | Migração para variáveis de ambiente via ficheiro **`.env`** e pacote `dotenv`. |
| **God Class (AppManager)** | **HIGH** | Um único objeto geria utilizadores, checkouts e relatórios, dificultando testes unitários. | Divisão em **Controllers** especializados (`Checkout`, `Report`, `User`). |
| **N+1 Query** | **HIGH** | Relatório financeiro executava uma consulta ao banco dentro de um loop para cada curso. | Otimização via **JOIN único** com agregadores SQL (`SUM`, `COUNT`) no `ReportController`. |
| **Insegurança de Hashing** | **MEDIUM** | Armazenamento de senhas em texto plano ou usando algoritmos obsoletos. | Implementação de **bcryptjs** com 10 rounds de salt para proteção de credenciais. |

## 3. Arquitetura Alvo (MVC)

### 📂 Camada de Modelo (Models)
* **`User.js`**: Centraliza a interação com o SQLite. Garante que os dados sensíveis (hashes de senha) sejam ocultados através do método `toDict()` antes de serem enviados para a API.

### 🎮 Camada de Controle (Controllers)
* **`CheckoutController.js`**: Gere o fluxo de compra, validação de utilizadores e registo de matrículas de forma isolada.
* **`ReportController.js`**: Focado em performance, entrega relatórios administrativos complexos com impacto mínimo no banco de dados.
* **`UserController.js`**: Interface para gestão de utilizadores com validação de parâmetros e tratamento de erros.

### 🛣️ Camada de Roteamento (Routes)
* **`index.js`**: Implementação de rotas limpas (**Thin Routes**). O roteador apenas mapeia os endpoints e delega a execução aos controllers, mantendo o `app.js` enxuto.

## 4. Evidências de Validação
* **Segurança SQL:** Testes de penetração via `curl` utilizando injeção de comandos na URL (`' OR '1'='1`) foram neutralizados. O sistema agora trata entradas maliciosas como strings literais.
* **Integridade de Ambiente:** O sistema agora exige a presença de um ficheiro `.env` para carregar o `DB_PATH`, eliminando caminhos fixos (hardcoded).
* **Escalabilidade:** A separação de pastas (`src/controllers`, `src/models`, `src/config`) permite manutenção modular sem risco de efeitos colaterais em outros componentes.

## 5. Conclusão
A refatoração transformou um protótipo inseguro num sistema de nível profissional. As vulnerabilidades críticas foram mitigadas e a dívida técnica foi reduzida significativamente, alinhando o projeto às melhores práticas de Engenharia de Software modernas e às exigências de segurança da informação.