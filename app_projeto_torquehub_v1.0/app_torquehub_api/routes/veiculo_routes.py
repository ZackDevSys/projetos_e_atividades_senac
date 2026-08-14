from flask import Blueprint

from controllers.veiculo_controller import (
    listar,
    buscar_por_id,
    criar,
    atualizar,
    excluir
)

veiculo_routes = Blueprint(
    "veiculo_routes",
    __name__,
    url_prefix="/api/veiculos"
)

@veiculo_routes.route("/", methods=["GET"])
def get_veiculos():
    return listar()

@veiculo_routes.route("/<int:id>", methods=["GET"])
def get_veiculo(id):
    return buscar_por_id(id)

@veiculo_routes.route("/", methods=["POST"])
def post_veiculo():
    return criar()

@veiculo_routes.route("/<int:id>", methods=["PUT"])
def put_veiculo(id):
    return atualizar(id)

@veiculo_routes.route("/<int:id>", methods=["DELETE"])
def delete_veiculo(id):
    return excluir(id)