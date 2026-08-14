class Peca:

    def __init__(
        self,
        id=None,
        codigo=None,
        nome_produto=None,
        fabricante=None,
        descricao=None,
        preco_custo=None,
        preco_venda=None,
        estoque_atual=None,
        estoque_minimo=None,
        status=None
    ):
        self.id = id
        self.codigo = codigo
        self.nome_produto = nome_produto
        self.fabricante = fabricante
        self.descricao = descricao
        self.preco_custo = preco_custo
        self.preco_venda = preco_venda
        self.estoque_atual = estoque_atual
        self.estoque_minimo = estoque_minimo
        self.status = status