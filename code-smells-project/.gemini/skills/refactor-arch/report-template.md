# Relatório de Conclusão: Refatoração e Segurança (Fase 3)

**Responsável:** Tiago Aragão  
**Projeto:** API de Gerenciamento de Produtos  
**Status:** Concluído / Saneado  

---

## 1. Implementação da Arquitetura MVC
Para resolver o problema do "God File", a aplicação foi migrada para uma estrutura modular, garantindo a separação de responsabilidades:

* **src/models/**: Toda a lógica de acesso a dados e sanitização SQL.
* **src/controllers/**: Lógica de negócio e tratamento das requisições.
* **src/routes/**: Definição dos endpoints e roteamento da API.



[Image of MVC software architecture pattern]


## 2. Saneamento de Vulnerabilidades Críticas
As falhas de segurança detectadas na auditoria técnica (`audit-project-1.md`) foram corrigidas conforme os padrões da indústria:

* **SQL Injection**: Implementada a parametrização de queries (`?`) em todos os métodos de busca e inserção no banco de dados.
* **Gestão de Segredos**: Migração da `SECRET_KEY` para variáveis de ambiente utilizando `.env` e a biblioteca `python-dotenv`.

## 3. Evidência de Validação (Teste de Intrusão)
Foi realizado um teste final para garantir que a vulnerabilidade de SQL Injection foi mitigada. 

**Comando executado:**
```bash
curl "[http://127.0.0.1:5000/produtos?id=1](http://127.0.0.1:5000/produtos?id=1)' OR '1'='1"

