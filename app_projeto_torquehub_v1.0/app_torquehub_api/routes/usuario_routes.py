from flask import Blueprint

from controllers.usuario_controller import (
    listar,
    buscar_por_id,
    criar,
    atualizar,
    excluir
)

usuario_routes = Blueprint(
    "usuario_routes",
    __name__,
    url_prefix="/api/usuarios"
)

@usuario_routes.route("/", methods=["GET"])
def get_usuarios():
    return listar()

@usuario_routes.route("/<int:id>", methods=["GET"])
def get_usuario(id):
    return buscar_por_id(id)

@usuario_routes.route("/", methods=["POST"])
def post_usuario():
    return criar()

@usuario_routes.route("/<int:id>", methods=["PUT"])
def put_usuario(id):
    return atualizar(id)

@usuario_routes.route("/<int:id>", methods=["DELETE"])
def delete_usuario(id):
    return excluir(id)