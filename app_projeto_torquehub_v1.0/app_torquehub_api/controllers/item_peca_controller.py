from flask import jsonify, request

from services.item_peca_service import (
    buscar_itens_pecas,
    buscar_item_peca,
    cadastrar_item_peca,
    atualizar_item_peca_service,
    excluir_item_peca_service
)

def listar():

    try:

        itens = buscar_itens_pecas()

        return jsonify({
            "sucesso": True,
            "quantidade": len(itens),
            "dados": itens
        }), 200

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao buscar itens de peças.",
            "erro": str(erro)
        }), 500

def buscar_por_id(id):

    try:

        item = buscar_item_peca(id)

        if item is None:

            return jsonify({
                "sucesso": False,
                "mensagem": "Item de peça não encontrado."
            }), 404

        return jsonify({
            "sucesso": True,
            "dados": item
        }), 200

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao buscar item de peça.",
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

        id_item = cadastrar_item_peca(dados)

        return jsonify({
            "sucesso": True,
            "mensagem": "Item de peça criado com sucesso.",
            "id": id_item
        }), 201

    except ValueError as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": str(erro)
        }), 400

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao criar item de peça.",
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

        resultado = atualizar_item_peca_service(
            id,
            dados
        )

        if resultado == 0:

            return jsonify({
                "sucesso": False,
                "mensagem": "Item de peça não encontrado."
            }), 404

        return jsonify({
            "sucesso": True,
            "mensagem": "Item de peça atualizado com sucesso."
        }), 200

    except ValueError as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": str(erro)
        }), 400

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao atualizar item de peça.",
            "erro": str(erro)
        }), 500

def excluir(id):

    try:

        resultado = excluir_item_peca_service(id)

        if resultado == 0:

            return jsonify({
                "sucesso": False,
                "mensagem": "Item de peça não encontrado."
            }), 404

        return jsonify({
            "sucesso": True,
            "mensagem": "Item de peça excluído com sucesso."
        }), 200

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao excluir item de peça.",
            "erro": str(erro)
        }), 500