from database import db
from datetime import datetime

class Task(db.Model):
    __tablename__ = 'tasks'

    # 1. Identificadores e Campos Principais
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(50), default='pending') # Estados: pending, in_progress, done, cancelled
    priority = db.Column(db.Integer, default=3)          # Escala de 1 (Alta) a 5 (Baixa)
    
    # 2. Chaves Estrangeiras (Mapeamento de Relacionamentos)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'), nullable=True)
    category_id = db.Column(db.Integer, db.ForeignKey('categories.id'), nullable=True)
    
    # 3. Metadados e Prazos
    created_at = db.Column(db.DateTime, default=datetime.utcnow)
    updated_at = db.Column(db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)
    due_date = db.Column(db.DateTime, nullable=True)
    tags = db.Column(db.String(500), nullable=True) # Armazenadas como string separada por vírgulas

    # 4. Relacionamentos Virtuais do SQLAlchemy
    user = db.relationship('User', backref='tasks')
    category = db.relationship('Category', backref='tasks')

    def to_dict(self):
        """
        Converte a instância do banco num dicionário Python.
        Essencial para a serialização e retorno via JSON nas rotas HTTP.
        """
        return {
            'id': self.id,
            'title': self.title,
            'description': self.description,
            'status': self.status,
            'priority': self.priority,
            'user_id': self.user_id,
            'category_id': self.category_id,
            'created_at': str(self.created_at),
            'updated_at': str(self.updated_at),
            'due_date': str(self.due_date) if self.due_date else None,
            'tags': self.tags.split(',') if self.tags else []
        }

    def validate_status(self, new_status):
        """
        Garante a integridade do ciclo de vida da tarefa.
        """
        valid_statuses = ['pending', 'in_progress', 'done', 'cancelled']
        return new_status in valid_statuses

    def validate_priority(self, p):
        """
        Valida se a prioridade está dentro do escopo permitido (1 a 5).
        """
        return 1 <= p <= 5

    def is_overdue(self):
        """
        Regra de negócio dinâmica: Avalia se a tarefa está em atraso
        comparando o prazo com o horário UTC atual.
        """
        if self.due_date and self.due_date < datetime.utcnow():
            return self.status not in ['done', 'cancelled']
        return False