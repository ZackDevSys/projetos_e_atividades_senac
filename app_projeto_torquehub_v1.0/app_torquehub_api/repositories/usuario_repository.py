from config.database import get_connection

def listar_usuarios():
    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                id,
                nome,
                email,
                telefone,
                perfil,
                especialidade,
                status,
                data_cadastro
            FROM usuarios
            ORDER BY nome
        """)

        return cursor.fetchall()

    finally:
        cursor.close()
        conexao.close()

def buscar_usuario_por_id(id):
    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                id,
                nome,
                email,
                telefone,
                perfil,
                especialidade,
                status,
                data_cadastro
            FROM usuarios
            WHERE id = %s
        """, (id,))

        return cursor.fetchone()

    finally:
        cursor.close()
        conexao.close()

def criar_usuario(
    nome,
    email,
    telefone,
    perfil,
    especialidade,
    status
):
    conexao = get_connection()
    cursor = conexao.cursor()

    try:
        sql = """
            INSERT INTO usuarios (
                nome,
                email,
                telefone,
                perfil,
                especialidade,
                status
            )
            VALUES (%s, %s, %s, %s, %s, %s)
        """

        valores = (
            nome,
            email,
            telefone,
            perfil,
            especialidade,
            status
        )

        cursor.execute(sql, valores)
        conexao.commit()

        return cursor.lastrowid

    finally:
        cursor.close()
        conexao.close()

def atualizar_usuario(
    id,
    nome,
    email,
    telefone,
    perfil,
    especialidade,
    status
):
    conexao = get_connection()
    cursor = conexao.cursor()

    try:
        sql = """
            UPDATE usuarios
            SET
                nome = %s,
                email = %s,
                telefone = %s,
                perfil = %s,
                especialidade = %s,
                status = %s
            WHERE id = %s
        """

        valores = (
            nome,
            email,
            telefone,
            perfil,
            especialidade,
            status,
            id
        )

        cursor.execute(sql, valores)
        conexao.commit()

        return cursor.rowcount

    finally:
        cursor.close()
        conexao.close()

def excluir_usuario(id):
    conexao = get_connection()
    cursor = conexao.cursor()

    try:
        sql = """
            DELETE FROM usuarios
            WHERE id = %s
        """

        cursor.execute(sql, (id,))
        conexao.commit()

        return cursor.rowcount

    finally:
        cursor.close()
        conexao.close()