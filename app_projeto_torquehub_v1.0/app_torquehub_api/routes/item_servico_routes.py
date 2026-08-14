from flask import Blueprint

from controllers.item_servico_controller import (
    listar,
    buscar_por_id,
    criar,
    atualizar,
    excluir
)

item_servico_routes = Blueprint(
    "item_servico_routes",
    __name__,
    url_prefix="/api/ordens-servico"
)

@item_servico_routes.route(
    "/<int:ordem_servico_id>/itens",
    methods=["GET"]
)
def get_itens(ordem_servico_id):
    return listar(ordem_servico_id)

@item_servico_routes.route(
    "/<int:ordem_servico_id>/itens",
    methods=["POST"]
)
def post_item(ordem_servico_id):
    return criar(ordem_servico_id)

@item_servico_routes.route(
    "/itens/<int:id>",
    methods=["GET"]
)
def get_item(id):
    return buscar_por_id(id)

@item_servico_routes.route(
    "/itens/<int:id>",
    methods=["PUT"]
)
def put_item(id):
    return atualizar(id)

@item_servico_routes.route(
    "/itens/<int:id>",
    methods=["DELETE"]
)
def delete_item(id):
    return excluir(id)