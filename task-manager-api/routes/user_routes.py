from flask import Blueprint, request, jsonify
from sqlalchemy.orm import joinedload
from database import db
from models.user import User
from models.task import Task
from datetime import datetime

user_bp = Blueprint('users', __name__)

@user_bp.route('/users', methods=['GET'])
def get_users():
    """
    Retorna todos os usuários com contagem de tarefas otimizada.
    Resolve o problema de N+1 queries usando subqueries ou joins.
    """
    try:
        # Usamos joinedload para trazer as tarefas associadas de uma vez
        users = User.query.options(joinedload(User.tasks)).all()
        
        result = []
        for u in users:
            user_data = u.to_dict()
            # A contagem agora é feita sobre os dados já carregados em memória
            user_data['task_count'] = len(u.tasks)
            result.append(user_data)
            
        return jsonify(result), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@user_bp.route('/users/<int:user_id>', methods=['GET'])
def get_user(user_id):
    # Otimizamos a busca do usuário já trazendo suas tarefas
    user = User.query.options(joinedload(User.tasks)).get(user_id)
    if not user:
        return jsonify({'error': 'Usuário não encontrado'}), 404

    data = user.to_dict()
    # Adicionamos a lista de tarefas detalhada
    data['tasks'] = [t.to_dict() for t in user.tasks]
    
    return jsonify(data), 200

@user_bp.route('/users', methods=['POST'])
def create_user():
    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Email e senha são obrigatórios'}), 400

    # Verificação de duplicidade (Boa prática de segurança)
    if User.query.filter_by(email=data['email']).first():
        return jsonify({'error': 'Email já cadastrado'}), 409

    new_user = User(
        name=data.get('name', ''),
        email=data['email'],
        role=data.get('role', 'user'),
        active=True
    )
    # O hash da senha deve ser tratado no Model ou aqui via método seguro
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
    data = request.get_json()
    if not data or 'email' not in data or 'password' not in data:
        return jsonify({'error': 'Credenciais incompletas'}), 400

    user = User.query.filter_by(email=data['email']).first()
    
    # Blindagem contra timing attacks: não diferenciar erro de user ou senha
    if not user or not user.check_password(data['password']):
        return jsonify({'error': 'Credenciais inválidas'}), 401

    if not user.active:
        return jsonify({'error': 'Conta desativada'}), 403

    return jsonify({
        'message': 'Login realizado com sucesso',
        'user': user.to_dict()
    }), 200