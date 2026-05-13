import os
from flask import Flask
from dotenv import load_dotenv
from routes.task_routes import task_bp
from routes.user_routes import user_bp
from database import init_db

# 1. Carrega variáveis de ambiente (Segurança: Resolve Hardcoded Secrets)
load_dotenv()

def create_app():
    app = Flask(__name__)

    # 2. Configurações Seguras
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'default-dev-key-ifpi-2026')
    app.config['JSON_AS_ASCII'] = False

    # 3. Inicializa o Banco de Dados
    with app.app_context():
        init_db()

    # 4. Registro de Blueprints (MVC: Desacoplamento de Rotas)
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(task_bp, url_prefix='/api/tasks')

    @app.route('/')
    def health_check():
        return {"status": "online", "message": "Task Manager API rodando no IFPI"}, 200

    return app

if __name__ == '__main__':
    app = create_app()
    PORT = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=PORT, debug=os.getenv('FLASK_DEBUG', 'False') == 'True')