from database import db
from datetime import datetime

class Category(db.Model):
    __tablename__ = 'categories'

    # Identificador único da categoria
    id = db.Column(db.Integer, primary_key=True)
    
    # Nome da categoria (ex: Trabalho, Pessoal, IFPI)
    name = db.Column(db.String(100), nullable=False)
    
    # Descrição opcional para detalhar o propósito da categoria
    description = db.Column(db.String(300), nullable=True)
    
    # Campo para código hexadecimal de cores (útil para o frontend)
    color = db.Column(db.String(7), default='#000000')
    
    # Timestamp de criação para auditoria
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    def to_dict(self):
        """
        Converte o objeto SQLAlchemy num dicionário Python.
        Essencial para a serialização JSON nas rotas da API.
        """
        return {
            'id': self.id,
            'name': self.name,
            'description': self.description,
            'color': self.color,
            'created_at': str(self.created_at),
        }