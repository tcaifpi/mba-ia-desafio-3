from flask import Blueprint, jsonify
from controllers.product_controller import detalhar_produto

# Definimos o Blueprint para agrupar as rotas de produtos
product_bp = Blueprint('products', __name__)

@product_bp.route('/produtos/<id>', methods=['GET'])
def get_produto(id):
    # Chamamos o controller e desempacotamos o retorno (data, status_code)
    data, status_code = detalhar_produto(id)
    return jsonify(data), status_code

# Você pode adicionar mais rotas aqui seguindo o mesmo padrão
# @product_bp.route('/produtos', methods=['POST'])
# ...