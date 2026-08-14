from flask import Blueprint

from controllers.item_peca_controller import (
    listar,
    buscar_por_id,
    criar,
    atualizar,
    excluir
)

item_peca_routes = Blueprint(
    "item_peca_routes",
    __name__,
    url_prefix="/api/itens-pecas"
)

@item_peca_routes.route("/", methods=["GET"])
def get_itens_pecas():

    return listar()

@item_peca_routes.route("/<int:id>", methods=["GET"])
def get_item_peca(id):

    return buscar_por_id(id)

@item_peca_routes.route("/", methods=["POST"])
def post_item_peca():

    return criar()

@item_peca_routes.route("/<int:id>", methods=["PUT"])
def put_item_peca(id):

    return atualizar(id)

@item_peca_routes.route("/<int:id>", methods=["DELETE"])
def delete_item_peca(id):

    return excluir(id)