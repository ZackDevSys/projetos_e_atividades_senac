from config.database import get_connection


def listar_servicos():
    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                id,
                nome,
                descricao,
                valor_base,
                tempo_estimado,
                status
            FROM servicos
            ORDER BY id DESC
        """)

        return cursor.fetchall()

    finally:
        cursor.close()
        conexao.close()


def buscar_servico_por_id(id):
    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                id,
                nome,
                descricao,
                valor_base,
                tempo_estimado,
                status
            FROM servicos
            WHERE id = %s
        """, (id,))

        return cursor.fetchone()

    finally:
        cursor.close()
        conexao.close()


def criar_servico(
    nome,
    descricao,
    valor_base,
    tempo_estimado,
    status
):
    conexao = get_connection()
    cursor = conexao.cursor()

    try:
        sql = """
            INSERT INTO servicos (
                nome,
                descricao,
                valor_base,
                tempo_estimado,
                status
            )
            VALUES (%s, %s, %s, %s, %s)
        """

        valores = (
            nome,
            descricao,
            valor_base,
            tempo_estimado,
            status
        )

        cursor.execute(sql, valores)
        conexao.commit()

        return cursor.lastrowid

    finally:
        cursor.close()
        conexao.close()


def atualizar_servico(
    id,
    nome,
    descricao,
    valor_base,
    tempo_estimado,
    status
):
    conexao = get_connection()
    cursor = conexao.cursor()

    try:
        sql = """
            UPDATE servicos
            SET
                nome = %s,
                descricao = %s,
                valor_base = %s,
                tempo_estimado = %s,
                status = %s
            WHERE id = %s
        """

        valores = (
            nome,
            descricao,
            valor_base,
            tempo_estimado,
            status,
            id
        )

        cursor.execute(sql, valores)
        conexao.commit()

        return cursor.rowcount

    finally:
        cursor.close()
        conexao.close()


def excluir_servico(id):
    conexao = get_connection()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            DELETE FROM servicos
            WHERE id = %s
        """, (id,))

        conexao.commit()

        return cursor.rowcount

    finally:
        cursor.close()
        conexao.close()