from repositories.item_peca_repository import (
    listar_itens_pecas,
    buscar_item_peca_por_id,
    verificar_ordem_servico,
    buscar_preco_peca,
    criar_item_peca,
    atualizar_item_peca,
    excluir_item_peca
)

def buscar_itens_pecas():

    return listar_itens_pecas()

def buscar_item_peca(id):

    return buscar_item_peca_por_id(id)

def validar_dados(ordem_servico_id, peca_id, quantidade):

    if not ordem_servico_id:
        raise ValueError(
            "O ordem_servico_id é obrigatório."
        )

    if not peca_id:
        raise ValueError(
            "O peca_id é obrigatório."
        )

    if quantidade is None:
        raise ValueError(
            "A quantidade é obrigatória."
        )

    try:
        quantidade = float(quantidade)
    except (ValueError, TypeError):
        raise ValueError(
            "A quantidade deve ser numérica."
        )

    if quantidade <= 0:
        raise ValueError(
            "A quantidade deve ser maior que zero."
        )

    if not verificar_ordem_servico(ordem_servico_id):
        raise ValueError(
            "A ordem de serviço informada não existe."
        )

    peca = buscar_preco_peca(peca_id)

    if peca is None:
        raise ValueError(
            "A peça informada não existe."
        )

    if peca["status"] != "ATIVO":
        raise ValueError(
            "A peça informada está inativa."
        )

    return quantidade, peca

def cadastrar_item_peca(dados):

    ordem_servico_id = dados.get("ordem_servico_id")
    peca_id = dados.get("peca_id")
    quantidade = dados.get("quantidade")

    quantidade, peca = validar_dados(
        ordem_servico_id,
        peca_id,
        quantidade
    )

    valor_unitario = float(
        peca["preco_venda"]
    )

    valor_total = quantidade * valor_unitario

    return criar_item_peca(
        ordem_servico_id,
        peca_id,
        quantidade,
        valor_unitario,
        valor_total
    )

def atualizar_item_peca_service(id, dados):

    item = buscar_item_peca_por_id(id)

    if item is None:
        return 0

    ordem_servico_id = dados.get("ordem_servico_id")
    peca_id = dados.get("peca_id")
    quantidade = dados.get("quantidade")

    quantidade, peca = validar_dados(
        ordem_servico_id,
        peca_id,
        quantidade
    )

    valor_unitario = float(
        peca["preco_venda"]
    )

    valor_total = quantidade * valor_unitario

    atualizar_item_peca(
        id,
        ordem_servico_id,
        peca_id,
        quantidade,
        valor_unitario,
        valor_total
    )

    return 1

def excluir_item_peca_service(id):

    return excluir_item_peca(id)