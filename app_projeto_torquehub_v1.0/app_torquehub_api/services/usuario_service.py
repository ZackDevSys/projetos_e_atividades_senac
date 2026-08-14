from werkzeug.security import generate_password_hash
from config.perfis import (
    perfil_valido,
    status_valido
)
from repositories.usuario_repository import (
    listar_usuarios,
    buscar_usuario_por_id,
    criar_usuario,
    atualizar_usuario as atualizar_usuario_repository,
    excluir_usuario as excluir_usuario_repository
)

def buscar_usuarios():
    return listar_usuarios()

def buscar_usuario(id):
    return buscar_usuario_por_id(id)

def cadastrar_usuario(dados):

    nome = dados.get("nome")
    email = dados.get("email")
    senha = dados.get("senha")
    telefone = dados.get("telefone")
    perfil = dados.get("perfil")
    especialidade = dados.get("especialidade")
    status = dados.get("status")

    # Validação do nome
    if not nome or not nome.strip():
        raise ValueError("O nome é obrigatório.")

    # Validação do email
    if not email or not email.strip():
        raise ValueError("O email é obrigatório.")

    # Validação da senha
    if not senha:
        raise ValueError("A senha é obrigatória.")

    if len(senha) < 6:
        raise ValueError("A senha deve possuir pelo menos 6 caracteres.")

    # Validação do perfil
    if not perfil:
        raise ValueError("O perfil é obrigatório.")

    perfil = perfil.strip().upper()

    if not perfil_valido(perfil):
        raise ValueError("Perfil de usuário inválido.")

    # Validação do status
    if not status:
        raise ValueError("O status é obrigatório.")

    status = status.strip().upper()

    if not status_valido(status):
        raise ValueError("Status de usuário inválido.")

    # Normalização
    nome = nome.strip()
    email = email.strip().lower()

    # Criptografa a senha antes de salvar
    senha_hash = generate_password_hash(senha)

    return criar_usuario(
        nome,
        email,
        senha_hash,
        telefone,
        perfil,
        especialidade,
        status
    )

def atualizar_usuario(id, dados):

    nome = dados.get("nome")
    email = dados.get("email")
    senha = dados.get("senha")
    telefone = dados.get("telefone")
    perfil = dados.get("perfil")
    especialidade = dados.get("especialidade")
    status = dados.get("status")

    # Validação do nome
    if not nome or not nome.strip():
        raise ValueError("O nome é obrigatório.")

    # Validação do email
    if not email or not email.strip():
        raise ValueError("O email é obrigatório.")

    # Validação do perfil
    if not perfil:
        raise ValueError("O perfil é obrigatório.")

    perfil = perfil.strip().upper()

    if not perfil_valido(perfil):
        raise ValueError("Perfil de usuário inválido.")

    # Validação do status
    if not status:
        raise ValueError("O status é obrigatório.")

    status = status.strip().upper()

    if not status_valido(status):
        raise ValueError("Status de usuário inválido.")

    # Normalização
    nome = nome.strip()
    email = email.strip().lower()

    # Só altera a senha se uma nova senha foi enviada
    senha_hash = None

    if senha:
        if len(senha) < 6:
            raise ValueError(
                "A senha deve possuir pelo menos 6 caracteres."
            )

        senha_hash = generate_password_hash(senha)

    return atualizar_usuario_repository(
        id,
        nome,
        email,
        senha_hash,
        telefone,
        perfil,
        especialidade,
        status
    )

def excluir_usuario(id):
    return excluir_usuario_repository(id)