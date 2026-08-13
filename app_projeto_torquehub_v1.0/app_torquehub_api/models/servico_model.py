class Servico:
    def __init__(
        self,
        id=None,
        nome=None,
        descricao=None,
        valor_base=None,
        tempo_estimado=None,
        status=None
    ):
        self.id = id
        self.nome = nome
        self.descricao = descricao
        self.valor_base = valor_base
        self.tempo_estimado = tempo_estimado
        self.status = status