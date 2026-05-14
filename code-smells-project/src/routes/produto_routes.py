from flask import Blueprint

produto_bp = Blueprint('produtos', __name__)

@produto_bp.route("/produtos", methods=["GET"])
def listar():
    # Importação local para evitar Circular Import
    from controllers.produto_controller import list_produtos
    return list_produtos()

@produto_bp.route("/produtos/<int:id>", methods=["GET"])
def buscar(id):
    from controllers.produto_controller import get_produto
    return get_produto(id)