from config.database import get_connection


def listar_veiculos():
    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                id,
                cliente_id,
                tipo,
                marca,
                modelo,
                ano,
                placa,
                chassi,
                cor,
                quilometragem,
                observacoes,
                status,
                data_cadastro
            FROM veiculos
            ORDER BY id DESC
        """)

        return cursor.fetchall()

    finally:
        cursor.close()
        conexao.close()


def buscar_veiculo_por_id(id):
    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                id,
                cliente_id,
                tipo,
                marca,
                modelo,
                ano,
                placa,
                chassi,
                cor,
                quilometragem,
                observacoes,
                status,
                data_cadastro
            FROM veiculos
            WHERE id = %s
        """, (id,))

        return cursor.fetchone()

    finally:
        cursor.close()
        conexao.close()


def criar_veiculo(
    cliente_id,
    tipo,
    marca,
    modelo,
    ano,
    placa,
    chassi,
    cor,
    quilometragem,
    observacoes,
    status
):
    conexao = get_connection()
    cursor = conexao.cursor()

    try:
        sql = """
            INSERT INTO veiculos (
                cliente_id,
                tipo,
                marca,
                modelo,
                ano,
                placa,
                chassi,
                cor,
                quilometragem,
                observacoes,
                status
            )
            VALUES (
                %s, %s, %s, %s, %s,
                %s, %s, %s, %s, %s, %s
            )
        """

        valores = (
            cliente_id,
            tipo,
            marca,
            modelo,
            ano,
            placa,
            chassi,
            cor,
            quilometragem,
            observacoes,
            status
        )

        cursor.execute(sql, valores)
        conexao.commit()

        return cursor.lastrowid

    finally:
        cursor.close()
        conexao.close()


def atualizar_veiculo(
    id,
    cliente_id,
    tipo,
    marca,
    modelo,
    ano,
    placa,
    chassi,
    cor,
    quilometragem,
    observacoes,
    status
):
    conexao = get_connection()
    cursor = conexao.cursor()

    try:
        sql = """
            UPDATE veiculos
            SET
                cliente_id = %s,
                tipo = %s,
                marca = %s,
                modelo = %s,
                ano = %s,
                placa = %s,
                chassi = %s,
                cor = %s,
                quilometragem = %s,
                observacoes = %s,
                status = %s
            WHERE id = %s
        """

        valores = (
            cliente_id,
            tipo,
            marca,
            modelo,
            ano,
            placa,
            chassi,
            cor,
            quilometragem,
            observacoes,
            status,
            id
        )

        cursor.execute(sql, valores)
        conexao.commit()

        return cursor.rowcount

    finally:
        cursor.close()
        conexao.close()


def excluir_veiculo(id):
    conexao = get_connection()
    cursor = conexao.cursor()

    try:
        sql = """
            DELETE FROM veiculos
            WHERE id = %s
        """

        cursor.execute(sql, (id,))
        conexao.commit()

        return cursor.rowcount

    finally:
        cursor.close()
        conexao.close()


def cliente_existe(cliente_id):
    conexao = get_connection()
    cursor = conexao.cursor()

    try:
        cursor.execute("""
            SELECT id
            FROM clientes
            WHERE id = %s
        """, (cliente_id,))

        return cursor.fetchone() is not None

    finally:
        cursor.close()
        conexao.close()