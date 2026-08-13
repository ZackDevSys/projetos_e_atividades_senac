from flask import Blueprint

from controllers.servico_controller import (
    listar,
    buscar_por_id,
    criar,
    atualizar,
    excluir
)


servico_routes = Blueprint(
    "servico_routes",
    __name__,
    url_prefix="/api/servicos"
)


@servico_routes.route("/", methods=["GET"])
def get_servicos():
    return listar()


@servico_routes.route("/<int:id>", methods=["GET"])
def get_servico(id):
    return buscar_por_id(id)


@servico_routes.route("/", methods=["POST"])
def post_servico():
    return criar()


@servico_routes.route("/<int:id>", methods=["PUT"])
def put_servico(id):
    return atualizar(id)


@servico_routes.route("/<int:id>", methods=["DELETE"])
def delete_servico(id):
    return excluir(id)