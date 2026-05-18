# Catálogo de Anti-Patterns e Vulnerabilidades

Este documento cataloga 8 anti-padrões e falhas de segurança identificados na base de código legada do sistema de e-commerce, classificados pelo nível de severidade.

**1. Credenciais Expostas (Hardcoded Secrets)**
* **Severidade:** CRITICAL
* **Descrição:** Armazenamento de palavras-passe de base de dados e chaves de API de pagamento diretamente no código-fonte, permitindo o comprometimento total da infraestrutura em caso de fuga do código.

**2. Injeção de SQL (SQL Injection)**
* **Severidade:** CRITICAL
* **Descrição:** Construção de consultas à base de dados (`loja.db`) através da concatenação direta de strings com os inputs do utilizador, permitindo a execução de comandos maliciosos e o roubo de dados.

**3. Uso de APIs Deprecated (Obsoletas/Inseguras)**
* **Severidade:** HIGH
* **Descrição:** Utilização de bibliotecas e algoritmos descontinuados (ex: `hashlib.md5` para hashing de senhas de clientes), que já possuem vulnerabilidades conhecidas e não recebem patches de segurança.

**4. Padrão N+1 Query**
* **Severidade:** HIGH
* **Descrição:** Má utilização do acesso aos dados, onde o sistema faz uma consulta principal para listar as encomendas e, dentro de um ciclo, faz uma nova consulta individual para carregar os produtos de cada encomenda, sobrecarregando o servidor.

**5. Objeto Deus (God Object / God Class)**
* **Severidade:** MEDIUM
* **Descrição:** A existência de uma classe `LojaManager` massiva que centraliza a gestão de stock, o processamento de pagamentos, o envio de e-mails e a ligação à base de dados, quebrando o Princípio de Responsabilidade Única (SRP).

**6. Tratamento Genérico de Exceções (Catch-All Exception)**
* **Severidade:** MEDIUM
* **Descrição:** Blocos `try/except` que capturam exceções genéricas (ex: `except Exception: pass`) durante o checkout, silenciando falhas críticas de gateway de pagamento sem gerar logs de auditoria.

**7. Método Longo (Long Method)**
* **Severidade:** LOW
* **Descrição:** O método `processar_checkout()` possui mais de 200 linhas, misturando validação de carrinho, cálculo de portes e gravação de faturas, dificultando a manutenção e a criação de testes unitários.

**8. Aglomerados de Dados (Data Clumps)**
* **Severidade:** LOW
* **Descrição:** Parâmetros como `rua`, `cidade`, `codigo_postal` e `distrito` são passados repetidamente em conjunto para vários métodos de entrega, em vez de serem encapsulados num único objeto estruturado.