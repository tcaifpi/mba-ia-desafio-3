# Auditoria Técnica - Task Manager API (Python)

| Anti-padrão | Localização | Gravidade | Resolução |
| :--- | :--- | :--- | :--- |
| **MD5 Hashing** | `models/user.py` | **CRITICAL** | Substituído por Werkzeug (PBKDF2). |
| **SQL Injection** | `routes/task_routes.py` | **CRITICAL** | Parametrização de queries com `?`. |
| **N+1 Query** | `services/task_service.py` | **HIGH** | Implementação de JOIN na busca de tarefas. |