from repositories.usuario_repository import (
    listar_usuarios,
    buscar_usuario_por_id,
    criar_usuario,
    atualizar_usuario as atualizar_usuario_repository,
    excluir_usuario as excluir_usuario_repository
)


def buscar_usuarios():
    return listar_usuarios()


def buscar_usuario(id):
    return buscar_usuario_por_id(id)


def cadastrar_usuario(dados):
    nome = dados.get("nome")
    email = dados.get("email")
    telefone = dados.get("telefone")
    perfil = dados.get("perfil")
    especialidade = dados.get("especialidade")
    status = dados.get("status")

    if not nome:
        raise ValueError("O nome é obrigatório.")

    if not email:
        raise ValueError("O email é obrigatório.")

    if not perfil:
        raise ValueError("O perfil é obrigatório.")

    if not status:
        raise ValueError("O status é obrigatório.")

    return criar_usuario(
        nome,
        email,
        telefone,
        perfil,
        especialidade,
        status
    )


def atualizar_usuario(id, dados):
    nome = dados.get("nome")
    email = dados.get("email")
    telefone = dados.get("telefone")
    perfil = dados.get("perfil")
    especialidade = dados.get("especialidade")
    status = dados.get("status")

    if not nome:
        raise ValueError("O nome é obrigatório.")

    if not email:
        raise ValueError("O email é obrigatório.")

    if not perfil:
        raise ValueError("O perfil é obrigatório.")

    if not status:
        raise ValueError("O status é obrigatório.")

    return atualizar_usuario_repository(
        id,
        nome,
        email,
        telefone,
        perfil,
        especialidade,
        status
    )

def excluir_usuario(id):
    return excluir_usuario_repository(id)