class Cliente:
    
    def __init__(
        self,
        id=None,
        nome=None,
        cpf=None,
        telefone=None,
        email=None,
        endereco=None,
        data_cadastro=None
    ):
        self.id = id
        self.nome = nome
        self.cpf = cpf
        self.telefone = telefone
        self.email = email
        self.endereco = endereco
        self.data_cadastro = data_cadastro