from flask import jsonify, request

from services.veiculo_service import (
    buscar_veiculos,
    buscar_veiculo,
    cadastrar_veiculo,
    atualizar_veiculo,
    excluir_veiculo
)

def listar():

    try:
        veiculos = buscar_veiculos()

        return jsonify({
            "sucesso": True,
            "quantidade": len(veiculos),
            "dados": veiculos
        }), 200

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao buscar veículos.",
            "erro": str(erro)
        }), 500

def buscar_por_id(id):

    try:
        veiculo = buscar_veiculo(id)

        if veiculo is None:

            return jsonify({
                "sucesso": False,
                "mensagem": "Veículo não encontrado."
            }), 404

        return jsonify({
            "sucesso": True,
            "dados": veiculo
        }), 200

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao buscar veículo.",
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

        id_veiculo = cadastrar_veiculo(dados)

        return jsonify({
            "sucesso": True,
            "mensagem": "Veículo cadastrado com sucesso.",
            "id": id_veiculo
        }), 201

    except ValueError as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": str(erro)
        }), 400

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao cadastrar veículo.",
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

        resultado = atualizar_veiculo(id, dados)

        if resultado == 0:

            return jsonify({
                "sucesso": False,
                "mensagem": "Veículo não encontrado."
            }), 404

        return jsonify({
            "sucesso": True,
            "mensagem": "Veículo atualizado com sucesso."
        }), 200

    except ValueError as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": str(erro)
        }), 400

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao atualizar veículo.",
            "erro": str(erro)
        }), 500

def excluir(id):

    try:

        resultado = excluir_veiculo(id)

        if resultado == 0:

            return jsonify({
                "sucesso": False,
                "mensagem": "Veículo não encontrado."
            }), 404

        return jsonify({
            "sucesso": True,
            "mensagem": "Veículo excluído com sucesso."
        }), 200

    except Exception as erro:

        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao excluir veículo.",
            "erro": str(erro)
        }), 500