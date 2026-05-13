from werkzeug.security import generate_password_hash, check_password_hash
from database import get_db_connection

class User:
    def __init__(self, id, name, email, password_hash):
        self.id = id
        self.name = name
        self.email = email
        self.password_hash = password_hash

    @staticmethod
    def create(name, email, password):
        """Cria um usuário com a senha já criptografada (Hash Seguro)."""
        # Substitui o MD5 por um hash PBKDF2 ou BCrypt (padrão do werkzeug)
        hashed_password = generate_password_hash(password)
        
        conn = get_db_connection()
        cursor = conn.cursor()
        try:
            cursor.execute(
                'INSERT INTO users (name, email, password) VALUES (?, ?, ?)',
                (name, email, hashed_password)
            )
            conn.commit()
            return cursor.lastrowid
        finally:
            conn.close()

    @staticmethod
    def verify_login(email, password):
        """Verifica se a senha fornecida bate com o hash no banco."""
        conn = get_db_connection()
        cursor = conn.cursor()
        user_data = cursor.execute(
            'SELECT * FROM users WHERE email = ?', (email,)
        ).fetchone()
        conn.close()

        if user_data and check_password_hash(user_data['password'], password):
            return User(
                user_data['id'], 
                user_data['name'], 
                user_data['email'], 
                user_data['password']
            )
        return None

    def to_dict(self):
        """Retorna o usuário como dicionário, ocultando o hash da senha (Segurança)."""
        return {
            "id": self.id,
            "name": self.name,
            "email": self.email
            # Jamais retorne o password_hash aqui
        }