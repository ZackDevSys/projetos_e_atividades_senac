from flask import Blueprint

from controllers.ordem_servico_usuario_controller import (
    listar,
    buscar_por_id,
    criar,
    atualizar,
    excluir
)

ordem_servico_usuario_routes = Blueprint(
    "ordem_servico_usuario_routes",
    __name__,
    url_prefix="/api/ordens-servico-usuarios"
)

@ordem_servico_usuario_routes.route("/", methods=["GET"])
def get_atribuicoes():

    return listar()

@ordem_servico_usuario_routes.route("/<int:id>", methods=["GET"])
def get_atribuicao(id):

    return buscar_por_id(id)

@ordem_servico_usuario_routes.route("/", methods=["POST"])
def post_atribuicao():

    return criar()

@ordem_servico_usuario_routes.route("/<int:id>", methods=["PUT"])
def put_atribuicao(id):

    return atualizar(id)

@ordem_servico_usuario_routes.route("/<int:id>", methods=["DELETE"])
def delete_atribuicao(id):

    return excluir(id)