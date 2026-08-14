from repositories.peca_repository import (
    listar_pecas,
    buscar_peca_por_id,
    criar_peca,
    atualizar_peca,
    excluir_peca
)

STATUS_VALIDOS = [
    "ATIVO",
    "INATIVO"
]

def validar_status(status):

    if status is None:
        return "ATIVO"

    if status not in STATUS_VALIDOS:
        raise ValueError(
            "Status inválido. Utilize ATIVO ou INATIVO."
        )

    return status

def buscar_pecas():

    return listar_pecas()

def buscar_peca(id):

    return buscar_peca_por_id(id)

def cadastrar_peca(dados):

    codigo = dados.get("codigo")
    nome_produto = dados.get("nome_produto")

    if not codigo:
        raise ValueError(
            "O codigo é obrigatório."
        )

    if not nome_produto:
        raise ValueError(
            "O nome_produto é obrigatório."
        )

    preco_custo = dados.get("preco_custo", 0)
    preco_venda = dados.get("preco_venda", 0)
    estoque_minimo = dados.get("estoque_minimo", 0)

    status = validar_status(
        dados.get("status")
    )

    return criar_peca(
        codigo,
        nome_produto,
        dados.get("fabricante"),
        dados.get("descricao"),
        preco_custo,
        preco_venda,
        estoque_minimo,
        status
    )

def atualizar_peca_service(id, dados):

    # Primeiro verifica se a peça realmente existe
    peca = buscar_peca_por_id(id)

    if peca is None:
        return 0

    nome_produto = dados.get("nome_produto")

    if not nome_produto:
        raise ValueError(
            "O nome_produto é obrigatório."
        )

    status = validar_status(
        dados.get("status")
    )

    atualizar_peca(
        id,
        dados.get("codigo"),
        nome_produto,
        dados.get("fabricante"),
        dados.get("descricao"),
        dados.get("preco_custo", 0),
        dados.get("preco_venda", 0),
        dados.get("estoque_minimo", 0),
        status
    )

    # A peça existe, então consideramos a atualização válida,
    # mesmo que os dados enviados sejam iguais aos atuais.
    return 1

def excluir_peca_service(id):

    return excluir_peca(id)