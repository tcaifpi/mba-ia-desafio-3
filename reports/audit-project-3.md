# Relatório de Auditoria Técnica, Segurança e Governança de TI
**Projeto:** Task Manager API (Refatoração e Saneamento de Débitos Técnicos)  
**Analista Responsável:** Tiago Aragão  
**Instituição:** Instituto Federal do Piauí (IFPI) / MBA Engenharia de Software com IA  
**Data da Auditoria:** 18 de maio de 2026  
**Status:** Saneado e Homologado ✅  

---

## 1. Segurança, Autenticação e Governança de Dados

### 🔐 Saneamento de Secrets (Variáveis de Ambiente)
* **Cenário Legado:** Dados sensíveis de infraestrutura e credenciais de servidores de e-mail encontravam-se rigidamente codificados (*hardcoded*) nos arquivos de serviço.
* **Solução Implementada:** Centralização cirúrgica de todas as variáveis críticas no arquivo oculto `.env`, isoladas do controle de versão. O arquivo `app.py` realiza a inicialização segura através da biblioteca `python-dotenv` (`load_dotenv()`).

### 🛡️ Blindagem Contra Ataques de IDOR / BOLA (OWASP Top 10)
* **Cenário Legado:** As rotas de mutação e remoção aceitavam identificadores arbitrários na URL, permitindo que usuários mal-intencionados manipulassem IDs para alterar ou apagar registros de terceiros.
* **Solução Implementada:** Introdução do middleware `@auth_required` nos endpoints críticos de `task_routes.py`. A API agora força a validação estrita de escopo (`task.user_id != current_user.id`), bloqueando tentativas de intrusão com o código de estado `403 Forbidden`.

### 🔑 Mecanismo de Hashing de Credenciais
* **Cenário Legado:** Armazenamento de senhas vulnerável ou exposição de dados em texto limpo.
* **Solução Implementada:** Absorção de criptografia defensiva diretamente na camada de persistência (`user.py`). A geração e a checagem de senhas utilizam os métodos `generate_password_hash` e `check_password_hash` da biblioteca `werkzeug.security`, aplicando criptografia assimétrica com salt dinâmico.

---

## 2. Otimização de Performance e Eficiência Computacional

### 📉 Resolução do Problema de N+1 Queries (I/O Optimization)
* **Cenário Legado:** A listagem de usuários forçava o ORM a realizar uma nova requisição síncrona ao banco de dados para cada linha retornada a fim de computar as tarefas vinculadas, gerando sobrecarga e travamento de I/O no SQLite.
* **Solução Implementada:** Aplicação da estratégia de carregamento antecipado (**`joinedload(User.tasks)`**) na busca em lote dentro de `user_routes.py`. Múltiplas consultas concorrentes foram unificadas em um único e eficiente `LEFT OUTER JOIN` em nível de banco de dados, processando a contagem de forma instantânea em memória.

### 📊 Agregação SQL Nativa (Group By Engine)
* **Cenário Legado:** Relatórios gerenciais e dashboards dependiam de laços de repetição lentos em Python (`for` / `if`) para filtrar e computar métricas de volume.
* **Solução Implementada:** Reescripta completa do arquivo `report_routes.py`. O cálculo de volumetria por status e prioridade foi delegado inteiramente ao motor do banco de dados utilizando funções agregadoras nativas (`func.count(Task.id)`) acopladas a cláusulas `group_by`.

---

## 3. Organização Arquitetural e Manutenibilidade (Pattern MVC)

### 📂 Desacoplamento Arquitetural (Modular Blueprints)
* **Cenário Legado:** Código monolítico altamente acoplado, com rotas, regras de negócio e infraestrutura disputando o mesmo arquivo principal.
* **Solução Implementada:** Segregação modular do projeto através de sub-rotas estruturadas via **Blueprints** (`user_bp`, `task_bp`, `report_bp`) encapsuladas e registradas unicamente no factory do `app.py`.

### 🧠 Princípio da Responsabilidade Única (Fat Model Pattern)
* **Cenário Legado:** Controladores inflados assumindo validações primitivas de dados.
* **Solução Implementada:** Transferência da lógica de validação de estados (`validate_status`), faixas de criticidade (`validate_priority`) e monitoramento de prazos de expiração (`is_overdue`) para o escopo interno da classe `Task` em `models/task.py`, garantindo um código limpo (*Clean Code*) nas rotas.

---

## 4. Matriz de Endpoints Homologados

| Módulo | Endpoint HTTP | Proteção Requerida | Propósito Técnico |
| :--- | :--- | :--- | :--- |
| **Users** | `GET /api/users` | Nenhuma (Interno) | Listagem consolidada livre de N+1. |
| **Users** | `POST /api/users` | Validação Duplicidade | Registro de usuário com autocriptografia. |
| **Users** | `POST /api/login` | Resposta Opaca | Autenticação imune a Timing Attacks. |
| **Tasks** | `POST /api/tasks` | `@auth_required` (JWT) | Injeção implícita do dono do recurso. |
| **Tasks** | `PUT /api/tasks/<id>`| `@auth_required` + IDOR | Atualização segura e restrita ao proprietário. |
| **Tasks** | `DELETE /api/tasks