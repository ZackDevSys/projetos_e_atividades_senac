class OrdemServicoUsuario:

    def __init__(
        self,
        id=None,
        ordem_servico_id=None,
        usuario_id=None,
        perfil=None,
        data_atribuicao=None,
        observacoes=None,
        nome_usuario=None
    ):
        self.id = id
        self.ordem_servico_id = ordem_servico_id
        self.usuario_id = usuario_id
        self.perfil = perfil
        self.data_atribuicao = data_atribuicao
        self.observacoes = observacoes
        self.nome_usuario = nome_usuario