from config.perfis import PERFIS_MOVIMENTACAO_ESTOQUE
from repositories.movimentacao_estoque_repository import (
    listar_movimentacoes,
    buscar_movimentacao_por_id,
    criar_movimentacao,
    atualizar_movimentacao,
    excluir_movimentacao,
    buscar_usuario_para_movimentacao
)

TIPOS_VALIDOS = [
    "ENTRADA",
    "SAIDA"
]

def validar_tipo(tipo):

    if not tipo:
        raise ValueError("O tipo da movimentação é obrigatório.")

    tipo = tipo.upper()

    if tipo not in TIPOS_VALIDOS:
        raise ValueError(
            "Tipo inválido. Utilize ENTRADA ou SAIDA."
        )

    return tipo

def validar_quantidade(quantidade):

    if quantidade is None:
        raise ValueError(
            "A quantidade é obrigatória."
        )

    try:
        quantidade = int(quantidade)
    except (ValueError, TypeError):
        raise ValueError(
            "A quantidade deve ser um número inteiro."
        )

    if quantidade <= 0:
        raise ValueError(
            "A quantidade deve ser maior que zero."
        )

    return quantidade

def validar_usuario_movimentacao(usuario_id):

    usuario = buscar_usuario_para_movimentacao(usuario_id)

    if usuario is None:
        raise ValueError(
            "Usuário não encontrado."
        )

    if usuario["status"] != "ATIVO":
        raise ValueError(
            "O usuário está inativo e não pode realizar movimentações de estoque."
        )

    if usuario["perfil"] not in PERFIS_MOVIMENTACAO_ESTOQUE:
        raise ValueError(
            "O perfil do usuário não possui permissão para movimentar o estoque."
        )

    return usuario

def buscar_movimentacoes():
    return listar_movimentacoes()

def buscar_movimentacao(id):
    return buscar_movimentacao_por_id(id)

def cadastrar_movimentacao(dados):

    peca_id = dados.get("peca_id")
    usuario_id = dados.get("usuario_id")
    tipo = dados.get("tipo")
    quantidade = dados.get("quantidade")
    observacao = dados.get("observacao")

    if not peca_id:
        raise ValueError(
            "O peca_id é obrigatório."
        )

    if not usuario_id:
        raise ValueError(
            "O usuario_id é obrigatório."
        )
    
    validar_usuario_movimentacao(usuario_id)

    tipo = validar_tipo(tipo)

    quantidade = validar_quantidade(quantidade)

    return criar_movimentacao(
        peca_id,
        usuario_id,
        tipo,
        quantidade,
        observacao
    )

def atualizar_movimentacao_service(id, dados):

    peca_id = dados.get("peca_id")
    usuario_id = dados.get("usuario_id")
    tipo = dados.get("tipo")
    quantidade = dados.get("quantidade")
    observacao = dados.get("observacao")

    if not peca_id:
        raise ValueError(
            "O peca_id é obrigatório."
        )

    if not usuario_id:
        raise ValueError(
           "O usuario_id é obrigatório."
        )

    validar_usuario_movimentacao(usuario_id)

    tipo = validar_tipo(tipo)
    
    quantidade = validar_quantidade(quantidade)

    return atualizar_movimentacao(
        id,
        peca_id,
        usuario_id,
        tipo,
        quantidade,
        observacao
    )

def excluir_movimentacao_service(id):
    return excluir_movimentacao(id)