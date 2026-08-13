from flask import jsonify, request

from services.ordem_servico_usuario_service import (
    buscar_ordens_servico_usuario,
    buscar_ordem_servico_usuario,
    cadastrar_ordem_servico_usuario,
    atualizar_ordem_servico_usuario,
    excluir_ordem_servico_usuario
)


def listar():

    try:

        atribuicoes = buscar_ordens_servico_usuario()

        return jsonify({
            "sucesso": True,
            "quantidade": len(atribuicoes),
            "dados": atribuicoes
        }), 200

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao buscar usuários das ordens de serviço.",
            "erro": str(erro)
        }), 500


def buscar_por_id(id):

    try:

        atribuicao = buscar_ordem_servico_usuario(id)

        if atribuicao is None:

            return jsonify({
                "sucesso": False,
                "mensagem": "Atribuição não encontrada."
            }), 404

        return jsonify({
            "sucesso": True,
            "dados": atribuicao
        }), 200

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao buscar atribuição.",
            "erro": str(erro)
        }), 500


def criar():

    try:

        dados = request.get_json()

        if not dados:

            return jsonify({
                "sucesso": False,
                "mensagem": "Nenhum dado foi enviado."
            }), 400

        id_atribuicao = cadastrar_ordem_servico_usuario(dados)

        return jsonify({
            "sucesso": True,
            "mensagem": "Usuário atribuído à ordem de serviço com sucesso.",
            "id": id_atribuicao
        }), 201

    except ValueError as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": str(erro)
        }), 400

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao atribuir usuário à ordem de serviço.",
            "erro": str(erro)
        }), 500


def atualizar(id):

    try:

        dados = request.get_json()

        if not dados:

            return jsonify({
                "sucesso": False,
                "mensagem": "Nenhum dado foi enviado."
            }), 400

        resultado = atualizar_ordem_servico_usuario(
            id,
            dados
        )

        if resultado == 0:

            return jsonify({
                "sucesso": False,
                "mensagem": "Atribuição não encontrada."
            }), 404

        return jsonify({
            "sucesso": True,
            "mensagem": "Atribuição atualizada com sucesso."
        }), 200

    except ValueError as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": str(erro)
        }), 400

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao atualizar atribuição.",
            "erro": str(erro)
        }), 500


def excluir(id):

    try:

        resultado = excluir_ordem_servico_usuario(id)

        if resultado == 0:

            return jsonify({
                "sucesso": False,
                "mensagem": "Atribuição não encontrada."
            }), 404

        return jsonify({
            "sucesso": True,
            "mensagem": "Atribuição excluída com sucesso."
        }), 200

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao excluir atribuição.",
            "erro": str(erro)
        }), 500