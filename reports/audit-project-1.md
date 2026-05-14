# Auditoria Técnica de Código — Projeto Loja API

**Auditor:** Tiago Aragão
**Data:** 14 de maio de 2026
**Escopo:** Avaliação de Segurança e Arquitetura (Fase 1)

## 1. Vulnerabilidades de Segurança Identificadas
Durante a análise estática do código original, foram detectadas falhas graves que expõem o sistema a ataques externos:

* **SQL Injection [CRITICAL]**: O uso de concatenação de strings para montar queries SQL permite que usuários malintencionados executem comandos arbitrários no banco de dados.
* **Exposição de Segredos [HIGH]**: A `SECRET_KEY` do Flask e credenciais de banco de dados estão "hardcoded" no arquivo principal, facilitando o vazamento de informações em caso de acesso ao repositório.

## 2. Débitos Técnicos e Anti-padrões
A estrutura do projeto apresenta problemas de manutenção que impedem a escalabilidade:

* **God File (Objeto Divino)**: Toda a lógica da aplicação (rotas, persistência e regras de negócio) está centralizada no `app.py`. Isso viola o princípio de responsabilidade única.
* **Acoplamento Forte**: A falta de uma camada de abstração para o banco de dados impede a troca de tecnologias ou a realização de testes unitários isolados.
* **Tratamento de Erros Inexistente**: O sistema não possui validação de entradas, resultando em erros internos (HTTP 500) que expõem o stack trace para o cliente final.

## 3. Recomendações de Mitigação
Para sanear o projeto, as seguintes ações são obrigatórias:
1. Implementar o padrão **MVC** (Model-View-Controller) para desacoplar as camadas.
2. Utilizar **Prepared Statements** (parametrização) em todas as interações com o SQLite.
3. Migrar configurações sensíveis para um arquivo de ambiente (`.env`).