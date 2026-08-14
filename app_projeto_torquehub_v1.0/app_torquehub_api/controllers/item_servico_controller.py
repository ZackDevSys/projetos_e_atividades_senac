from flask import jsonify, request

from services.item_servico_service import (
    listar_itens,
    buscar_item,
    cadastrar_item,
    atualizar_item,
    excluir_item
)

def listar(ordem_servico_id):

    try:
        itens = listar_itens(ordem_servico_id)

        return jsonify({
            "sucesso": True,
            "quantidade": len(itens),
            "dados": itens
        }), 200

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao buscar itens da ordem de serviço.",
            "erro": str(erro)
        }), 500

def buscar_por_id(id):

    try:
        item = buscar_item(id)

        if not item:
            return jsonify({
                "sucesso": False,
                "mensagem": "Item de serviço não encontrado."
            }), 404

        return jsonify({
            "sucesso": True,
            "dados": item
        }), 200

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao buscar item de serviço.",
            "erro": str(erro)
        }), 500

def criar(ordem_servico_id):

    try:
        dados = request.get_json()

        if not dados:
            return jsonify({
                "sucesso": False,
                "mensagem": "Nenhum dado foi enviado."
            }), 400

        id_item = cadastrar_item(
            ordem_servico_id,
            dados
        )

        return jsonify({
            "sucesso": True,
            "mensagem": "Item de serviço adicionado com sucesso.",
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
            "mensagem": "Erro ao adicionar item de serviço.",
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

        resultado = atualizar_item(id, dados)

        if resultado == 0:
            return jsonify({
                "sucesso": False,
                "mensagem": "Item de serviço não encontrado."
            }), 404

        return jsonify({
            "sucesso": True,
            "mensagem": "Item de serviço atualizado com sucesso."
        }), 200

    except ValueError as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": str(erro)
        }), 400

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao atualizar item de serviço.",
            "erro": str(erro)
        }), 500

def excluir(id):

    try:
        resultado = excluir_item(id)

        if resultado == 0:
            return jsonify({
                "sucesso": False,
                "mensagem": "Item de serviço não encontrado."
            }), 404

        return jsonify({
            "sucesso": True,
            "mensagem": "Item de serviço excluído com sucesso."
        }), 200

    except ValueError as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": str(erro)
        }), 400

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao excluir item de serviço.",
            "erro": str(erro)
        }), 500