from config.database import get_connection


def listar_atribuicoes():

    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    try:

        cursor.execute("""
            SELECT
                osu.id,
                osu.ordem_servico_id,
                osu.usuario_id,
                u.nome AS nome_usuario,
                osu.perfil,
                osu.data_atribuicao,
                osu.observacoes
            FROM ordem_servico_usuario osu
            INNER JOIN usuarios u
                ON u.id = osu.usuario_id
            ORDER BY osu.id DESC
        """)

        return cursor.fetchall()

    finally:

        cursor.close()
        conexao.close()


def buscar_atribuicao_por_id(id):

    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    try:

        cursor.execute("""
            SELECT
                osu.id,
                osu.ordem_servico_id,
                osu.usuario_id,
                u.nome AS nome_usuario,
                osu.perfil,
                osu.data_atribuicao,
                osu.observacoes
            FROM ordem_servico_usuario osu
            INNER JOIN usuarios u
                ON u.id = osu.usuario_id
            WHERE osu.id = %s
        """, (id,))

        return cursor.fetchone()

    finally:

        cursor.close()
        conexao.close()


def criar_atribuicao(
    ordem_servico_id,
    usuario_id,
    perfil,
    observacoes
):

    conexao = get_connection()
    cursor = conexao.cursor()

    try:

        sql = """
            INSERT INTO ordem_servico_usuario (
                ordem_servico_id,
                usuario_id,
                perfil,
                observacoes
            )
            VALUES (%s, %s, %s, %s)
        """

        valores = (
            ordem_servico_id,
            usuario_id,
            perfil,
            observacoes
        )

        cursor.execute(sql, valores)

        conexao.commit()

        return cursor.lastrowid

    finally:

        cursor.close()
        conexao.close()


def atualizar_atribuicao(
    id,
    usuario_id,
    perfil,
    observacoes
):

    conexao = get_connection()
    cursor = conexao.cursor()

    try:

        sql = """
            UPDATE ordem_servico_usuario
            SET
                usuario_id = %s,
                perfil = %s,
                observacoes = %s
            WHERE id = %s
        """

        valores = (
            usuario_id,
            perfil,
            observacoes,
            id
        )

        cursor.execute(sql, valores)

        conexao.commit()

        return cursor.rowcount

    finally:

        cursor.close()
        conexao.close()


def excluir_atribuicao(id):

    conexao = get_connection()
    cursor = conexao.cursor()

    try:

        cursor.execute("""
            DELETE FROM ordem_servico_usuario
            WHERE id = %s
        """, (id,))

        conexao.commit()

        return cursor.rowcount

    finally:

        cursor.close()
        conexao.close()