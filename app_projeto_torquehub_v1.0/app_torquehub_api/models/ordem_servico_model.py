class OrdemServico:

    def __init__(
        self,
        id=None,
        numero=None,
        veiculo_id=None,
        usuarios=None,
        data_entrada=None,
        previsao_entrega=None,
        data_conclusao=None,
        data_entrega=None,
        km_entrada=None,
        problema_relatado=None,
        diagnostico=None,
        observacoes=None,
        status=None,
        valor_total=None
    ):
        self.id = id
        self.numero = numero
        self.veiculo_id = veiculo_id
        self.usuarios = usuarios or []
        self.data_entrada = data_entrada
        self.previsao_entrega = previsao_entrega
        self.data_conclusao = data_conclusao
        self.data_entrega = data_entrega
        self.km_entrada = km_entrada
        self.problema_relatado = problema_relatado
        self.diagnostico = diagnostico
        self.observacoes = observacoes
        self.status = status
        self.valor_total = valor_total