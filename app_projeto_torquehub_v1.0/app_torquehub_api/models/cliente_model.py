class Cliente:

    def __init__(
        self,
        id=None,
        nome=None,
        cpf=None,
        telefone=None,
        email=None,
        endereco=None,
        observacoes=None,
        status="ATIVO",
        data_cadastro=None
    ):

        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.observacoes = observacoes
        self.status = status
        self.data_cadastro = data_cadastro