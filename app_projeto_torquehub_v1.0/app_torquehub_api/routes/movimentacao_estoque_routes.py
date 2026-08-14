from flask import Blueprint

from controllers.movimentacao_estoque_controller import (
    listar,
    buscar_por_id,
    criar,
    atualizar,
    excluir
)

movimentacao_estoque_routes = Blueprint(
    "movimentacao_estoque_routes",
    __name__,
    url_prefix="/api/movimentacoes-estoque"
)

@movimentacao_estoque_routes.route("/", methods=["GET"])
def get_movimentacoes():
    return listar()

@movimentacao_estoque_routes.route("/<int:id>", methods=["GET"])
def get_movimentacao(id):
    return buscar_por_id(id)

@movimentacao_estoque_routes.route("/", methods=["POST"])
def post_movimentacao():
    return criar()

@movimentacao_estoque_routes.route("/<int:id>", methods=["PUT"])
def put_movimentacao(id):
    return atualizar(id)

@movimentacao_estoque_routes.route("/<int:id>", methods=["DELETE"])
def delete_movimentacao(id):
    return excluir(id)