import sqlite3
import os
from dotenv import load_dotenv

load_dotenv()

def init_database():
    # Pega o caminho do banco do .env ou usa o padrão
    db_path = os.getenv('DATABASE_PATH', 'database.db')
    
    print(f"Iniciando banco de dados em: {os.path.abspath(db_path)}")
    
    conn = sqlite3.connect(db_path)
    cursor = conn.cursor()

    # Criando a tabela de produtos
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS produtos (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            nome TEXT NOT NULL,
            preco REAL NOT NULL,
            estoque INTEGER NOT NULL
        )
    ''')

    # Inserindo dados iniciais para teste
    cursor.execute('DELETE FROM produtos') # Limpa para não duplicar
    cursor.execute('INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)', 
                   ('Notebook ThinkPad', 4500.00, 10))
    cursor.execute('INSERT INTO produtos (nome, preco, estoque) VALUES (?, ?, ?)', 
                   ('Mouse Sem Fio', 150.00, 50))

    conn.commit()
    conn.close()
    print("Tabela 'produtos' criada e populada com sucesso!")

if __name__ == "__main__":
    init_database()