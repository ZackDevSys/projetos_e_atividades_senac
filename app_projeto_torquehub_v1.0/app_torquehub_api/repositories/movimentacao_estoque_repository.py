from config.database import get_connection

def listar_movimentacoes():
    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                me.id,
                me.peca_id,
                p.nome_produto,
                me.usuario_id,
                u.nome AS usuario_nome,
                me.tipo,
                me.quantidade,
                me.data,
                me.observacao
            FROM movimentacoes_estoque me
            INNER JOIN pecas p
                ON p.id = me.peca_id
            INNER JOIN usuarios u
                ON u.id = me.usuario_id
            ORDER BY me.id DESC
        """)

        return cursor.fetchall()

    finally:
        cursor.close()
        conexao.close()

def buscar_movimentacao_por_id(id):
    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                me.id,
                me.peca_id,
                p.nome_produto,
                me.usuario_id,
                u.nome AS usuario_nome,
                me.tipo,
                me.quantidade,
                me.data,
                me.observacao
            FROM movimentacoes_estoque me
            INNER JOIN pecas p
                ON p.id = me.peca_id
            INNER JOIN usuarios u
                ON u.id = me.usuario_id
            WHERE me.id = %s
        """, (id,))

        return cursor.fetchone()

    finally:
        cursor.close()
        conexao.close()

def criar_movimentacao(
    peca_id,
    usuario_id,
    tipo,
    quantidade,
    observacao
):
    conexao = get_connection()
    cursor = conexao.cursor()

    try:

        # Verifica a peça e bloqueia o registro durante a operação
        cursor.execute("""
            SELECT estoque_atual
            FROM pecas
            WHERE id = %s
            FOR UPDATE
        """, (peca_id,))

        peca = cursor.fetchone()

        if peca is None:
            raise ValueError("Peça não encontrada.")

        estoque_atual = peca[0]

        if tipo == "ENTRADA":

            novo_estoque = estoque_atual + quantidade

        else:

            if quantidade > estoque_atual:
                raise ValueError(
                    "Estoque insuficiente para realizar a saída."
                )

            novo_estoque = estoque_atual - quantidade

        # Atualiza o estoque
        cursor.execute("""
            UPDATE pecas
            SET estoque_atual = %s
            WHERE id = %s
        """, (novo_estoque, peca_id))

        # Registra a movimentação
        cursor.execute("""
            INSERT INTO movimentacoes_estoque (
                peca_id,
                usuario_id,
                tipo,
                quantidade,
                data,
                observacao
            )
            VALUES (
                %s, %s, %s, %s, NOW(), %s
            )
        """, (
            peca_id,
            usuario_id,
            tipo,
            quantidade,
            observacao
        ))

        conexao.commit()

        return cursor.lastrowid

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()

def atualizar_movimentacao(
    id,
    peca_id,
    usuario_id,
    tipo,
    quantidade,
    observacao
):
    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    try:

        # Busca a movimentação original
        cursor.execute("""
            SELECT
                peca_id,
                tipo,
                quantidade
            FROM movimentacoes_estoque
            WHERE id = %s
            FOR UPDATE
        """, (id,))

        movimentacao = cursor.fetchone()

        if movimentacao is None:
            return 0

        peca_id_antiga = movimentacao["peca_id"]
        tipo_antigo = movimentacao["tipo"]
        quantidade_antiga = movimentacao["quantidade"]

        # Reverte a movimentação anterior
        cursor.execute("""
            SELECT estoque_atual
            FROM pecas
            WHERE id = %s
            FOR UPDATE
        """, (peca_id_antiga,))

        peca_antiga = cursor.fetchone()

        estoque_antigo = peca_antiga["estoque_atual"]

        if tipo_antigo == "ENTRADA":
            estoque_revertido = estoque_antigo - quantidade_antiga
        else:
            estoque_revertido = estoque_antigo + quantidade_antiga

        if estoque_revertido < 0:
            raise ValueError(
                "Não foi possível reverter a movimentação anterior."
            )

        cursor.execute("""
            UPDATE pecas
            SET estoque_atual = %s
            WHERE id = %s
        """, (
            estoque_revertido,
            peca_id_antiga
        ))

        # Busca a nova peça
        cursor.execute("""
            SELECT estoque_atual
            FROM pecas
            WHERE id = %s
            FOR UPDATE
        """, (peca_id,))

        nova_peca = cursor.fetchone()

        if nova_peca is None:
            raise ValueError("Peça não encontrada.")

        novo_estoque = nova_peca["estoque_atual"]

        if tipo == "ENTRADA":

            novo_estoque += quantidade

        else:

            if quantidade > novo_estoque:
                raise ValueError(
                    "Estoque insuficiente para realizar a saída."
                )

            novo_estoque -= quantidade

        # Atualiza o estoque da nova peça
        cursor.execute("""
            UPDATE pecas
            SET estoque_atual = %s
            WHERE id = %s
        """, (
            novo_estoque,
            peca_id
        ))

        # Atualiza a movimentação
        cursor.execute("""
            UPDATE movimentacoes_estoque
            SET
                peca_id = %s,
                usuario_id = %s,
                tipo = %s,
                quantidade = %s,
                observacao = %s
            WHERE id = %s
        """, (
            peca_id,
            usuario_id,
            tipo,
            quantidade,
            observacao,
            id
        ))

        conexao.commit()

        return cursor.rowcount

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()

def excluir_movimentacao(id):
    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    try:

        cursor.execute("""
            SELECT
                peca_id,
                tipo,
                quantidade
            FROM movimentacoes_estoque
            WHERE id = %s
            FOR UPDATE
        """, (id,))

        movimentacao = cursor.fetchone()

        if movimentacao is None:
            return 0

        peca_id = movimentacao["peca_id"]
        tipo = movimentacao["tipo"]
        quantidade = movimentacao["quantidade"]

        cursor.execute("""
            SELECT estoque_atual
            FROM pecas
            WHERE id = %s
            FOR UPDATE
        """, (peca_id,))

        peca = cursor.fetchone()

        if peca is None:
            raise ValueError("Peça relacionada não encontrada.")

        estoque_atual = peca["estoque_atual"]

        # Ao excluir, desfaz o efeito da movimentação
        if tipo == "ENTRADA":

            if quantidade > estoque_atual:
                raise ValueError(
                    "Não é possível excluir esta entrada, "
                    "pois o estoque atual é menor que a quantidade "
                    "da movimentação."
                )

            novo_estoque = estoque_atual - quantidade

        else:

            novo_estoque = estoque_atual + quantidade

        cursor.execute("""
            UPDATE pecas
            SET estoque_atual = %s
            WHERE id = %s
        """, (
            novo_estoque,
            peca_id
        ))

        cursor.execute("""
            DELETE FROM movimentacoes_estoque
            WHERE id = %s
        """, (id,))

        conexao.commit()

        return cursor.rowcount

    except Exception:
        conexao.rollback()
        raise

    finally:
        cursor.close()
        conexao.close()

def buscar_usuario_para_movimentacao(usuario_id):
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