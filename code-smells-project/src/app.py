import os
from flask import Flask, jsonify
from dotenv import load_dotenv

# 1. Carregamos as variáveis do arquivo .env (SECRET_KEY, etc.)
load_dotenv()

# 2. Importamos os Blueprints (nossas rotas organizadas)
from routes.product_routes import product_bp

def create_app():
    app = Flask(__name__)

    # 3. Configurações de Segurança
    # Nunca deixe a chave exposta! Pegamos do .env
    app.config['SECRET_KEY'] = os.getenv('SECRET_KEY', 'chave-padrao-de-seguranca')
    app.config['JSON_AS_ASCII'] = False # Garante acentos corretos no JSON

    # 4. Rota Inicial (Para evitar o erro 404 na raiz)
    @app.route('/')
    def index():
        return jsonify({
            "status": "Online",
            "message": "API do Desafio MBA - Refatoração MVC",
            "version": "1.0.0"
        }), 200

    # 5. Registro de Módulos (Blueprints)
    # Isso mantém o código modular. Cada domínio tem seu arquivo de rotas.
    app.register_blueprint(product_bp)

    return app

# Inicialização do Servidor
if __name__ == "__main__":
    app = create_app()
    
    # Em desenvolvimento usamos debug=True. 
    # Em produção (no IFPI, por exemplo), usaríamos um servidor como Gunicorn.
    app.run(
        host='0.0.0.0', 
        port=5000, 
        debug=True
    )