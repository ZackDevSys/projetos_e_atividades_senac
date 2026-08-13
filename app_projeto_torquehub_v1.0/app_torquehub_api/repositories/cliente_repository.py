from config.database import get_connection


def listar_clientes():
    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                id,
                nome,
                cpf,
                telefone,
                email,
                endereco,
                data_cadastro
            FROM clientes
            ORDER BY nome
        """)

        return cursor.fetchall()

    finally:
        cursor.close()
        conexao.close()

def buscar_cliente_por_id(id):
    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                id,
                nome,
                cpf,
                telefone,
                email,
                endereco,
                data_cadastro
            FROM clientes
            WHERE id = %s
        """, (id,))

        return cursor.fetchone()

    finally:
        cursor.close()
        conexao.close()

def criar_cliente(
    nome,
    cpf,
    telefone,
    email,
    endereco
):
    conexao = get_connection()
    cursor = conexao.cursor()

    try:
        sql = """
            INSERT INTO clientes (
                nome,
                cpf,
                telefone,
                email,
                endereco
            )
            VALUES (%s, %s, %s, %s, %s)
        """

        valores = (
            nome,
            cpf,
            telefone,
            email,
            endereco
        )

        cursor.execute(sql, valores)
        conexao.commit()

        return cursor.lastrowid

    finally:
        cursor.close()
        conexao.close()

def atualizar_cliente(
    id,
    nome,
    cpf,
    telefone,
    email,
    endereco
):
    conexao = get_connection()
    cursor = conexao.cursor()

    try:
        sql = """
            UPDATE clientes
            SET
                nome = %s,
                cpf = %s,
                telefone = %s,
                email = %s,
                endereco = %s
            WHERE id = %s
        """

        valores = (
            nome,
            cpf,
            telefone,
            email,
            endereco,
            id
        )

        cursor.execute(sql, valores)
        conexao.commit()

        return cursor.rowcount

    finally:
        cursor.close()
        conexao.close()

def excluir_cliente(id):
    conexao = get_connection()
    cursor = conexao.cursor()

    try:
        sql = """
            DELETE FROM clientes
            WHERE id = %s
        """

        cursor.execute(sql, (id,))
        conexao.commit()

        return cursor.rowcount

    finally:
        cursor.close()
        conexao.close()