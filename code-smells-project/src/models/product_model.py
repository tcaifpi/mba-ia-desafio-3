import sqlite3
import os

def get_db_connection():
    conn = sqlite3.connect(os.getenv('DATABASE_PATH', 'database.db'))
    conn.row_factory = sqlite3.Row
    return conn

def get_produto_por_id(id):
    conn = get_db_connection()
    # CORREÇÃO: Uso de ? para prevenir SQL Injection
    produto = conn.execute("SELECT * FROM produtos WHERE id = ?", (id,)).fetchone()
    conn.close()
    return produto

def get_todos_pedidos_otimizado():
    conn = get_db_connection()
    # CORREÇÃO: JOIN para evitar o problema N+1
    query = """
        SELECT p.*, i.item_nome 
        FROM pedidos p 
        LEFT JOIN itens_pedido i ON p.id = i.pedido_id
    """
    pedidos = conn.execute(query).fetchall()
    conn.close()
    return pedidos