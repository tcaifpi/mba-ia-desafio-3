1. Segurança e Governança de Dados
Saneamento de Secrets: Eliminamos as senhas em texto plano do notification_service.py, movendo-as para variáveis de ambiente.

Blindagem contra IDOR: Implementamos o middleware JWT para garantir que um usuário não possa deletar ou editar tarefas de terceiros.

Criptografia de Senhas: Substituímos métodos inseguros pela biblioteca werkzeug.security com hashing PBKDF2.

🚀 2. Otimização de Performance (Eficiência do IFPI)
Resolução do N+1: As rotas de listagem foram otimizadas com joinedload, consolidando múltiplas consultas ao banco em uma única operação.

Agregação SQL: Os relatórios em report_routes.py deixaram de usar loops lentos em Python para utilizar o processamento nativo do banco de dados via GROUP BY.

📂 3. Organização Arquitetural (MVC)
Desacoplamento: As rotas foram organizadas em Blueprints no app.py, facilitando a manutenção futura.

Lógica no Model: Cálculos de status e atrasos foram movidos para a classe Task, limpando os controladores.