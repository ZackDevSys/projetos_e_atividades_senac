from repositories.cliente_repository import (
    listar_clientes,
    buscar_cliente_por_id,
    criar_cliente,
    atualizar_cliente as atualizar_cliente_repository,
    excluir_cliente as excluir_cliente_repository
)

from config.perfis import status_valido


def buscar_clientes():

    return listar_clientes()


def buscar_cliente(id):

    return buscar_cliente_por_id(id)


def cadastrar_cliente(dados):

    nome = dados.get("nome")
    cpf = dados.get("cpf")
    telefone = dados.get("telefone")
    email = dados.get("email")
    endereco = dados.get("endereco")
    observacoes = dados.get("observacoes")

    # Cliente novo começa como ATIVO
    status = dados.get("status", "ATIVO")

    if not nome:
        raise ValueError("O nome é obrigatório.")

    if not cpf:
        raise ValueError("O CPF é obrigatório.")

    if not telefone:
        raise ValueError("O telefone é obrigatório.")

    if not email:
        raise ValueError("O email é obrigatório.")

    if not status_valido(status):
        raise ValueError(
            "Status inválido. Utilize ATIVO ou INATIVO."
        )

    return criar_cliente(
        nome,
        cpf,
        telefone,
        email,
        endereco,
        observacoes,
        status
    )


def atualizar_cliente(id, dados):

    nome = dados.get("nome")
    cpf = dados.get("cpf")
    telefone = dados.get("telefone")
    email = dados.get("email")
    endereco = dados.get("endereco")
    observacoes = dados.get("observacoes")

    if not nome:
        raise ValueError("O nome é obrigatório.")

    if not cpf:
        raise ValueError("O CPF é obrigatório.")

    if not telefone:
        raise ValueError("O telefone é obrigatório.")

    if not email:
        raise ValueError("O email é obrigatório.")

    #/*
    # * Se o frontend não enviar status,
    # * preservamos o status atual do cliente.
    #*/

    status = dados.get("status")

    if status is None:

        cliente_atual = buscar_cliente_por_id(id)

        if cliente_atual is None:
            return 0

        status = cliente_atual.get("status", "ATIVO")

    if not status_valido(status):
        raise ValueError(
            "Status inválido. Utilize ATIVO ou INATIVO."
        )

    return atualizar_cliente_repository(
        id,
        nome,
        cpf,
        telefone,
        email,
        endereco,
        observacoes,
        status
    )


def excluir_cliente(id):

    return excluir_cliente_repository(id)