class Usuario:
    def __init__(
        self,
        id=None,
        nome=None,
        email=None,
        senha=None,
        telefone=None,
        perfil=None,
        especialidade=None,
        status=None,
        data_cadastro=None
    ):
        self.id = id
        self.nome = nome
        self.email = email
        self.senha = senha
        self.telefone = telefone
        self.perfil = perfil
        self.especialidade = especialidade
        self.status = status
        self.data_cadastro = data_cadastro