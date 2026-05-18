import sqlite3

class ProdutoModel:
    """
    Camada Model: Responsável direta pela interação com a base de dados loja.db.
    Implementa padrões de segurança para evitar SQL Injection.
    """

    @staticmethod
    def buscar_por_id(id):
        # Ligação à base de dados local
        conn = sqlite3.connect('loja.db')
        
        # Define row_factory para permitir o acesso aos campos pelo nome da coluna
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        # EVIDÊNCIA DE SEGURANÇA:
        # A utilização do placeholder '?' garante que o motor do SQLite trate o input 
        # exclusivamente como um valor literal, neutralizando ataques de injeção.
        query = "SELECT * FROM produtos WHERE id = ?"
        
        try:
            # O ID é passado como uma tupla no segundo argumento do execute
            cursor.execute(query, (id,))
            produto = cursor.fetchone()
        except Exception as e:
            # Em produção, este erro deve ser registado num ficheiro de log
            print(f"Erro na consulta SQL: {e}")
            produto = None
        finally:
            # Garante o fecho da ligação independentemente do sucesso da query
            conn.close()
            
        return produto

    @staticmethod
    def listar_todos():
        """
        Retorna a lista completa de produtos para ser processada pelo Controller.
        """
        conn = sqlite3.connect('loja.db')
        conn.row_factory = sqlite3.Row
        cursor = conn.cursor()
        
        query = "SELECT * FROM produtos"
        
        try:
            cursor.execute(query)
            produtos = cursor.fetchall()
        except Exception:
            produtos = []
        finally:
            conn.close()
            
        return produtos