class ItemPeca:

    def __init__(
        self,
        id=None,
        ordem_servico_id=None,
        peca_id=None,
        quantidade=None,
        valor_unitario=None,
        valor_total=None
    ):
        self.id = id
        self.ordem_servico_id = ordem_servico_id
        self.peca_id = peca_id
        self.quantidade = quantidade
        self.valor_unitario = valor_unitario
        self.valor_total = valor_total