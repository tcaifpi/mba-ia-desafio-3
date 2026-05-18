from database import db
from werkzeug.security import generate_password_hash, check_password_hash
from datetime import datetime

class User(db.Model):
    __tablename__ = 'users'

    # 1. Definição da Estrutura da Tabela
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    
    # Email como chave única, essencial para o processo de login seguro
    email = db.Column(db.String(120), unique=True, nullable=False)
    
    # Campo dimensionado para suportar hashes robustos (Bcrypt/Argon2 via Werkzeug)
    password_hash = db.Column(db.String(200), nullable=False)
    
    # Controle de Níveis de Acesso (RBAC) e Estado do Usuário
    role = db.Column(db.String(20), default='user') # ex: 'user', 'admin'
    active = db.Column(db.Boolean, default=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    # 2. Camada de Segurança de Credenciais (OWASP Guard)
    def set_password(self, password):
        """
        Gera o hash seguro com salt aleatório em tempo de execução.
        Impede o armazenamento de senhas em texto limpo.
        """
        self.password_hash = generate_password_hash(password)

    def check_password(self, password):
        """
        Verificação segura contra Timing Attacks ao comparar os hashes das senhas.
        """
        return check_password_hash(self.password_hash, password)

    # 3. Serialização Controlada (Prevenção de Information Disclosure)
    def to_dict(self):
        """
        Converte o modelo em dicionário para respostas JSON.
        Segurança Crítica: O campo 'password_hash' foi explicitamente omitido 
        para nunca vazar dados sensíveis na API.
        """
        return {
            'id': self.id,
            'name': self.name,
            'email': self.email,
            'role': self.role,
            'active': self.active
        }