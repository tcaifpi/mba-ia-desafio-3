import os
from flask import Flask, jsonify
from dotenv import load_dotenv
from database import db
from routes.task_routes import task_bp
from routes.user_routes import user_bp
from routes.report_routes import report_bp

# 1. Carregamento de Configurações Sensíveis
# Essencial para que o auth.py e o notification_service funcionem com segurança
load_dotenv()

def create_app():
    app = Flask(__name__)

    # 2. Configurações de Segurança e Infraestrutura
    # A SECRET_KEY é vital para a assinatura dos tokens JWT em utils/auth.py
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'ifpi-secret-key-2026-mba')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///taskmanager.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_AS_ASCII'] = False

    # 3. Inicialização do Banco de Dados (Padrão SQLAlchemy)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # 4. Registro de Módulos (Blueprints)
    # Organização MVC para facilitar a manutenção e auditorias futuras
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(task_bp, url_prefix='/api/tasks')
    app.register_blueprint(report_bp, url_prefix='/api/reports')

    # 5. Health Check / Rota Raiz
    @app.route('/')
    def status():
        return jsonify({
            "status": "operacional",
            "ambiente": os.getenv('FLASK_ENV', 'development'),
            "instituicao": "IFPI - Gestão de TI",
            "analista_responsavel": "Tiago Aragão"
        }), 200

    # Tratamento Global de Erros de Autenticação (Opcional)
    @app.errorhandler(401)
    def unauthorized(e):
        return jsonify({'error': 'Acesso negado: Token inválido ou ausente'}), 401

    return app

if __name__ == '__main__':
    app = create_app()
    # Configuração de porta dinâmica para deploys em servidores internos
    PORT = int(os.getenv('PORT', 5000))
    DEBUG_MODE = os.getenv('FLASK_DEBUG', 'False').lower() == 'true'
    
    app.run(host='0.0.0.0', port=PORT, debug=DEBUG_MODE)