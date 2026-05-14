# Task Manager API - Refatoração e Auditoria

**Responsável:** Tiago Aragão (Analista de TI - IFPI)  
**Projeto:** Gestão de Tarefas com Foco em Segurança e Performance  
**Tecnologias:** Python, Flask, SQLAlchemy, JWT, SQLite.

## 🚀 Sobre o Projeto
Este projeto passou por um processo de auditoria e refatoração profunda para sanar vulnerabilidades críticas e otimizar a performance em ambientes institucionais. O sistema agora segue o padrão MVC (Model-View-Controller) e utiliza autenticação JWT para garantir a integridade dos dados.

## 🛠️ Melhorias Implementadas (Resumo da Auditoria)
Conforme detalhado no arquivo `audit-project-3.md`, as seguintes ações foram realizadas:

- **Segurança (IDOR & Secrets):** Implementação de middleware JWT para proteção de rotas e migração de credenciais sensíveis para variáveis de ambiente (.env).
- **Performance (N+1 Queries):** Otimização de listagens de usuários e tarefas utilizando *Eager Loading* (`joinedload`), reduzindo o overhead de banco de dados.
- **Eficiência de Relatórios:** Migração de processamento pesado em Python para agregações nativas SQL (`GROUP BY`).
- **Arquitetura:** Desacoplamento total via Blueprints e saneamento de lógica nos modelos.

## 📦 Instalação e Configuração

1. **Clonar o Repositório:**
   ```bash
   git clone <url-do-repositorio>
   cd task-manager-api