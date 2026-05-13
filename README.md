# MBA Full Cycle - Desafio 3: Refatoração de Projetos com IA (Gemini Skill)

Este repositório contém a entrega do Desafio 3, focado na utilização de Inteligência Artificial para auditoria técnica e refatoração arquitetural de três projetos distintos: um legado em Python, uma API de E-commerce em Node.js e um Gerenciador de Tarefas em Flask.

## 🚀 Estrutura do Desafio

O projeto foi dividido em três fases principais para cada um dos sistemas analisados:
1. **Análise de Contexto**: Identificação de tecnologias e mapeamento de dependências.
2. **Auditoria Técnica**: Identificação de "Code Smells", vulnerabilidades de segurança e gargalos de performance.
3. **Refatoração Estrutural**: Migração para o padrão **MVC (Model-View-Controller)** e correção de débitos técnicos.

## 📁 Projetos Analisados

### 1. Code Smells Project (Python)
- **Foco**: Organização de código espaguete.
- **Resultado**: Implementação completa de MVC, separando a lógica de banco de dados das rotas do sistema.

### 2. Ecommerce API Legacy (Node.js)
- **Foco**: Eliminação de "God Objects" e Segurança.
- **Resultado**: O arquivo centralizado `AppManager.js` foi desmembrado em Controllers específicos. Implementada proteção contra SQL Injection e tratamento de Hardcoded Secrets via variáveis de ambiente.

### 3. Task Manager API (Python/Flask)
- **Foco**: Segurança Crítica e Performance.
- **Resultado**: Substituição do algoritmo de hash **MD5** pelo `werkzeug.security` (PBKDF2). Otimização de performance com a identificação de N+1 Queries e correção de vulnerabilidades de injeção de SQL.

## 🤖 Engenharia de Prompt e IA

Para este desafio, foi desenvolvida uma **Gemini Skill** customizada (localizada em `.gemini/skills/refactor-arch/`), que automatizou a geração dos relatórios de auditoria localizados na pasta `/reports`.

### 🛠️ Notas de Troubleshooting (Desafios Técnicos)
Durante a execução no ambiente IDX/Nix, foram superados os seguintes obstáculos:
- **Conflito de Shell**: O comando de confirmação `y` foi interceptado pelo pacote de sistema `yakut`. A solução foi a confirmação via `yes` por extenso ou aplicação assistida das sugestões da IA.
- **Limitações de Escrita**: Devido a restrições de permissão de escrita de arquivos via CLI em certos módulos, a refatoração da Fase 3 foi realizada de forma assistida, onde a IA gerou o código refatorado e a implementação foi validada manualmente.

## 📊 Relatórios de Auditoria
Os diagnósticos detalhados podem ser encontrados em:
- [Relatório Projeto 1](./reports/audit-project-1.md)
- [Relatório Projeto 2](./reports/audit-project-2.md)
- [Relatório Projeto 3](./reports/audit-project-3.md)

---
**Desenvolvido por:** Tiago Cavalcante Aragão  
**Contexto:** MBA em Engenharia de Software com IA - Full Cycle