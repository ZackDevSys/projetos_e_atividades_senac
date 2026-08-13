from flask import jsonify, request

from services.ordem_servico_service import (
    buscar_ordens,
    buscar_ordem,
    cadastrar_ordem,
    atualizar_ordem,
    excluir_ordem
)


def listar():

    try:

        ordens = buscar_ordens()

        return jsonify({
            "sucesso": True,
            "quantidade": len(ordens),
            "dados": ordens
        }), 200

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao buscar ordens de serviço.",
            "erro": str(erro)
        }), 500


def buscar_por_id(id):

    try:

        ordem = buscar_ordem(id)

        if ordem is None:

            return jsonify({
                "sucesso": False,
                "mensagem": "Ordem de serviço não encontrada."
            }), 404

        return jsonify({
            "sucesso": True,
            "dados": ordem
        }), 200

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao buscar ordem de serviço.",
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

        id_ordem = cadastrar_ordem(dados)

        return jsonify({
            "sucesso": True,
            "mensagem": "Ordem de serviço criada com sucesso.",
            "id": id_ordem
        }), 201

    except ValueError as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": str(erro)
        }), 400

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao criar ordem de serviço.",
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

        resultado = atualizar_ordem(id, dados)

        if resultado == 0:

            return jsonify({
                "sucesso": False,
                "mensagem": "Ordem de serviço não encontrada."
            }), 404

        return jsonify({
            "sucesso": True,
            "mensagem": "Ordem de serviço atualizada com sucesso."
        }), 200

    except ValueError as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": str(erro)
        }), 400

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao atualizar ordem de serviço.",
            "erro": str(erro)
        }), 500


def excluir(id):

    try:

        resultado = excluir_ordem(id)

        if resultado == 0:

            return jsonify({
                "sucesso": False,
                "mensagem": "Ordem de serviço não encontrada."
            }), 404

        return jsonify({
            "sucesso": True,
            "mensagem": "Ordem de serviço excluída com sucesso."
        }), 200

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao excluir ordem de serviço.",
            "erro": str(erro)
        }), 500