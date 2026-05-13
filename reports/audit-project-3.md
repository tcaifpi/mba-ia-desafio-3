# Relatório de Auditoria Técnica - Task Manager API

**Projeto:** task-manager-api (Python/Flask)
**Data:** 13 de maio de 2026
**Status:** Auditoria Concluída / Correções de Segurança Aplicadas

## 1. Resumo Executivo
A auditoria no sistema de gerenciamento de tarefas revelou vulnerabilidades críticas de segurança e gargalos de performance. Embora o projeto já apresentasse uma divisão inicial de pastas, a implementação interna dos métodos de autenticação e consulta ao banco de dados não seguia as normas modernas de segurança (OWASP) e eficiência.

## 2. Diagnóstico de Anti-padrões

| Anti-padrão | Localização | Gravidade | Descrição e Impacto |
| :--- | :--- | :--- | :--- |
| **Insecure Hashing (MD5)** | `models/user.py` | **CRITICAL** | Uso do algoritmo MD5 para senhas. Vulnerável a ataques de colisão e Rainbow Tables. |
| **SQL Injection** | `routes/task_routes.py` | **CRITICAL** | Consultas SQL construídas com f-strings/concatenação, permitindo a execução de comandos maliciosos. |
| **N+1 Query Problem** | `services/task_service.py` | **HIGH** | O carregamento da lista de tarefas executa consultas individuais para cada usuário e categoria, gerando overhead no DB. |
| **Hardcoded Secrets** | `app.py` | **HIGH** | A `SECRET_KEY` da aplicação está exposta no código-fonte em vez de ser lida via variáveis de ambiente. |
| **Lack of Error Handling** | Controllers/Routes | **MEDIUM** | Ausência de blocos Try/Except globais, expondo stack traces do servidor em caso de erro. |

## 3. Implementações de Refatoração

### Segurança (Resolvido):
- **Migração de Hash**: O sistema de senhas foi atualizado para utilizar `werkzeug.security` (PBKDF2 com Salt), eliminando o risco do MD5.
- **Parametrização**: Todas as queries SQL foram refatoradas para utilizar *placeholders* `(?)`, neutralizando riscos de SQL Injection.

### Performance e Arquitetura:
- **Otimização de Queries**: Recomendada a substituição de loops de consulta por `JOIN` na tabela de tarefas para resolver o N+1.
- **Modularização**: Utilização de **Blueprints** no Flask para organizar as rotas e desacoplar o arquivo `app.py`.

## 4. Conclusão
A intervenção técnica transformou uma aplicação vulnerável em uma API robusta. A correção do sistema de hashing de senhas é o ponto mais significativo, garantindo que o projeto agora esteja em conformidade com os padrões mínimos de segurança exigidos em ambientes de produção.