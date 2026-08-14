from config.database import get_connection

def listar_itens_por_ordem(ordem_servico_id):
    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                i.id,
                i.ordem_servico_id,
                i.servico_id,
                s.nome AS servico_nome,
                s.descricao AS servico_descricao,
                i.quantidade,
                i.valor_unitario,
                i.valor_total
            FROM itens_servico i
            INNER JOIN servicos s
                ON s.id = i.servico_id
            WHERE i.ordem_servico_id = %s
            ORDER BY i.id
        """, (ordem_servico_id,))

        return cursor.fetchall()

    finally:
        cursor.close()
        conexao.close()

def buscar_item_por_id(id):
    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                i.id,
                i.ordem_servico_id,
                i.servico_id,
                s.nome AS servico_nome,
                s.descricao AS servico_descricao,
                i.quantidade,
                i.valor_unitario,
                i.valor_total
            FROM itens_servico i
            INNER JOIN servicos s
                ON s.id = i.servico_id
            WHERE i.id = %s
        """, (id,))

        return cursor.fetchone()

    finally:
        cursor.close()
        conexao.close()

def buscar_servico_por_id(servico_id):
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
        """, (servico_id,))

        return cursor.fetchone()

    finally:
        cursor.close()
        conexao.close()

def criar_item(
    ordem_servico_id,
    servico_id,
    quantidade,
    valor_unitario,
    valor_total
):
    conexao = get_connection()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            INSERT INTO itens_servico (
                ordem_servico_id,
                servico_id,
                quantidade,
                valor_unitario,
                valor_total
            )
            VALUES (%s, %s, %s, %s, %s)
        """, (
            ordem_servico_id,
            servico_id,
            quantidade,
            valor_unitario,
            valor_total
        ))

        conexao.commit()

        return cursor.lastrowid

    finally:
        cursor.close()
        conexao.close()

def atualizar_item(
    id,
    servico_id,
    quantidade,
    valor_unitario,
    valor_total
):
    conexao = get_connection()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            UPDATE itens_servico
            SET
                servico_id = %s,
                quantidade = %s,
                valor_unitario = %s,
                valor_total = %s
            WHERE id = %s
        """, (
            servico_id,
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

def excluir_item(id):
    conexao = get_connection()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            DELETE FROM itens_servico
            WHERE id = %s
        """, (id,))

        conexao.commit()

        return cursor.rowcount

    finally:
        cursor.close()
        conexao.close()

def recalcular_total_ordem(ordem_servico_id):
    conexao = get_connection()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            UPDATE ordens_servico
            SET valor_total = (
                SELECT COALESCE(SUM(valor_total), 0)
                FROM itens_servico
                WHERE ordem_servico_id = %s
            )
            WHERE id = %s
        """, (
            ordem_servico_id,
            ordem_servico_id
        ))

        conexao.commit()

    finally:
        cursor.close()
        conexao.close()