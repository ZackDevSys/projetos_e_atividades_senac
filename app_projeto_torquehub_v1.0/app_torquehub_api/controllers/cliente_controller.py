from flask import jsonify, request

from services.cliente_service import (
    buscar_clientes,
    buscar_cliente,
    cadastrar_cliente,
    atualizar_cliente,
    excluir_cliente
)

def listar():
    try:
        clientes = buscar_clientes()

        return jsonify({
            "sucesso": True,
            "quantidade": len(clientes),
            "dados": clientes
        }), 200

    except Exception as erro:
        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao buscar clientes.",
            "erro": str(erro)
        }), 500

def buscar_por_id(id):
    try:
        cliente = buscar_cliente(id)

        if cliente is None:
            return jsonify({
                "sucesso": False,
                "mensagem": "Cliente não encontrado."
            }), 404

        return jsonify({
            "sucesso": True,
            "dados": cliente
        }), 200

    except Exception as erro:
        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao buscar cliente.",
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

        id_cliente = cadastrar_cliente(dados)

        return jsonify({
            "sucesso": True,
            "mensagem": "Cliente cadastrado com sucesso.",
            "id": id_cliente
        }), 201

    except ValueError as erro:
        return jsonify({
            "sucesso": False,
            "mensagem": str(erro)
        }), 400

    except Exception as erro:
        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao cadastrar cliente.",
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

        resultado = atualizar_cliente(id, dados)

        if resultado == 0:
            return jsonify({
                "sucesso": False,
                "mensagem": "Cliente não encontrado."
            }), 404

        return jsonify({
            "sucesso": True,
            "mensagem": "Cliente atualizado com sucesso."
        }), 200

    except ValueError as erro:
        return jsonify({
            "sucesso": False,
            "mensagem": str(erro)
        }), 400

    except Exception as erro:
        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao atualizar cliente.",
            "erro": str(erro)
        }), 500

def excluir(id):
    try:
        resultado = excluir_cliente(id)

        if resultado == 0:
            return jsonify({
                "sucesso": False,
                "mensagem": "Cliente não encontrado."
            }), 404

        return jsonify({
            "sucesso": True,
            "mensagem": "Cliente excluído com sucesso."
        }), 200

    except Exception as erro:
        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao excluir cliente.",
            "erro": str(erro)
        }), 500