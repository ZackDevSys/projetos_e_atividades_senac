from repositories.veiculo_repository import (
    listar_veiculos,
    buscar_veiculo_por_id,
    criar_veiculo,
    atualizar_veiculo as atualizar_veiculo_repository,
    excluir_veiculo as excluir_veiculo_repository,
    cliente_existe
)

TIPOS_VEICULO = [
    "MOTOCICLETA",
    "CARRO",
    "CAMINHONETE",
    "VAN",
    "UTILITARIO",
    "OUTRO"
]

STATUS_VEICULO = [
    "ATIVO",
    "INATIVO"
]

def buscar_veiculos():
    return listar_veiculos()

def buscar_veiculo(id):
    return buscar_veiculo_por_id(id)

def validar_dados(dados):

    cliente_id = dados.get("cliente_id")
    tipo = dados.get("tipo")
    marca = dados.get("marca")
    modelo = dados.get("modelo")
    ano = dados.get("ano")

    if not cliente_id:
        raise ValueError("O cliente_id é obrigatório.")

    if not cliente_existe(cliente_id):
        raise ValueError("O cliente informado não existe.")

    if not tipo:
        raise ValueError("O tipo do veículo é obrigatório.")

    if tipo not in TIPOS_VEICULO:
        raise ValueError(
            "Tipo de veículo inválido. "
            "Use: MOTOCICLETA, CARRO, CAMINHONETE, "
            "VAN, UTILITARIO ou OUTRO."
        )

    if not marca:
        raise ValueError("A marca é obrigatória.")

    if not modelo:
        raise ValueError("O modelo é obrigatório.")

    if not ano:
        raise ValueError("O ano é obrigatório.")

    try:
        ano = int(ano)
    except (ValueError, TypeError):
        raise ValueError("O ano deve ser um número válido.")

    if ano < 1900 or ano > 2100:
        raise ValueError("O ano informado é inválido.")

    placa = dados.get("placa")

    chassi = dados.get("chassi")

    cor = dados.get("cor")

    quilometragem = dados.get("quilometragem", 0)

    try:
        quilometragem = int(quilometragem)
    except (ValueError, TypeError):
        raise ValueError(
            "A quilometragem deve ser um número inteiro."
        )

    if quilometragem < 0:
        raise ValueError(
            "A quilometragem não pode ser negativa."
        )

    observacoes = dados.get("observacoes")

    status = dados.get("status", "ATIVO")

    if status not in STATUS_VEICULO:
        raise ValueError(
            "Status inválido. Use ATIVO ou INATIVO."
        )

    return (
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

def cadastrar_veiculo(dados):

    valores = validar_dados(dados)

    return criar_veiculo(*valores)

def atualizar_veiculo(id, dados):

    valores = validar_dados(dados)

    return atualizar_veiculo_repository(
        id,
        *valores
    )

def excluir_veiculo(id):

    return excluir_veiculo_repository(id)