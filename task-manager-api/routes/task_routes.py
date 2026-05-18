from flask import Blueprint, request, jsonify
from sqlalchemy.orm import joinedload
from database import db
from models.task import Task
from utils.auth import auth_required # Middleware de proteção JWT
from datetime import datetime

task_bp = Blueprint('tasks', __name__)

@task_bp.route('/tasks', methods=['POST'])
@auth_required
def create_task(current_user): 
    """
    Cria uma nova tarefa.
    Segurança: O user_id é injetado pelo token (current_user), 
    impedindo que um utilizador crie tarefas para outros.
    """
    data = request.get_json()
    if not data or 'title' not in data:
        return jsonify({'error': 'O título é obrigatório'}), 400

    new_task = Task(
        title=data['title'],
        description=data.get('description', ''),
        status=data.get('status', 'pending'),
        priority=data.get('priority', 3),
        user_id=current_user.id, # Vínculo forçado ao utilizador autenticado
        category_id=data.get('category_id'),
        due_date=datetime.fromisoformat(data['due_date']) if data.get('due_date') else None,
        tags=",".join(data.get('tags', [])) if isinstance(data.get('tags'), list) else None
    )

    try:
        db.session.add(new_task)
        db.session.commit()
        return jsonify(new_task.to_dict()), 201
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@task_bp.route('/tasks', methods=['GET'])
@auth_required
def get_tasks(current_user):
    """
    Lista tarefas apenas do utilizador autenticado.
    """
    tasks = Task.query.filter_by(user_id=current_user.id).all()
    return jsonify([t.to_dict() for t in tasks]), 200

@task_bp.route('/tasks/<int:task_id>', methods=['PUT'])
@auth_required
def update_task(current_user, task_id):
    """
    Atualiza uma tarefa com verificação de propriedade (Anti-IDOR).
    """
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Tarefa não encontrada'}), 404

    # VALIDAÇÃO DE PROPRIEDADE (BOLA/IDOR Defense)
    if task.user_id != current_user.id:
        return jsonify({'error': 'Acesso negado. Esta tarefa pertence a outro utilizador'}), 403

    data = request.get_json()
    if 'title' in data: task.title = data['title']
    if 'status' in data: task.status = data['status']
    if 'priority' in data: task.priority = data['priority']
    if 'description' in data: task.description = data['description']

    try:
        db.session.commit()
        return jsonify(task.to_dict()), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500

@task_bp.route('/tasks/<int:task_id>', methods=['DELETE'])
@auth_required
def delete_task(current_user, task_id):
    """
    Eliminação segura de tarefas.
    """
    task = Task.query.get(task_id)
    if not task:
        return jsonify({'error': 'Tarefa não encontrada'}), 404

    # VALIDAÇÃO DE PROPRIEDADE
    if task.user_id != current_user.id:
        return jsonify({'error': 'Acesso negado. Não pode eliminar dados de terceiros'}), 403

    try:
        db.session.delete(task)
        db.session.commit()
        return jsonify({'message': 'Tarefa eliminada com sucesso'}), 200
    except Exception as e:
        db.session.rollback()
        return jsonify({'error': str(e)}), 500