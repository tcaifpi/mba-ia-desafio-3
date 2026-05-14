import os
import sys
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# Garante que o Python trate a pasta 'src' como a base dos módulos
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# IMPORTANTE: Como você está na raiz, o Python precisa saber 
# que deve procurar 'produto_bp' dentro do pacote 'routes' que está em 'src'
try:
    from routes.produto_routes import produto_bp
except ImportError as e:
    print(f"\n[ERRO DE ARQUITETURA] Falha ao carregar módulos: {e}")
    sys.exit(1)

load_dotenv()

def create_app():
    app = Flask(__name__)
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "chave-padrao-ifpi")
    CORS(app)
    app.register_blueprint(produto_bp)
    return app

if __name__ == "__main__":
    app = create_app()
    print("\n🚀 SERVIDOR INICIADO: http://127.0.0.1:5000\n")
    app.run(host="0.0.0.0", port=5000)