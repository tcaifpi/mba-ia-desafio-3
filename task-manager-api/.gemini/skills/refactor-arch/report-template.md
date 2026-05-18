# Relatório de Conclusão: Refatoração, Performance e Segurança (Desafio 3)

**Responsável:** Tiago Aragão  
**Cargo:** Analista de Tecnologia da Informação  
**Projeto:** Task Manager API  
**Status:** Concluído / Saneado em Homologação ✅  

---

## 1. Implementação da Arquitetura MVC e Desacoplamento
A estrutura monolítica original foi completamente segmentada seguindo o padrão de arquitetura **MVC (Model-View-Controller)**, eliminando o acoplamento rígido de código e distribuindo as responsabilidades de forma limpa:

* **`models/`**: Contém as entidades e regras de negócio essenciais (`user.py`, `task.py`, `category.py`). Toda a validação de integridade de dados (como estados e prioridades de tarefas) foi movida para esta camada.
* **`routes/` (Controllers/Blueprints)**: Isolamento dos pontos de entrada e fluxos da API em módulos independentes (`user_routes.py`, `task_routes.py`, `report_routes.py`), centralizados dinamicamente através do arquivo principal `app.py`.
* **`utils/` (Middlewares)**: Componentes transversais de segurança, como o interceptador de tokens de acesso.

---

## 2. Saneamento de Vulnerabilidades Críticas (OWASP Top 10)

### 🛡️ Proteção Contra BOLA / IDOR (Broken Object Level Authorization)
* **Falha Detectada:** Usuários autenticados conseguiam adulterar ou apagar tarefas pertencentes a outras contas simplesmente manipulando o parâmetro de ID numérico exposto na URL.
* **Mitigação Aplicada:** Acoplamento do decorador de segurança `@auth_required` em `task_routes.py`. O sistema passou a injetar o contexto seguro do utilizador logado (`current_user`) diretamente pelo token JWT e a validar de forma estrita a propriedade antes de qualquer operação em banco (`task.user_id != current_user.id`).

### 🔑 Armazenamento Seguro de Credenciais e Gestão de Segredos
* **Falha Detectada:** Armazenamento inseguro de senhas e exposição de credenciais de infraestrutura em texto limpo no código.
* **Mitigação Aplicada:** Migração da chave criptográfica do sistema (`SECRET_KEY`) e dados do servidor de e-mail para o arquivo isolado `.env`. Na camada de dados (`user.py`), a gravação e checagem de senhas passaram a utilizar criptografia assimétrica forte através dos métodos `generate_password_hash` e `check_password_hash` da biblioteca `werkzeug.security`.

---

## 3. Otimização de Performance e I/O

### 📉 Mitigação do Anti-padrão N+1 Queries
* **Cenário Crítico:** Na listagem de usuários, o ORM executava uma consulta SQL síncrona separada para cada linha retornada para contar as tarefas de cada perfil, gerando alto overhead.
* **Mitigação Aplicada:** Implementação da técnica de *Eager Loading* utilizando o método **`joinedload(User.tasks)`** em `user_routes.py`. A varredura foi unificada num único `LEFT OUTER JOIN` executado diretamente pelo motor do banco de dados, computando os totais em memória instantaneamente.

### 📊 Agregação de Dados Nativa (GROUP BY Engine)
* **Cenário Crítico:** Relatórios gerenciais processavam laços de repetição síncronos e lentos (`for` / `if`) em Python para agrupar e calcular volumetria de tarefas.
* **Mitigação Aplicada:** O módulo `report_routes.py` foi reescrito para delegar toda a agregação matemática ao banco de dados utilizando cláusulas estruturadas `group_by` associadas a funções nativas de contagem (`func.count(Task.id)`).

---

## 4. Evidência de Validação (Teste de Intrusão)

Para homologar a barreira anti-IDOR/BOLA e garantir que um usuário não consiga intervir nas tarefas de terceiros, simulou-se um ataque de deleção forçada via terminal:

**Comando Executado (Ataque):**
```bash
curl -X DELETE http://localhost:5000/api/tasks/99 \
     -H "Authorization: Bearer <TOKEN_JWT_ATACANTE>" \
     -H "Accept: application/json"