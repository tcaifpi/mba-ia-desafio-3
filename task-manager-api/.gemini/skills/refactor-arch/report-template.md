# 🛡️ Relatório de Conformidade Técnica: Refatoração e Segurança

**Responsável:** Tiago Aragão (Analista de TI)  
**Projeto:** [Nome do Projeto]  
**Data:** [Data]  
**Status:** 🟢 Saneado e Validado

---

## 1. Evolução Arquitetural (Migração para MVC)

O projeto foi submetido a uma reestruturação completa para mitigar o débito técnico causado pelo padrão **God File** (monólito de ficheiro único). A nova arquitetura modular segue o padrão **MVC**, garantindo o desacoplamento de responsabilidades:

* **📦 Models (Camada de Dados):** Centralização da lógica de persistência, esquemas de banco de dados e sanitização rigorosa de entradas.
* **⚙️ Controllers (Lógica de Negócio):** Orquestração das regras de negócio, validações de permissão e processamento de dados, isolados da camada de transporte.
* **🛣️ Routes (Interface de Exposição):** Definição clara de endpoints RESTful e mapeamento de verbos HTTP, facilitando a governança da API.

> **Impacto:** Melhoria na manutenibilidade e redução da complexidade ciclomática.

---

## 2. Fortalecimento da Postura de Segurança

Foram identificadas e neutralizadas vulnerabilidades críticas que comprometiam a integridade e a confidencialidade do sistema:

### 💉 Mitigação de SQL Injection
- **Antes:** Queries construídas via concatenação de strings, vulneráveis a injeção de comandos maliciosos.
- **Depois:** Implementação obrigatória de **Consultas Parametrizadas (?)** através de ORM (SQLAlchemy) ou Prepared Statements, garantindo que o motor de banco de dados trate entradas apenas como dados, nunca como código executável.

### 🔑 Governança de Segredos (Secret Management)
- **Ação:** Saneamento de todas as *Hardcoded Secrets* (chaves de API, credenciais e `SECRET_KEY`).
- **Solução:** Migração para armazenamento em variáveis de ambiente controladas via ficheiro `.env` e biblioteca `python-dotenv`, impedindo a exposição acidental em repositórios de código.

---

## 3. Evidência de Validação (PoC - Proof of Concept)

A eficácia das correções foi validada através de testes de intrusão controlados, simulando vetores de ataque reais.

### Teste de Blindagem SQL
**Vetor de Ataque:** Tentativa de bypass de autenticação via `OR '1'='1'`.
```bash
curl -X GET "http://localhost:5000/recurso?id=1' OR '1'='1"