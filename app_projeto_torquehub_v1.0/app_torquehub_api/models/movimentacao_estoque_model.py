class MovimentacaoEstoque:

    def __init__(
        self,
        id=None,
        peca_id=None,
        usuario_id=None,
        tipo=None,
        quantidade=None,
        data=None,
        observacao=None
    ):
        self.id = id
        self.peca_id = peca_id
        self.usuario_id = usuario_id
        self.tipo = tipo
        self.quantidade = quantidade
        self.data = data
        self.observacao = observacao