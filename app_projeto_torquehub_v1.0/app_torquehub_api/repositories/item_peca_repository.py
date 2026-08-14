from config.database import get_connection

def listar_itens_pecas():

    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    try:

        cursor.execute("""
            SELECT
                ip.id,
                ip.ordem_servico_id,
                ip.peca_id,
                p.nome_produto AS nome_produto,
                ip.quantidade,
                ip.valor_unitario,
                ip.valor_total
            FROM itens_pecas ip
            INNER JOIN pecas p
                ON p.id = ip.peca_id
            ORDER BY ip.id DESC
        """)

        itens = cursor.fetchall()

        for item in itens:
            if item["valor_unitario"] is not None:
                item["valor_unitario"] = float(item["valor_unitario"])

            if item["valor_total"] is not None:
                item["valor_total"] = float(item["valor_total"])

            if item["quantidade"] is not None:
                item["quantidade"] = float(item["quantidade"])

        return itens

    finally:
        cursor.close()
        conexao.close()

def buscar_item_peca_por_id(id):

    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    try:

        cursor.execute("""
            SELECT
                ip.id,
                ip.ordem_servico_id,
                ip.peca_id,
                p.nome_produto AS nome_produto,
                ip.quantidade,
                ip.valor_unitario,
                ip.valor_total
            FROM itens_pecas ip
            INNER JOIN pecas p
                ON p.id = ip.peca_id
            WHERE ip.id = %s
        """, (id,))

        item = cursor.fetchone()

        if item:

            if item["valor_unitario"] is not None:
                item["valor_unitario"] = float(
                    item["valor_unitario"]
                )

            if item["valor_total"] is not None:
                item["valor_total"] = float(
                    item["valor_total"]
                )

            if item["quantidade"] is not None:
                item["quantidade"] = float(
                    item["quantidade"]
                )

        return item

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

        return cursor.fetchone() is not None

    finally:
        cursor.close()
        conexao.close()

def buscar_preco_peca(peca_id):

    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    try:

        cursor.execute("""
            SELECT
                id,
                nome_produto,
                preco_venda,
                status
            FROM pecas
            WHERE id = %s
        """, (peca_id,))

        peca = cursor.fetchone()

        if peca and peca["preco_venda"] is not None:
            peca["preco_venda"] = float(
                peca["preco_venda"]
            )

        return peca

    finally:
        cursor.close()
        conexao.close()

def criar_item_peca(
    ordem_servico_id,
    peca_id,
    quantidade,
    valor_unitario,
    valor_total
):

    conexao = get_connection()
    cursor = conexao.cursor()

    try:

        cursor.execute("""
            INSERT INTO itens_pecas (
                ordem_servico_id,
                peca_id,
                quantidade,
                valor_unitario,
                valor_total
            )
            VALUES (%s, %s, %s, %s, %s)
        """, (
            ordem_servico_id,
            peca_id,
            quantidade,
            valor_unitario,
            valor_total
        ))

        conexao.commit()

        return cursor.lastrowid

    finally:
        cursor.close()
        conexao.close()

def atualizar_item_peca(
    id,
    ordem_servico_id,
    peca_id,
    quantidade,
    valor_unitario,
    valor_total
):

    conexao = get_connection()
    cursor = conexao.cursor()

    try:

        cursor.execute("""
            UPDATE itens_pecas
            SET
                ordem_servico_id = %s,
                peca_id = %s,
                quantidade = %s,
                valor_unitario = %s,
                valor_total = %s
            WHERE id = %s
        """, (
            ordem_servico_id,
            peca_id,
            quantidade,
            valor_unitario,
            valor_total,
            id
        ))

        conexao.commit()

        return cursor.rowcount

    finally:
        cursor.close()
        conexao.close()

def excluir_item_peca(id):

    conexao = get_connection()
    cursor = conexao.cursor()

    try:

        cursor.execute("""
            DELETE FROM itens_pecas
            WHERE id = %s
        """, (id,))

        conexao.commit()

        return cursor.rowcount

    finally:
        cursor.close()
        conexao.close()