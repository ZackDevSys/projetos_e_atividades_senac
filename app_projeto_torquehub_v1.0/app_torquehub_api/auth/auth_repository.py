from config.database import get_connection

def buscar_usuario_por_email(email):
    conexao = get_connection()
    cursor = conexao.cursor(dictionary=True)

    try:
        cursor.execute("""
            SELECT
                id,
                nome,
                email,
                senha,
                telefone,
                perfil,
                especialidade,
                status,
                data_cadastro
            FROM usuarios
            WHERE email = %s
        """, (email,))

        return cursor.fetchone()

    finally:
        cursor.close()
        conexao.close()