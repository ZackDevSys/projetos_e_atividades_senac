from flask import Blueprint

from controllers.cliente_controller import (
    listar,
    buscar_por_id,
    criar,
    atualizar,
    excluir
)

cliente_routes = Blueprint(
    "cliente_routes",
    __name__,
    url_prefix="/api/clientes"
)

@cliente_routes.route("/", methods=["GET"])
def get_clientes():
    return listar()

@cliente_routes.route("/<int:id>", methods=["GET"])
def get_cliente(id):
    return buscar_por_id(id)

@cliente_routes.route("/", methods=["POST"])
def post_cliente():
    return criar()

@cliente_routes.route("/<int:id>", methods=["PUT"])
def put_cliente(id):
    return atualizar(id)

@cliente_routes.route("/<int:id>", methods=["DELETE"])
def delete_cliente(id):
    return excluir(id)