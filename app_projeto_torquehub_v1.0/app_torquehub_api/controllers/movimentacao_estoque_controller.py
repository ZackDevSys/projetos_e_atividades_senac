from flask import jsonify, request

from services.movimentacao_estoque_service import (
    buscar_movimentacoes,
    buscar_movimentacao,
    cadastrar_movimentacao,
    atualizar_movimentacao_service,
    excluir_movimentacao_service
)

def listar():

    try:

        movimentacoes = buscar_movimentacoes()

        return jsonify({
            "sucesso": True,
            "quantidade": len(movimentacoes),
            "dados": movimentacoes
        }), 200

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao buscar movimentações de estoque.",
            "erro": str(erro)
        }), 500

def buscar_por_id(id):

    try:

        movimentacao = buscar_movimentacao(id)

        if movimentacao is None:

            return jsonify({
                "sucesso": False,
                "mensagem": "Movimentação não encontrada."
            }), 404

        return jsonify({
            "sucesso": True,
            "dados": movimentacao
        }), 200

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao buscar movimentação.",
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

        id_movimentacao = cadastrar_movimentacao(dados)

        return jsonify({
            "sucesso": True,
            "mensagem": "Movimentação registrada com sucesso.",
            "id": id_movimentacao
        }), 201

    except ValueError as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": str(erro)
        }), 400

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao registrar movimentação.",
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

        resultado = atualizar_movimentacao_service(
            id,
            dados
        )

        if resultado == 0:

            return jsonify({
                "sucesso": False,
                "mensagem": "Movimentação não encontrada."
            }), 404

        return jsonify({
            "sucesso": True,
            "mensagem": "Movimentação atualizada com sucesso."
        }), 200

    except ValueError as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": str(erro)
        }), 400

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao atualizar movimentação.",
            "erro": str(erro)
        }), 500

def excluir(id):

    try:

        resultado = excluir_movimentacao_service(id)

        if resultado == 0:

            return jsonify({
                "sucesso": False,
                "mensagem": "Movimentação não encontrada."
            }), 404

        return jsonify({
            "sucesso": True,
            "mensagem": "Movimentação excluída com sucesso."
        }), 200

    except ValueError as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": str(erro)
        }), 400

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao excluir movimentação.",
            "erro": str(erro)
        }), 500