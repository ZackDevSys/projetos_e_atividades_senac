from flask import jsonify, request

from services.servico_service import (
    buscar_servicos,
    buscar_servico,
    cadastrar_servico,
    atualizar_servico,
    excluir_servico
)

def listar():

    try:
        servicos = buscar_servicos()

        return jsonify({
            "sucesso": True,
            "quantidade": len(servicos),
            "dados": servicos
        }), 200

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao buscar serviços.",
            "erro": str(erro)
        }), 500

def buscar_por_id(id):

    try:
        servico = buscar_servico(id)

        if servico is None:
            return jsonify({
                "sucesso": False,
                "mensagem": "Serviço não encontrado."
            }), 404

        return jsonify({
            "sucesso": True,
            "dados": servico
        }), 200

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao buscar serviço.",
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

        id_servico = cadastrar_servico(dados)

        return jsonify({
            "sucesso": True,
            "mensagem": "Serviço cadastrado com sucesso.",
            "id": id_servico
        }), 201

    except ValueError as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": str(erro)
        }), 400

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao cadastrar serviço.",
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

        resultado = atualizar_servico(id, dados)

        if resultado == 0:
            return jsonify({
                "sucesso": False,
                "mensagem": "Serviço não encontrado."
            }), 404

        return jsonify({
            "sucesso": True,
            "mensagem": "Serviço atualizado com sucesso."
        }), 200

    except ValueError as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": str(erro)
        }), 400

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao atualizar serviço.",
            "erro": str(erro)
        }), 500

def excluir(id):

    try:
        resultado = excluir_servico(id)

        if resultado == 0:
            return jsonify({
                "sucesso": False,
                "mensagem": "Serviço não encontrado."
            }), 404

        return jsonify({
            "sucesso": True,
            "mensagem": "Serviço excluído com sucesso."
        }), 200

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao excluir serviço.",
            "erro": str(erro)
        }), 500