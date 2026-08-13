from decimal import Decimal

from repositories.item_servico_repository import (
    listar_itens_por_ordem,
    buscar_item_por_id,
    buscar_servico_por_id,
    criar_item,
    atualizar_item as atualizar_repository,
    excluir_item as excluir_repository,
    recalcular_total_ordem
)


def listar_itens(ordem_servico_id):
    return listar_itens_por_ordem(ordem_servico_id)


def buscar_item(id):
    return buscar_item_por_id(id)


def cadastrar_item(ordem_servico_id, dados):

    servico_id = dados.get("servico_id")
    quantidade = dados.get("quantidade")

    if not servico_id:
        raise ValueError("O servico_id é obrigatório.")

    if quantidade is None:
        raise ValueError("A quantidade é obrigatória.")

    quantidade = Decimal(str(quantidade))

    if quantidade <= 0:
        raise ValueError("A quantidade deve ser maior que zero.")

    servico = buscar_servico_por_id(servico_id)

    if not servico:
        raise ValueError("Serviço não encontrado.")

    valor_unitario = Decimal(str(servico["valor_base"]))

    valor_total = quantidade * valor_unitario

    id_item = criar_item(
        ordem_servico_id,
        servico_id,
        quantidade,
        valor_unitario,
        valor_total
    )

    recalcular_total_ordem(ordem_servico_id)

    return id_item


def atualizar_item(id, dados):

    item = buscar_item_por_id(id)

    if not item:
        raise ValueError("Item de serviço não encontrado.")

    servico_id = dados.get("servico_id")
    quantidade = dados.get("quantidade")

    if not servico_id:
        raise ValueError("O servico_id é obrigatório.")

    if quantidade is None:
        raise ValueError("A quantidade é obrigatória.")

    quantidade = Decimal(str(quantidade))

    if quantidade <= 0:
        raise ValueError("A quantidade deve ser maior que zero.")

    servico = buscar_servico_por_id(servico_id)

    if not servico:
        raise ValueError("Serviço não encontrado.")

    valor_unitario = Decimal(str(servico["valor_base"]))

    valor_total = quantidade * valor_unitario

    resultado = atualizar_repository(
        id,
        servico_id,
        quantidade,
        valor_unitario,
        valor_total
    )

    recalcular_total_ordem(item["ordem_servico_id"])

    return resultado


def excluir_item(id):

    item = buscar_item_por_id(id)

    if not item:
        raise ValueError("Item de serviço não encontrado.")

    resultado = excluir_repository(id)

    recalcular_total_ordem(item["ordem_servico_id"])

    return resultado