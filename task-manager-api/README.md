# Task Manager API — Governança, Segurança e Refatoração MVC

**Analista Responsável:** Tiago Aragão (Analista de TI)
**Instituição:** Instituto Federal do Piauí (IFPI) / MBA Engenharia de Software com IA
**Ambiente de Homologação:** Python 3.x | Flask | SQLAlchemy | SQLite | JWT

---

## 🚀 Sobre o Projeto
Este repositório contém a versão refatorada e saneada da **Task Manager API**. O projeto passou por uma rigorosa auditoria de segurança corporativa e engenharia de software para eliminação de débitos técnicos acentuados, transicionando de um modelo monolítico acoplado para uma arquitetura limpa baseada no padrão **MVC (Model-View-Controller)**.

As principais melhorias incluíram a mitigação de vulnerabilidades críticas do **OWASP Top 10** (como BOLA/IDOR e vazamento de credenciais) e o saneamento de severos gargalos de I/O em consultas ao banco de dados.

---

## 🛠️ Engenharia de Saneamento (Resumo de Impacto)
Conforme documentado detalhadamente no arquivo `audit-project-3.md`, as seguintes intervenções de infraestrutura foram consolidadas:

* **Segurança Arquitetural (Anti-BOLA/IDOR):** Acoplamento do middleware `@auth_required` para interceptação e validação de tokens JWT, forçando o escopo transacional seguro (`task.user_id != current_user.id`).
* **Gestão de Segredos:** Extração de credenciais de e-mail e chaves criptográficas (`SECRET_KEY`) hardcoded para isolamento dinâmico em arquivo `.env`.
* **Otimização de Consultas (Anti-N+1 Query):** Substituição de loops de busca iterativos pela estratégia de Eager Loading (`joinedload(User.tasks)`), unificando varreduras de banco de dados em um único `LEFT OUTER JOIN`.
* **Agregação Nativa em Banco:** Relatórios gerenciais convertidos para processamento nativo via queries estruturadas com `GROUP BY` e `func.count()`.

---

## 📦 Instalação e Inicialização do Sistema

Siga rigorosamente as diretrizes de terminal abaixo para instanciar a API em seu ambiente local Linux:

2. Isolar o Ambiente Virtual (Virtualenv)
Crie e ative uma instância de ambiente isolada para mitigar conflitos de dependências globais:

Bash
python3 -m venv venv
source venv/bin/activate
3. Instalar Dependências Homologadas
Instale os pacotes e drivers necessários definidos no manifesto do projeto (incluindo PyJWT e python-dotenv):

Bash
pip install -r requirements.txt
4. Executar a Aplicação
Inicie o servidor web do Flask. O ORM executará automaticamente o db.create_all(), provisionando o banco de dados relacional SQLite (taskmanager.db) de forma autônoma:

Bash
python3 app.py
O servidor estará ativo e escutando por requisições em: http://localhost:5000/

