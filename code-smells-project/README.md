# Projeto de Refatoração: Code Smells & Dívida Técnica

**Responsável:** Tiago Aragão (Analista de TI)  
**Contexto:** MBA em Engenharia de Software com IA  
**Tecnologias:** Python, Flask, SQLite.

## 🎯 Objetivo
Este projeto consiste na auditoria e refatoração de uma aplicação de e-commerce ("Loja") que apresentava diversos *code smells* clássicos e vulnerabilidades de segurança, dificultando a manutenção e a escalabilidade. O objetivo foi aplicar padrões de projeto (Design Patterns), princípios SOLID e o padrão arquitetural MVC para sanear o sistema.

## 🔍 Code Smells & Vulnerabilidades Identificadas
Durante a auditoria inicial (detalhada no `audit-project-1.md`), foram detectados os seguintes problemas:

1. **Large Class / God Object:** O arquivo `app.py` centralizava todas as responsabilidades (rotas, lógica e banco).
2. **SQL Injection [CRITICAL]:** Consultas ao banco via concatenação de strings.
3. **Hardcoded Secrets [HIGH]:** Credenciais e chaves de segurança expostas diretamente no código.
4. **Long Method:** Métodos complexos dificultando testes unitários.
5. **Data Clumps:** Grupos de dados repetitivos não encapsulados.

## 🛡️ Auditoria de Segurança e Arquitetura MVC
A refatoração não apenas limpou o código, mas reestruturou a governança da aplicação seguindo as melhores práticas:

- **Migração para MVC:** Desacoplamento total entre Models (Persistência), Controllers (Lógica) e Routes (Endpoints).
- **Prevenção de SQL Injection:** Substituição de strings dinâmicas por consultas parametrizadas (`?`) em todos os Models.
- **Gestão de Segredos:** Uso de variáveis de ambiente via `.env` para proteger a `SECRET_KEY` e chaves institucionais.
- **Tratamento de Erros:** Implementação de retornos HTTP adequados (ex: 404 para recursos não encontrados) em vez de erros genéricos 500.

## 🛠️ Refatorações Aplicadas
- **Extract Method:** Divisão de funções gigantes em métodos menores e coesos.
- **Move Method:** Redistribuição de responsabilidades para as classes corretas.
- **Injeção de Dependência:** Desacoplamento de serviços externos e de banco de dados.

## 📂 Estrutura Final do Projeto
```text
code-smells-project/
├── app.py                # Inicialização e Registro de Blueprints
├── .env                  # Gestão de Variáveis Sensíveis (Protegido)
├── src/
│   ├── controllers/      # Lógica de negócio (Orquestração)
│   ├── models/           # Camada de Dados (SQL Parametrizado)
│   └── routes/           # Mapeamento de Endpoints (Clean Routes)
├── docs/                 # Documentação (audit-project-1.md, anti-patterns.md)
└── loja.db               # Base de dados sanitizada

🚀 Como Executar
Ativar Ambiente Virtual:

Bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# ou
.\venv\Scripts\activate   # Windows
Instalar Dependências:

Bash
pip install -r requirements.txt
Iniciar Servidor:

Bash
python app.py