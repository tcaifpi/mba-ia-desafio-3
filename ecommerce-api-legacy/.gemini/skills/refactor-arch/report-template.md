# Relatório de Conclusão: Refatoração e Segurança (Fase 3)

**Responsável:** Tiago Aragão
**Projeto:** Ecommerce API Legacy (Node.js/Express)
**Status:** Concluído / Saneado ✅

---

## 1. Implementação da Arquitetura MVC
Para resolver o débito técnico do "God File" (antigo AppManager), a aplicação foi migrada para uma estrutura modular, garantindo a separação de responsabilidades (SoC):

* **src/models/**: Abstração da lógica de persistência e sanitização SQL (Ex: `User.js`).
* **src/controllers/**: Gestão da lógica de negócio e processamento de requisições.
* **src/routes/**: Roteamento centralizado e "magro" via `index.js`.
* **src/config/**: Centralização da conexão assíncrona com o SQLite.



[Image of MVC software architecture pattern]


## 2. Saneamento de Vulnerabilidades Críticas
As falhas de segurança detectadas na auditoria técnica foram corrigidas seguindo os padrões de Engenharia de Software:

* **SQL Injection**: Implementada a parametrização de queries (`?`) em todos os métodos de busca e remoção, neutralizando ataques via URL.
* **Gestão de Segredos**: Migração da `SECRET_KEY` e caminhos de base de dados para variáveis de ambiente utilizando a biblioteca `dotenv`.
* **Segurança de Hashing**: Substituição de algoritmos inseguros pelo `bcryptjs` com 10 rounds de salt.

## 3. Evidência de Validação (Teste de Intrusão)
Foi realizado um teste final para garantir que a vulnerabilidade de SQL Injection foi mitigada com sucesso.

**Comando executado no terminal:**
```bash
curl -X DELETE "http://localhost:3000/api/users/1%27%20OR%20%271%27%3D%271"