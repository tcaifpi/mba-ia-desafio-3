from models.product_model import get_produto_por_id

def detalhar_produto(id):
    if not id.isdigit():
        return {"error": "ID inválido"}, 400
    
    produto = get_produto_por_id(id)
    if not produto:
        return {"error": "Produto não encontrado"}, 404
        
    return dict(produto), 200