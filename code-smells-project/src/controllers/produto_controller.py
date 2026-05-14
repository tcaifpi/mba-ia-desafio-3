from flask import jsonify, request
from models.produto_model import ProdutoModel

def list_produtos():
    # Captura o ID da query string (?id=...) de forma segura
    id_param = request.args.get('id')
    
    if id_param:
        # Tenta buscar o produto específico
        produto = ProdutoModel.buscar_por_id(id_param)
        if produto:
            return jsonify({"dados": dict(produto), "sucesso": True}), 200
        # Se não achar (ou se for tentativa de injeção), retorna 404 e não erro 500
        return jsonify({"erro": "Produto não encontrado", "sucesso": False}), 404

    # Se não houver ID, lista todos normalmente
    produtos = ProdutoModel.listar_todos()
    return jsonify({"dados": [dict(p) for p in produtos], "sucesso": True}), 200