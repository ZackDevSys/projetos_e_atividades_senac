PERFIS_VALIDOS = [
    "ADMINISTRADOR",
    "FUNCIONARIO",
    "MECANICO",
    "ESTOQUISTA",
    "ATENDENTE"
]

STATUS_VALIDOS = [
    "ATIVO",
    "INATIVO"
]


def perfil_valido(perfil):
    return perfil in PERFIS_VALIDOS


def status_valido(status):
    return status in STATUS_VALIDOS