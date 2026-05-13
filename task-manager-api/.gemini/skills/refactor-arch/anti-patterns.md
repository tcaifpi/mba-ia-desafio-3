# Catálogo de Anti-padrões e Heurísticas de Auditoria

Use esta lista para identificar violações de design e segurança durante a Fase 2.

## ## 1. Segurança e Integridade
- **SQL Injection:** Detecção de concatenação de strings ou f-strings diretamente em queries SQL (ex: `execute(f"SELECT * FROM users WHERE id = {id}")`).
- **Hardcoded Secrets:** Chaves de API, senhas de banco ou tokens expostos diretamente no código em vez de usar variáveis de ambiente (`.env`).
- **Exposição de Erros:** Blocos `except` que retornam o traceback completo para o usuário final ou logs que expõem dados sensíveis.

## ## 2. Arquitetura e Design (Code Smells)
- **Fat Routes / God Routes:** Endpoints que contêm lógica de negócio complexa, cálculos ou chamadas diretas ao banco de dados.
- **God Class / God File:** Arquivos únicos (como o `app.py` original) que gerenciam rotas, banco de dados e lógica de negócio simultaneamente.
- **Acoplamento Forte:** Funções que dependem de variáveis globais ou estados mutáveis externos para funcionar.
- **Falta de Tipagem/Validação:** Recebimento de dados de formulários ou JSON sem validação prévia de tipos ou campos obrigatórios.

## ## 3. Manutenibilidade
- **Código Morto:** Funções ou variáveis declaradas que nunca são chamadas.
- **Inconsistência de Nomenclatura:** Mistura de snake_case e camelCase, ou nomes de variáveis genéricos (ex: `data`, `var1`, `temp`).
- **Falta de Comentários em Lógicas Complexas:** Trechos de "código ninja" que realizam operações críticas sem documentação.

## ## 4. Performance
- **N+1 Query Problem:** Loops que realizam consultas ao banco de dados a cada iteração em vez de usar Joins ou Eager Loading.