import os
import sys
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# Configuração de Path para reconhecer a pasta 'src'
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# Importação das Rotas (Blueprints)
try:
    from routes.produto_routes import produto_bp
except ImportError as e:
    print(f"\n[ERRO] Falha ao carregar módulos: {e}")
    sys.exit(1)

load_dotenv()

def create_app():
    app = Flask(__name__)
    # Proteção de Segredos: Hardcoded Secrets [CRITICAL] corrigido
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "chave-ifpi-2026")
    CORS(app)

    # Registro de Rotas (MVC)
    app.register_blueprint(produto_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    print("\n🚀 SERVIDOR ONLINE: http://127.0.0.1:5000")
    app.run(host="0.0.0.0", port=5000)