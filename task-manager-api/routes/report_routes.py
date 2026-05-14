from flask import Blueprint, request, jsonify
from sqlalchemy import func
from database import db
from models.task import Task
from models.user import User
from models.category import Category
from datetime import datetime

report_bp = Blueprint('reports', __name__)

@report_bp.route('/reports/summary', methods=['GET'])
def summary_report():
    """
    Gera um relatório consolidado.
    Otimizado: Substitui múltiplas queries por funções de agregação do SQL.
    """
    try:
        # 1. Estatísticas de Status (Uma única query GROUP BY)
        status_counts = db.session.query(
            Task.status, func.count(Task.id)
        ).group_by(Task.status).all()
        status_map = {status: count for status, count in status_counts}

        # 2. Estatísticas de Prioridade (Uma única query GROUP BY)
        priority_counts = db.session.query(
            Task.priority, func.count(Task.id)
        ).group_by(Task.priority).all()
        priority_map = {f'p{priority}': count for priority, count in priority_counts}

        # 3. Contagem de Atrasos (Executada no Banco, não em Python)
        overdue_count = Task.query.filter(
            Task.due_date < datetime.utcnow(),
            Task.status.notin_(['done', 'cancelled'])
        ).count()

        # 4. Totais Gerais
        total_tasks = sum(status_map.values())
        
        report = {
            'overview': {
                'total_tasks': total_tasks,
                'total_users': User.query.count(),
                'total_categories': Category.query.count(),
                'overdue_count': overdue_count
            },
            'by_status': {
                'pending': status_map.get('pending', 0),
                'in_progress': status_map.get('in_progress', 0),
                'done': status_map.get('done', 0),
                'cancelled': status_map.get('cancelled', 0)
            },
            'by_priority': priority_map
        }

        return jsonify(report), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@report_bp.route('/categories', methods=['GET'])
def get_categories():
    categories = Category.query.all()
    return jsonify([c.to_dict() for c in categories]), 200

@report_bp.route('/categories', methods=['POST'])
def create_category():
    data = request.get_json()
    if not data or 'name' not in data:
        return jsonify({'error': 'Nome é obrigatório'}), 400

    new_cat = Category(
        name=data['name'],
        description=data.get('description', ''),
        color=data.get('color', '#000000')
    )

    try:
        db.session.add(new_cat)
        db.session.commit()
        return jsonify(new_cat.to_dict()), 201
    except Exception:
        db.session.rollback()
        return jsonify({'error': 'Erro ao criar categoria'}), 500