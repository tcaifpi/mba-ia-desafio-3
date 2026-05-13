# Playbook de Refatoração: Estratégias de Transformação

Este guia define como converter padrões legados em código moderno e seguro durante a Fase 3.

## ## 1. Segurança: SQL Injection
**Cenário Legado:** Uso de f-strings ou concatenação direta.
**Ação:** Substituir por consultas parametrizadas (Prepared Statements).

- **Antes (Python/Flask):**
  `cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")`
- **Depois (Python/Flask):**
  `cursor.execute("SELECT * FROM users WHERE email = %s", (email,))`

## ## 2. Gestão de Configuração
**Cenário Legado:** Credenciais e chaves expostas no código.
**Ação:** Mover para variáveis de ambiente e usar um arquivo `.env.example`.

- **Antes:** `app.config['SECRET_KEY'] = 'minha-chave-super-secreta-123'`
- **Depois:** 
  `import os`
  `app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default_fallback_key')`

## ## 3. Separação de Responsabilidades (MVC)
**Cenário Legado:** Rota processando lógica e banco de dados.
**Ação:** Delegar para Controller e Model.

- **Fluxo de Transformação:**
  1. O código de consulta SQL vai para uma função em `src/models/`.
  2. A lógica de decisão (if/else, cálculos) vai para `src/controllers/`.
  3. A rota em `src/routes/` apenas chama o controller e retorna o `jsonify`.

## ## 4. Tratamento de Erros Profissional
**Cenário Legado:** Try/Except vazio ou falta de retorno adequado.
**Ação:** Implementar logs e retornos HTTP semânticos.

- **Antes:** `except: pass`
- **Depois:**
  `except Exception as e:`
  `    logger.error(f"Erro ao processar pedido: {str(e)}")`
  `    return jsonify({"error": "Internal Server Error"}), 500`

## ## 5. Padronização de Nomenclatura
**Ação:** Normalizar para as convenções da linguagem (PEP 8 para Python, CamelCase para classes em JS).