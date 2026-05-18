from flask import Blueprint
from controllers.produto_controller import list_produtos

# Definição do Blueprint para modularização (conforme audit-project-3.md)
produto_bp = Blueprint('produto_bp', __name__)

# REGRA DE OURO (guidelines-mvc.md):
# Nenhuma lógica de negócio ou de dados reside aqui.
# Apenas o mapeamento do Verbo HTTP + URL para o Controller.

@produto_bp.route('/produtos', methods=['GET'])
def get_produtos():
    """
    Endpoint para listagem de produtos.
    Suporta busca por ID via query string: /produtos?id=1
    """
    return list_produtos()