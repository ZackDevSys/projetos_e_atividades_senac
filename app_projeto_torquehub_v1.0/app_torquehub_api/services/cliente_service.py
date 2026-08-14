from repositories.cliente_repository import (
    listar_clientes,
    buscar_cliente_por_id,
    criar_cliente,
    atualizar_cliente as atualizar_cliente_repository,
    excluir_cliente as excluir_cliente_repository
)

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

    if not nome:
        raise ValueError("O nome é obrigatório.")

    if not cpf:
        raise ValueError("O CPF é obrigatório.")

    if not telefone:
        raise ValueError("O telefone é obrigatório.")

    if not email:
        raise ValueError("O email é obrigatório.")

    return criar_cliente(
        nome,
        cpf,
        telefone,
        email,
        endereco
    )

def atualizar_cliente(id, dados):
    nome = dados.get("nome")
    cpf = dados.get("cpf")
    telefone = dados.get("telefone")
    email = dados.get("email")
    endereco = dados.get("endereco")

    if not nome:
        raise ValueError("O nome é obrigatório.")

    if not cpf:
        raise ValueError("O CPF é obrigatório.")

    if not telefone:
        raise ValueError("O telefone é obrigatório.")

    if not email:
        raise ValueError("O email é obrigatório.")

    return atualizar_cliente_repository(
        id,
        nome,
        cpf,
        telefone,
        email,
        endereco
    )

def excluir_cliente(id):
    return excluir_cliente_repository(id)