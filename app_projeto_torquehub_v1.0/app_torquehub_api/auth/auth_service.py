from werkzeug.security import check_password_hash
from config.perfis import status_valido
from auth.auth_repository import buscar_usuario_por_email

def autenticar_usuario(email, senha):

    # Validação do email
    if not email or not email.strip():
        raise ValueError("O email é obrigatório.")

    # Validação da senha
    if not senha:
        raise ValueError("A senha é obrigatória.")

    # Normalização
    email = email.strip().lower()

    # Busca o usuário pelo email
    usuario = buscar_usuario_por_email(email)

    # Não revela se o email existe ou não
    if usuario is None:
        raise PermissionError("E-mail ou senha inválidos.")

    # Verifica a senha
    senha_correta = check_password_hash(
        usuario["senha"],
        senha
    )

    if not senha_correta:
        raise PermissionError("E-mail ou senha inválidos.")

    # Verifica o status
    status = usuario["status"]

    if not status_valido(status):
        raise PermissionError("Status do usuário inválido.")

    if status != "ATIVO":
        raise PermissionError(
            "Usuário inativo. Acesso não permitido."
        )

    # Retorna somente os dados necessários para o Front-end
    return {
        "id": usuario["id"],
        "nome": usuario["nome"],
        "email": usuario["email"],
        "telefone": usuario["telefone"],
        "perfil": usuario["perfil"],
        "especialidade": usuario["especialidade"],
        "status": usuario["status"],
        "data_cadastro": usuario["data_cadastro"]
    }