# 🛡️ Relatório de Conformidade Técnica e Segurança

**Responsável:** Tiago Aragão (Analista de TI)  
**Projeto:** [Nome do Projeto]  
**Status:** 🟢 Saneado e Auditado

---

## 1. Implementação da Arquitetura MVC (Modularização)
O sistema foi migrado de uma estrutura monolítica ("God File") para o padrão **MVC (Model-View-Controller)**, eliminando o acoplamento excessivo e garantindo a escalabilidade da solução:

* **📦 Models (Camada de Dados):** Centralização da lógica de persistência e esquemas de dados. Inclui a sanitização rigorosa de entradas antes de qualquer interação com o banco.
* **⚙️ Controllers (Lógica de Negócio):** Isolamento das regras de negócio, garantindo que o processamento de dados ocorra de forma independente da interface de exposição.
* **🛣️ Routes (Definição de Endpoints):** Mapeamento claro de recursos e verbos HTTP, facilitando a governança e a futura expansão da API.

> **Benefício:** Redução da dívida técnica e facilitação de testes unitários e manutenção.

---

## 2. Saneamento de Vulnerabilidades Críticas

### 💉 Mitigação de SQL Injection
- **Problema:** Queries construídas via concatenação de strings eram vulneráveis a injeções maliciosas.
- **Solução:** Implementação obrigatória de **Consultas Parametrizadas (?)**. Todas as requisições agora tratam os inputs de utilizador como dados literais, neutralizando a execução de comandos não autorizados no banco de dados.

### 🔑 Gestão de Segredos (Secret Management)
- **Problema:** Credenciais críticas e chaves de segurança estavam expostas diretamente no código-fonte.
- **Solução:** Saneamento total de *Hardcoded Secrets*. Migração de chaves como `SECRET_KEY` e credenciais de e-mail para o ficheiro `.env`, gerido através de variáveis de ambiente seguras.

---

## 3. Evidência de Validação (Prova de Conceito)

Para validar a integridade das correções, foram realizados testes de intrusão e validação de permissões:

### Teste de Blindagem SQL
**Vetor de Ataque:** Tentativa de bypass via manipulação de parâmetros.
```bash
curl -X GET "http://localhost:5000/recurso?id=1' OR '1'='1"