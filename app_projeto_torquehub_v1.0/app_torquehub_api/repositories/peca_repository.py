from config.database import get_connection

def listar_pecas():

    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    try:

        cursor.execute("""
            SELECT
                id,
                codigo,
                nome_produto,
                fabricante,
                descricao,
                preco_custo,
                preco_venda,
                estoque_atual,
                estoque_minimo,
                status
            FROM pecas
            ORDER BY id DESC
        """)

        return cursor.fetchall()

    finally:

        cursor.close()
        conexao.close()

def buscar_peca_por_id(id):

    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    try:

        cursor.execute("""
            SELECT
                id,
                codigo,
                nome_produto,
                fabricante,
                descricao,
                preco_custo,
                preco_venda,
                estoque_atual,
                estoque_minimo,
                status
            FROM pecas
            WHERE id = %s
        """, (id,))

        return cursor.fetchone()

    finally:

        cursor.close()
        conexao.close()

def criar_peca(
    codigo,
    nome_produto,
    fabricante,
    descricao,
    preco_custo,
    preco_venda,
    estoque_minimo,
    status
):

    conexao = get_connection()
    cursor = conexao.cursor()

    try:

        sql = """
            INSERT INTO pecas (
                codigo,
                nome_produto,
                fabricante,
                descricao,
                preco_custo,
                preco_venda,
                estoque_atual,
                estoque_minimo,
                status
            )
            VALUES (
                %s, %s, %s, %s, %s, %s, %s, %s, %s
            )
        """

        valores = (
            codigo,
            nome_produto,
            fabricante,
            descricao,
            preco_custo,
            preco_venda,
            0,
            estoque_minimo,
            status
        )

        cursor.execute(sql, valores)

        conexao.commit()

        return cursor.lastrowid

    finally:

        cursor.close()
        conexao.close()

def atualizar_peca(
    id,
    codigo,
    nome_produto,
    fabricante,
    descricao,
    preco_custo,
    preco_venda,
    estoque_minimo,
    status
):

    conexao = get_connection()
    cursor = conexao.cursor()

    try:

        sql = """
            UPDATE pecas
            SET
                codigo = %s,
                nome_produto = %s,
                fabricante = %s,
                descricao = %s,
                preco_custo = %s,
                preco_venda = %s,
                estoque_minimo = %s,
                status = %s
            WHERE id = %s
        """

        valores = (
            codigo,
            nome_produto,
            fabricante,
            descricao,
            preco_custo,
            preco_venda,
            estoque_minimo,
            status,
            id
        )

        cursor.execute(sql, valores)

        conexao.commit()

        return cursor.rowcount

    finally:

        cursor.close()
        conexao.close()

def excluir_peca(id):

    conexao = get_connection()
    cursor = conexao.cursor()

    try:

        cursor.execute("""
            DELETE FROM pecas
            WHERE id = %s
        """, (id,))

        conexao.commit()

        return cursor.rowcount

    finally:

        cursor.close()
        conexao.close()