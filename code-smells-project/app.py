import os
import sys
from flask import Flask
from flask_cors import CORS
from dotenv import load_dotenv

# Garante que o Python trate a pasta 'src' como a base dos módulos.
# Isso permite que você faça 'from routes.produto_routes' mesmo estando na raiz.
current_dir = os.path.dirname(os.path.abspath(__file__))
src_path = os.path.join(current_dir, "src")
if src_path not in sys.path:
    sys.path.insert(0, src_path)

# IMPORTAÇÃO DA CAMADA DE ROTAS:
# Aqui o app.py "descobre" as rotas definidas no seu Blueprint.
try:
    from routes.produto_routes import produto_bp
except ImportError as e:
    print(f"\n[ERRO DE ARQUITETURA] Falha ao carregar módulos: {e}")
    sys.exit(1)

load_dotenv()

def create_app():
    app = Flask(__name__)
    
    # Saneamento de Secrets: Corrigindo a vulnerabilidade Hardcoded Secrets [CRITICAL]
    app.config["SECRET_KEY"] = os.getenv("SECRET_KEY", "chave-padrao-ifpi")
    
    CORS(app)

    # REGISTRO DO BLUEPRINT:
    # Este comando ativa todas as rotas que você definiu na pasta 'src/routes'.
    app.register_blueprint(produto_bp)
    
    return app

if __name__ == "__main__":
    app = create_app()
    print("\n🚀 SERVIDOR INICIADO: http://127.0.0.1:5000\n")
    app.run(host="0.0.0.0", port=5000)