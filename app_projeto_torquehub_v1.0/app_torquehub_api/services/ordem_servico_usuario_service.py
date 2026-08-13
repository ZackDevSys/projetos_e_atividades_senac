from repositories.ordem_servico_usuario_repository import (
    listar_atribuicoes,
    buscar_atribuicao_por_id,
    criar_atribuicao,
    atualizar_atribuicao,
    excluir_atribuicao
)

from config.database import get_connection


def buscar_usuarios(usuario_id):

    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    try:

        cursor.execute("""
            SELECT
                id,
                nome,
                perfil,
                status
            FROM usuarios
            WHERE id = %s
        """, (usuario_id,))

        return cursor.fetchone()

    finally:

        cursor.close()
        conexao.close()

def verificar_ordem_servico(ordem_servico_id):

    conexao = get_connection()
    cursor = conexao.cursor()

    try:

        cursor.execute("""
            SELECT id
            FROM ordens_servico
            WHERE id = %s
        """, (ordem_servico_id,))

        return cursor.fetchone()

    finally:

        cursor.close()
        conexao.close()


def buscar_ordens_servico_usuario():

    return listar_atribuicoes()


def buscar_ordem_servico_usuario(id):

    return buscar_atribuicao_por_id(id)


def cadastrar_ordem_servico_usuario(dados):

    ordem_servico_id = dados.get("ordem_servico_id")
    usuario_id = dados.get("usuario_id")
    observacoes = dados.get("observacoes")

    if not ordem_servico_id:
        raise ValueError(
            "O ordem_servico_id é obrigatório."
        )

    if not usuario_id:
        raise ValueError(
            "O usuario_id é obrigatório."
        )

    if not verificar_ordem_servico(ordem_servico_id):
        raise ValueError(
            "Ordem de serviço não encontrada."
        )

    usuario = buscar_usuarios(usuario_id)

    if not usuario:
        raise ValueError(
            "Usuário não encontrado."
        )

    if usuario["status"] != "ATIVO":
        raise ValueError(
            "O usuário selecionado está inativo."
        )

    perfil = usuario["perfil"]

    return criar_atribuicao(
        ordem_servico_id,
        usuario_id,
        perfil,
        observacoes
    )


def atualizar_ordem_servico_usuario(id, dados):

    usuario_id = dados.get("usuario_id")
    observacoes = dados.get("observacoes")

    if not usuario_id:
        raise ValueError(
            "O usuario_id é obrigatório."
        )

    usuario = buscar_usuarios(usuario_id)

    if not usuario:
        raise ValueError(
            "Usuário não encontrado."
        )

    if usuario["status"] != "ATIVO":
        raise ValueError(
            "O usuário selecionado está inativo."
        )

    perfil = usuario["perfil"]

    return atualizar_atribuicao(
        id,
        usuario_id,
        perfil,
        observacoes
    )


def excluir_ordem_servico_usuario(id):

    return excluir_atribuicao(id)