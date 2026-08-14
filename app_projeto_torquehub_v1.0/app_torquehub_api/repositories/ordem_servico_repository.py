from config.database import get_connection

def listar_ordens_servico():

    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    try:

        cursor.execute("""
            SELECT
                id,
                numero,
                veiculo_id,
                data_entrada,
                previsao_entrega,
                data_conclusao,
                data_entrega,
                km_entrada,
                problema_relatado,
                diagnostico,
                observacoes,
                status,
                valor_total
            FROM ordens_servico
            ORDER BY id DESC
        """)

        ordens = cursor.fetchall()

        # Busca os usuários vinculados às ordens
        for ordem in ordens:

            cursor.execute("""
                SELECT
                    osu.usuario_id,
                    u.nome AS nome_usuario,
                    osu.perfil,
                    osu.data_atribuicao,
                    osu.observacoes
                FROM ordem_servico_usuario osu
                INNER JOIN usuarios u
                    ON u.id = osu.usuario_id
                WHERE osu.ordem_servico_id = %s
                ORDER BY osu.id
            """, (ordem["id"],))

            ordem["usuarios"] = cursor.fetchall()

        return ordens

    finally:

        cursor.close()
        conexao.close()

def buscar_ordem_servico_por_id(id):

    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    try:

        cursor.execute("""
            SELECT
                id,
                numero,
                veiculo_id,
                data_entrada,
                previsao_entrega,
                data_conclusao,
                data_entrega,
                km_entrada,
                problema_relatado,
                diagnostico,
                observacoes,
                status,
                valor_total
            FROM ordens_servico
            WHERE id = %s
        """, (id,))

        ordem = cursor.fetchone()

        if ordem is None:
            return None

        cursor.execute("""
            SELECT
                osu.usuario_id,
                u.nome AS nome_usuario,
                osu.perfil,
                osu.data_atribuicao,
                osu.observacoes
            FROM ordem_servico_usuario osu
            INNER JOIN usuarios u
                ON u.id = osu.usuario_id
            WHERE osu.ordem_servico_id = %s
            ORDER BY osu.id
        """, (id,))

        ordem["usuarios"] = cursor.fetchall()

        return ordem

    finally:

        cursor.close()
        conexao.close()

def criar_ordem_servico(
    numero,
    veiculo_id,
    data_entrada,
    previsao_entrega,
    data_conclusao,
    data_entrega,
    km_entrada,
    problema_relatado,
    diagnostico,
    observacoes,
    status,
    valor_total,
    usuarios
):

    conexao = get_connection()
    cursor = conexao.cursor()

    try:

        sql = """
            INSERT INTO ordens_servico (
                numero,
                veiculo_id,
                data_entrada,
                previsao_entrega,
                data_conclusao,
                data_entrega,
                km_entrada,
                problema_relatado,
                diagnostico,
                observacoes,
                status,
                valor_total
            )
            VALUES (
                %s, %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s
            )
        """

        valores = (
            numero,
            veiculo_id,
            data_entrada,
            previsao_entrega,
            data_conclusao,
            data_entrega,
            km_entrada,
            problema_relatado,
            diagnostico,
            observacoes,
            status,
            valor_total
        )

        cursor.execute(sql, valores)

        id_ordem = cursor.lastrowid

        # Vincula os usuários à OS
        for usuario in usuarios:

            cursor.execute("""
                INSERT INTO ordem_servico_usuario (
                    ordem_servico_id,
                    usuario_id,
                    perfil,
                    observacoes
                )
                VALUES (%s, %s, %s, %s)
            """, (
                id_ordem,
                usuario["usuario_id"],
                usuario["perfil"],
                usuario.get("observacoes")
            ))

        conexao.commit()

        return id_ordem

    except Exception:

        conexao.rollback()
        raise

    finally:

        cursor.close()
        conexao.close()

def atualizar_ordem_servico(
    id,
    veiculo_id,
    previsao_entrega,
    data_conclusao,
    data_entrega,
    km_entrada,
    problema_relatado,
    diagnostico,
    observacoes,
    status,
    valor_total,
    usuarios
):

    conexao = get_connection()
    cursor = conexao.cursor()

    try:

        sql = """
            UPDATE ordens_servico
            SET
                veiculo_id = %s,
                previsao_entrega = %s,
                data_conclusao = %s,
                data_entrega = %s,
                km_entrada = %s,
                problema_relatado = %s,
                diagnostico = %s,
                observacoes = %s,
                status = %s,
                valor_total = %s
            WHERE id = %s
        """

        valores = (
            veiculo_id,
            previsao_entrega,
            data_conclusao,
            data_entrega,
            km_entrada,
            problema_relatado,
            diagnostico,
            observacoes,
            status,
            valor_total,
            id
        )

        cursor.execute(sql, valores)

        if cursor.rowcount == 0:

            conexao.rollback()
            return 0

        # Remove os vínculos antigos
        cursor.execute("""
            DELETE FROM ordem_servico_usuario
            WHERE ordem_servico_id = %s
        """, (id,))

        # Cria os novos vínculos
        for usuario in usuarios:

            cursor.execute("""
                INSERT INTO ordem_servico_usuario (
                    ordem_servico_id,
                    usuario_id,
                    perfil,
                    observacoes
                )
                VALUES (%s, %s, %s, %s)
            """, (
                id,
                usuario["usuario_id"],
                usuario["perfil"],
                usuario.get("observacoes")
            ))

        conexao.commit()

        return 1

    except Exception:

        conexao.rollback()
        raise

    finally:

        cursor.close()
        conexao.close()

def excluir_ordem_servico(id):

    conexao = get_connection()
    cursor = conexao.cursor()

    try:

        cursor.execute("""
            DELETE FROM ordens_servico
            WHERE id = %s
        """, (id,))

        conexao.commit()

        return cursor.rowcount

    finally:

        cursor.close()
        conexao.close()