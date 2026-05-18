import os
from flask import Flask, jsonify
from dotenv import load_dotenv
from database import db
from routes.task_routes import task_bp
from routes.user_routes import user_bp
from routes.report_routes import report_bp

# 1. Carregamento de Configurações Sensíveis
# Garante que chaves de API e segredos não fiquem expostos no código
load_dotenv()

def create_app():
    app = Flask(__name__)

    # 2. Configurações de Segurança e Infraestrutura
    # A SECRET_KEY é vital para a assinatura dos tokens JWT e segurança da sessão
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'ifpi-secret-key-default-2026')
    app.config['SQLALCHEMY_DATABASE_URI'] = os.getenv('DATABASE_URL', 'sqlite:///taskmanager.db')
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    app.config['JSON_AS_ASCII'] = False

    # 3. Inicialização do Banco de Dados (Padrão SQLAlchemy)
    # Separação da instância do banco da criação da app (evita circular imports)
    db.init_app(app)
    with app.app_context():
        db.create_all()

    # 4. Registro de Módulos (Blueprints - Camada de Rotas MVC)
    # Organização por domínio para facilitar auditorias e escalabilidade
    app.register_blueprint(user_bp, url_prefix='/api/users')
    app.register_blueprint(task_bp, url_prefix='/api/tasks')
    app.register_blueprint(report_bp, url_prefix='/api/reports')

    # 5. Health Check / Rota Raiz
    @app.route('/')
    def status():
        return jsonify({
            "status": "operacional",
            "ambiente": os.getenv('FLASK_ENV', 'development'),
            "analista_responsavel": "Tiago Aragão",
            "projeto": "Task Manager API - Refatoração MVC"
        }), 200

    # 6. Tratamento Global de Erros (Segurança)
    @app.errorhandler(401)
    def unauthorized(e):
        return jsonify({'error': 'Acesso negado: Token JWT inválido ou ausente'}), 401

    @app.errorhandler(404)
    def not_found(e):
        return jsonify({'error': 'Recurso não encontrado'}), 404

    return app

if __name__ == '__main__':
    app = create_app()
    # No ambiente IFPI, rodamos geralmente na porta 5000 para Flask
    app.run(host='0.0.0.0', port=5000, debug=True)