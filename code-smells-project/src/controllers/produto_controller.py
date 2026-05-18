from flask import jsonify, request
from models.produto_model import ProdutoModel

def list_produtos():
    """
    Camada Controller: Orquestra a lógica de negócio.
    Recebe o pedido da rota, decide qual método do Model chamar e 
    define o status HTTP de retorno.
    """
    
    # SEGURANÇA: Captura o ID da query string (?id=...) de forma isolada.
    # O Controller não monta a query, apenas repassa o parâmetro para o Model.
    id_param = request.args.get('id')
    
    if id_param:
        # Tenta buscar o produto específico através do Model saneado
        produto = ProdutoModel.buscar_por_id(id_param)
        
        if produto:
            # Sucesso: Retorna 200 OK com os dados formatados
            return jsonify({
                "dados": dict(produto), 
                "sucesso": True
            }), 200
        
        # TRATAMENTO DE ERRO: Se o produto não existir ou se for uma tentativa 
        # de SQL Injection (que resultará em zero resultados), retorna 404.
        # Isso evita vazar informações sobre a estrutura do banco (Erro 500).
        return jsonify({
            "erro": "Produto não encontrado", 
            "sucesso": False
        }), 404

    # FLUXO PADRÃO: Se não houver ID, lista todos os produtos normalmente
    produtos = ProdutoModel.listar_todos()
    return jsonify({
        "dados": [dict(p) for p in produtos], 
        "sucesso": True
    }), 200