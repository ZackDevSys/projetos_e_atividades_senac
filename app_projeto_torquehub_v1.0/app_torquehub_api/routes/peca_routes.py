from flask import Blueprint

from controllers.peca_controller import (
    listar,
    buscar_por_id,
    criar,
    atualizar,
    excluir
)

peca_routes = Blueprint(
    "peca_routes",
    __name__,
    url_prefix="/api/pecas"
)

@peca_routes.route("/", methods=["GET"])
def get_pecas():

    return listar()

@peca_routes.route("/<int:id>", methods=["GET"])
def get_peca(id):

    return buscar_por_id(id)

@peca_routes.route("/", methods=["POST"])
def post_peca():

    return criar()

@peca_routes.route("/<int:id>", methods=["PUT"])
def put_peca(id):

    return atualizar(id)

@peca_routes.route("/<int:id>", methods=["DELETE"])
def delete_peca(id):

    return excluir(id)