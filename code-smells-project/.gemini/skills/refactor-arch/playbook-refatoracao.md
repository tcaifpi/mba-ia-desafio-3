Playbook de Refatoração: Estratégias de Transformação
Este guia define as diretrizes técnicas para converter padrões legados em código moderno, seguro e manutenível, conforme as melhores práticas de Engenharia de Software.

1. Segurança: SQL Injection
Cenário: Uso de f-strings ou concatenação direta em queries.
Ação: Implementar consultas parametrizadas (Prepared Statements).

Antes: cursor.execute(f"SELECT * FROM users WHERE email = '{email}'")

Depois: cursor.execute("SELECT * FROM users WHERE email = ?", (email,))

2. Secure Hashing (APIs Obsoletas)
Cenário: Uso de algoritmos de hash vulneráveis (MD5/SHA1) para senhas.
Ação: Migrar para padrões OWASP utilizando PBKDF2 ou Argon2.

Antes: hashlib.md5(password.encode()).hexdigest()

Depois: generate_password_hash(password, method='pbkdf2:sha256')

3. Gestão de Configuração (Hardcoded Secrets)
Cenário: Credenciais, chaves de API e segredos expostos diretamente no código.
Ação: Mover segredos para variáveis de ambiente utilizando arquivos .env.

Antes: SECRET_KEY = "minha-chave-secreta-123"

Depois: SECRET_KEY = os.getenv("SECRET_KEY")

4. Separação de Responsabilidades (MVC)
Cenário: Arquivos únicos (God Files) processando rotas, lógica e banco de dados simultaneamente.
Ação: Desmembrar o código em camadas de Model, View e Controller.

Antes: Um arquivo AppManager.js lidando com toda a lógica da aplicação.

Depois: Rotas apenas recebem a requisição e delegam para um Controller específico.

5. Tratamento de Erros Profissional
Cenário: Blocos try/except vazios ou que expõem detalhes internos (stack traces).
Ação: Implementar logs estruturados e retornos HTTP semânticos ao usuário.

Antes: except: pass

Depois: except Exception as e: logger.error(e); return jsonify({"error": "Internal Error"}), 500

6. Performance: N+1 Query Problem
Cenário: Realização de consultas ao banco de dados dentro de loops de repetição.
Ação: Utilizar JOINs ou carregar dados em lote (Eager Loading).

Antes: Consultar o perfil de cada usuário individualmente dentro de um loop.

Depois: SELECT * FROM users JOIN profiles ON users.id = profiles.user_id

7. Validação de Dados (Input Sanitization)
Cenário: Processamento de dados de entrada (request.json) sem validação de tipos ou campos.
Ação: Implementar esquemas de validação obrigatórios.

Antes: user_data = request.json

Depois: Uso de bibliotecas como Pydantic ou Marshmallow para validar a estrutura do JSON.

8. Padronização e Código Morto
Cenário: Variáveis com nomes genéricos e funções declaradas que nunca são chamadas.
Ação: Aplicar padrões de Clean Code e remover trechos de código inutilizados.

Antes: Variáveis como data, x, temp e funções comentadas "por segurança".

Depois: Nomes semânticos (ex: user_registration_date) e limpeza completa do repositório.