# Projeto de Refatoração: Code Smells & Dívida Técnica

**Responsável:** Tiago Aragão (Analista de TI)  
**Contexto:** MBA em Engenharia de Software com IA  
**Tecnologias:** Python, Flask, SQLite.

## 🎯 Objetivo
Este projeto consiste na auditoria e refatoração de uma aplicação de e-commerce ("Loja") que apresentava diversos *code smells* clássicos, dificultando a manutenção e a escalabilidade. O objetivo foi aplicar padrões de projeto (Design Patterns) e princípios SOLID para limpar o código.

## 🔍 Code Smells Identificados
Durante a auditoria inicial, foram detectados os seguintes problemas:

1. **Large Class / God Object:** Classes que acumulavam responsabilidades demais (ex: gerenciar estoque, processar pagamento e enviar e-mail no mesmo método).
2. **Long Method:** Métodos complexos com mais de 50 linhas, dificultando testes unitários.
3. **Data Clumps:** Grupos de dados que sempre apareciam juntos mas não estavam encapsulados em classes próprias.
4. **Hardcoded Secrets:** Credenciais expostas diretamente no código-fonte.

## 🛠️ Refatorações Aplicadas

- **Extract Method:** Divisão de funções gigantes em métodos menores e reutilizáveis.
- **Move Method:** Redistribuição de responsabilidades para as classes corretas (ex: lógica de preço movida para a classe Produto).
- **Injeção de Dependência:** Desacoplamento de serviços externos (Gateways de pagamento e serviços de Notificação).
- **Encapsulamento de Campo:** Proteção de atributos sensíveis das entidades de negócio.

## 🚀 Como Executar

1. **Ativar Ambiente Virtual:**
   ```bash
   source venv/bin/activate