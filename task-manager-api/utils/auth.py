import jwt
import os
from functools import wraps
from flask import request, jsonify
from datetime import datetime, timedelta
from models.user import User

# Segurança: A SECRET_KEY deve ser lida do .env para evitar exposição (Saneamento de Secrets)
SECRET_KEY = os.getenv('SECRET_KEY', 'ifpi-secret-key-2026-mba')

def generate_token(user_id):
    """
    Gera um token JWT com validade de 24 horas para o utilizador.
    """
    try:
        payload = {
            'exp': datetime.utcnow() + timedelta(hours=24),
            'iat': datetime.utcnow(),
            'sub': user_id
        }
        return jwt.encode(payload, SECRET_KEY, algorithm='HS256')
    except Exception as e:
        return str(e)

def auth_required(f):
    """
    Middleware de autenticação.
    Verifica se o token é válido e injeta o objeto current_user na rota.
    """
    @wraps(f)
    def decorated(*args, **kwargs):
        token = None

        # O token deve ser enviado no Header 'Authorization: Bearer <token>'
        if 'Authorization' in request.headers:
            auth_header = request.headers['Authorization']
            try:
                token = auth_header.split(" ")[1]
            except IndexError:
                return jsonify({'error': 'Formato do token inválido. Use Bearer <token>'}), 401

        if not token:
            return jsonify({'error': 'Token de autenticação ausente'}), 401

        try:
            # Descodificação segura do token
            data = jwt.decode(token, SECRET_KEY, algorithms=['HS256'])
            current_user = User.query.get(data['sub'])
            
            if not current_user:
                return jsonify({'error': 'Utilizador inexistente'}), 401
            
            if not current_user.active:
                return jsonify({'error': 'Conta de utilizador inativa'}), 401
                
        except jwt.ExpiredSignatureError:
            return jsonify({'error': 'Sessão expirada. Por favor, faça login novamente'}), 401
        except jwt.InvalidTokenError:
            return jsonify({'error': 'Token inválido ou corrompido'}), 401

        # Injeta o utilizador autenticado como o primeiro argumento da função da rota
        return f(current_user, *args, **kwargs)

    return decorated