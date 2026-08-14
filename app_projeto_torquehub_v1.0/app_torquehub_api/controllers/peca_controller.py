from flask import jsonify, request

from services.peca_service import (
    buscar_pecas,
    buscar_peca,
    cadastrar_peca,
    atualizar_peca_service,
    excluir_peca_service
)

def listar():

    try:

        pecas = buscar_pecas()

        return jsonify({
            "sucesso": True,
            "quantidade": len(pecas),
            "dados": pecas
        }), 200

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao buscar peças.",
            "erro": str(erro)
        }), 500

def buscar_por_id(id):

    try:

        peca = buscar_peca(id)

        if peca is None:

            return jsonify({
                "sucesso": False,
                "mensagem": "Peça não encontrada."
            }), 404

        return jsonify({
            "sucesso": True,
            "dados": peca
        }), 200

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao buscar peça.",
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

        id_peca = cadastrar_peca(dados)

        return jsonify({
            "sucesso": True,
            "mensagem": "Peça cadastrada com sucesso.",
            "id": id_peca
        }), 201

    except ValueError as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": str(erro)
        }), 400

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao cadastrar peça.",
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

        resultado = atualizar_peca_service(
            id,
            dados
        )

        if resultado == 0:

            return jsonify({
                "sucesso": False,
                "mensagem": "Peça não encontrada."
            }), 404

        return jsonify({
            "sucesso": True,
            "mensagem": "Peça atualizada com sucesso."
        }), 200

    except ValueError as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": str(erro)
        }), 400

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao atualizar peça.",
            "erro": str(erro)
        }), 500

def excluir(id):

    try:

        resultado = excluir_peca_service(id)

        if resultado == 0:

            return jsonify({
                "sucesso": False,
                "mensagem": "Peça não encontrada."
            }), 404

        return jsonify({
            "sucesso": True,
            "mensagem": "Peça excluída com sucesso."
        }), 200

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao excluir peça.",
            "erro": str(erro)
        }), 500