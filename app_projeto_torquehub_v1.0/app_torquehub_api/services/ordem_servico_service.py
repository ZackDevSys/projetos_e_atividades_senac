from repositories.ordem_servico_repository import (
    listar_ordens_servico,
    buscar_ordem_servico_por_id,
    criar_ordem_servico,
    atualizar_ordem_servico as atualizar_repository,
    excluir_ordem_servico as excluir_repository
)

from config.database import get_connection


STATUS_VALIDOS = [
    "ABERTA",
    "EM_ANALISE",
    "AGUARDANDO_APROVACAO",
    "EM_MANUTENCAO",
    "AGUARDANDO_PECA",
    "FINALIZADA",
    "ENTREGUE",
    "CANCELADA"
]


def validar_status(status):

    if status is None:
        return "ABERTA"

    if status not in STATUS_VALIDOS:

        raise ValueError(
            "Status inválido. Utilize um dos seguintes: "
            + ", ".join(STATUS_VALIDOS)
        )

    return status


def validar_usuarios(usuarios):

    if not usuarios:

        raise ValueError(
            "É necessário informar pelo menos um usuário."
        )

    for usuario in usuarios:

        if not isinstance(usuario, dict):

            raise ValueError(
                "Cada usuário deve ser informado como objeto."
            )

        usuario_id = usuario.get("usuario_id")
        perfil = usuario.get("perfil")

        if not usuario_id:

            raise ValueError(
                "O usuario_id é obrigatório."
            )

        if not perfil:

            raise ValueError(
                "O perfil é obrigatório."
            )

        verificar_usuario(usuario_id, perfil)


def verificar_usuario(usuario_id, perfil):

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

        usuario = cursor.fetchone()

        if usuario is None:

            raise ValueError(
                f"Usuário com id {usuario_id} não encontrado."
            )

        if usuario["status"] != "ATIVO":

            raise ValueError(
                f"O usuário {usuario['nome']} está inativo."
            )

        if usuario["perfil"] != perfil:

            raise ValueError(
                f"O usuário {usuario['nome']} possui o perfil "
                f"{usuario['perfil']} e não {perfil}."
            )

    finally:

        cursor.close()
        conexao.close()


def buscar_ordens():

    return listar_ordens_servico()


def buscar_ordem(id):

    return buscar_ordem_servico_por_id(id)


def cadastrar_ordem(dados):

    veiculo_id = dados.get("veiculo_id")

    if not veiculo_id:

        raise ValueError(
            "O veiculo_id é obrigatório."
        )

    usuarios = dados.get("usuarios")

    validar_usuarios(usuarios)

    problema_relatado = dados.get("problema_relatado")

    if not problema_relatado:

        raise ValueError(
            "O problema_relatado é obrigatório."
        )

    status = validar_status(
        dados.get("status")
    )

    return criar_ordem_servico(
        dados.get("numero"),
        veiculo_id,
        dados.get("data_entrada"),
        dados.get("previsao_entrega"),
        dados.get("data_conclusao"),
        dados.get("data_entrega"),
        dados.get("km_entrada"),
        problema_relatado,
        dados.get("diagnostico"),
        dados.get("observacoes"),
        status,
        dados.get("valor_total", 0),
        usuarios
    )


def atualizar_ordem(id, dados):

    veiculo_id = dados.get("veiculo_id")

    if not veiculo_id:

        raise ValueError(
            "O veiculo_id é obrigatório."
        )

    usuarios = dados.get("usuarios")

    validar_usuarios(usuarios)

    status = validar_status(
        dados.get("status")
    )

    return atualizar_repository(
        id,
        veiculo_id,
        dados.get("previsao_entrega"),
        dados.get("data_conclusao"),
        dados.get("data_entrega"),
        dados.get("km_entrada"),
        dados.get("problema_relatado"),
        dados.get("diagnostico"),
        dados.get("observacoes"),
        status,
        dados.get("valor_total", 0),
        usuarios
    )


def excluir_ordem(id):

    return excluir_repository(id)