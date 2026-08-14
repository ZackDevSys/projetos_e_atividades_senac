from repositories.servico_repository import (
    listar_servicos,
    buscar_servico_por_id,
    criar_servico,
    atualizar_servico as atualizar_servico_repository,
    excluir_servico as excluir_servico_repository
)

STATUS_SERVICO = [
    "ATIVO",
    "INATIVO"
]

def buscar_servicos():
    return listar_servicos()

def buscar_servico(id):
    return buscar_servico_por_id(id)

def validar_dados(dados):

    nome = dados.get("nome")
    descricao = dados.get("descricao")
    valor_base = dados.get("valor_base")
    tempo_estimado = dados.get("tempo_estimado")
    status = dados.get("status", "ATIVO")

    if not nome or not str(nome).strip():
        raise ValueError("O nome do serviço é obrigatório.")

    if valor_base is None:
        raise ValueError("O valor_base é obrigatório.")

    try:
        valor_base = float(valor_base)
    except (ValueError, TypeError):
        raise ValueError(
            "O valor_base deve ser um número válido."
        )

    if valor_base < 0:
        raise ValueError(
            "O valor_base não pode ser negativo."
        )

    if tempo_estimado is None:
        raise ValueError(
            "O tempo_estimado é obrigatório."
        )

    try:
        tempo_estimado = int(tempo_estimado)
    except (ValueError, TypeError):
        raise ValueError(
            "O tempo_estimado deve ser um número inteiro."
        )

    if tempo_estimado <= 0:
        raise ValueError(
            "O tempo_estimado deve ser maior que zero."
        )

    if status not in STATUS_SERVICO:
        raise ValueError(
            "Status inválido. Use ATIVO ou INATIVO."
        )

    return (
        nome.strip(),
        descricao,
        valor_base,
        tempo_estimado,
        status
    )

def cadastrar_servico(dados):

    valores = validar_dados(dados)

    return criar_servico(*valores)

def atualizar_servico(id, dados):

    valores = validar_dados(dados)

    return atualizar_servico_repository(
        id,
        *valores
    )

def excluir_servico(id):

    return excluir_servico_repository(id)