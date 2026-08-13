from flask import Blueprint

from controllers.ordem_servico_controller import (
    listar,
    buscar_por_id,
    criar,
    atualizar,
    excluir
)


ordem_servico_routes = Blueprint(
    "ordem_servico_routes",
    __name__,
    url_prefix="/api/ordens-servico"
)


@ordem_servico_routes.route("/", methods=["GET"])
def get_ordens():

    return listar()


@ordem_servico_routes.route("/<int:id>", methods=["GET"])
def get_ordem(id):

    return buscar_por_id(id)


@ordem_servico_routes.route("/", methods=["POST"])
def post_ordem():

    return criar()


@ordem_servico_routes.route("/<int:id>", methods=["PUT"])
def put_ordem(id):

    return atualizar(id)


@ordem_servico_routes.route("/<int:id>", methods=["DELETE"])
def delete_ordem(id):

    return excluir(id)