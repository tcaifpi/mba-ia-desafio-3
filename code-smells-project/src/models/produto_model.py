import sqlite3

class ProdutoModel:
    @staticmethod
    def buscar_por_id(id):
        conn = sqlite3.connect('loja.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # PROTEÇÃO: O '?' garante que o input seja tratado como texto puro
        # Isso neutraliza o ' OR '1'='1
        query = "SELECT * FROM produtos WHERE id = ?"
        
        try:
            cursor.execute(query, (id,))
            produto = cursor.fetchone()
        except Exception:
            produto = None
        finally:
            conn.close()
            
        return produto