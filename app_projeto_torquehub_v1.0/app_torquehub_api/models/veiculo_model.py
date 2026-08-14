class Veiculo:
    
    def __init__(
        self,
        id=None,
        cliente_id=None,
        tipo=None,
        marca=None,
        modelo=None,
        ano=None,
        placa=None,
        quilometragem=None,
        cor=None,
        chassi=None,
        status=None
    ):
        self.id = id
        self.cliente_id = cliente_id
        self.tipo = tipo
        self.marca = marca
        self.modelo = modelo
        self.ano = ano
        self.placa = placa
        self.quilometragem = quilometragem
        self.cor = cor
        self.chassi = chassi
        self.status = status