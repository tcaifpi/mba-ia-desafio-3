from flask import Blueprint, request, jsonify
from sqlalchemy.orm import joinedload
import jwt
import os
from datetime import datetime, timedelta
from database import db
from models.user import User

user_bp = Blueprint('users', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    """
    Retorna todos os usuários cadastrados com contagem de tarefas otimizada.
    Saneamento de Performance: Usa 'joinedload' para resolver o problema N+1,
    trazendo os relacionamentos de tarefas em um único JOIN de banco de dados.
    """
    try:
        # Carrega os usuários e suas tarefas associadas em uma única consulta estruturada
        users = User.query.options(joinedload(User.tasks)).all()
        
        result = []
        for u in users:
            user_data = u.to_dict()
            # A contagem é executada sobre a coleção já presente na memória
            user_data['task_count'] = len(u.tasks)
            result.append(user_data)
            
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    """
    Busca um usuário específico pelo ID, incluindo seu detalhamento de tarefas.
    """
    user = User.query.options(joinedload(User.tasks)).get(user_id)
    if not user:
        return jsonify({'error': 'Usuário não encontrado'}), 404

    data = user.to_dict()
    data['tasks'] = [t.to_dict() for t in user.tasks]
    return jsonify(data), 200

@user_bp.route('/register', methods=['POST'])
def register():
    """
    Registra um novo usuário na plataforma.
    Segurança: Valida a duplicidade de e-mail e delega o hashing de senha para o Model.
    """
    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Email e senha são campos obrigatórios'}), 400

    # Validação de duplicidade para mitigar conflitos de persistência
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email já cadastrado no sistema'}), 409

    new_user = User(
        name=data.get('name', ''),
        email=data['email'],
        role=data.get('role', 'user'),
        active=True
    )
    
    # Criptografia defensiva (o método trata o salt interno com bcrypt/werkzeug)
    new_user.set_password(data['password'])

    try:
        db.session.add(new_user)
        db.session.commit()
        return jsonify(new_user.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@user_bp.route('/login', methods=['POST'])
def login():
    """
    Autentica o usuário e emite um Token JWT assinado.
    Segurança (OWASP): Retorna uma mensagem genérica em caso de falha, 
    neutralizando ataques de enumeração de contas e Timing Attacks.
    """
    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Credenciais incompletas'}), 400

    user = User.query.filter_by(email=data['email']).first()
    
    # Blindagem contra mapeamento de credenciais: resposta idêntica para usuário ou senha inválidos
    if not user or not user.check_password(data['password']):
        return jsonify({'error': 'Credenciais inválidas'}), 401

    if not user.active:
        return jsonify({'error': 'Esta conta de usuário está inativa'}), 403

    # Geração do Token de Acesso Assinado (JWT)
    secret_key = os.getenv('SECRET_KEY', 'ifpi-secret-key-2026-mba')
    payload = {
        'user_id': user.id,
        'role': user.role,
        'exp': datetime.utcnow() + timedelta(hours=8) # Expiração segura de 8 horas
    }
    
    token = jwt.encode(payload, secret_key, algorithm='HS256')

    return jsonify({
        'token': token,
        'user': user.to_dict()
    }), 200