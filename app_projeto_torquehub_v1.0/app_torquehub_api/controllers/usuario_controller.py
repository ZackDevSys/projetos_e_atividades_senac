from flask import jsonify, request

from services.usuario_service import (
    buscar_usuarios,
    buscar_usuario,
    cadastrar_usuario,
    atualizar_usuario,
    excluir_usuario
)

def listar():
    try:
        usuarios = buscar_usuarios()

        return jsonify({
            "sucesso": True,
            "quantidade": len(usuarios),
            "dados": usuarios
        }), 200

    except Exception as erro:
        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao buscar usuários.",
            "erro": str(erro)
        }), 500

def buscar_por_id(id):
    try:
        usuario = buscar_usuario(id)

        if usuario is None:
            return jsonify({
                "sucesso": False,
                "mensagem": "Usuário não encontrado."
            }), 404

        return jsonify({
            "sucesso": True,
            "dados": usuario
        }), 200

    except Exception as erro:
        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao buscar usuário.",
            "erro": str(erro)
        }), 500

def criar():
    try:
        dados = request.get_json(silent=True)

        if not dados:
            return jsonify({
                "sucesso": False,
                "mensagem": "Nenhum dado foi enviado."
            }), 400

        id_usuario = cadastrar_usuario(dados)

        return jsonify({
            "sucesso": True,
            "mensagem": "Usuário cadastrado com sucesso.",
            "id": id_usuario
        }), 201

    except ValueError as erro:
        return jsonify({
            "sucesso": False,
            "mensagem": str(erro)
        }), 400

    except Exception as erro:
        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao cadastrar usuário.",
            "erro": str(erro)
        }), 500

def atualizar(id):
    try:
        dados = request.get_json(silent=True)

        if not dados:
            return jsonify({
                "sucesso": False,
                "mensagem": "Nenhum dado foi enviado."
            }), 400

        resultado = atualizar_usuario(id, dados)

        if resultado == 0:
            return jsonify({
                "sucesso": False,
                "mensagem": "Usuário não encontrado."
            }), 404

        return jsonify({
            "sucesso": True,
            "mensagem": "Usuário atualizado com sucesso."
        }), 200

    except ValueError as erro:
        return jsonify({
            "sucesso": False,
            "mensagem": str(erro)
        }), 400

    except Exception as erro:
        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao atualizar usuário.",
            "erro": str(erro)
        }), 500

def excluir(id):
    try:
        resultado = excluir_usuario(id)

        if resultado == 0:
            return jsonify({
                "sucesso": False,
                "mensagem": "Usuário não encontrado."
            }), 404

        return jsonify({
            "sucesso": True,
            "mensagem": "Usuário excluído com sucesso."
        }), 200

    except Exception as erro:
        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao excluir usuário.",
            "erro": str(erro)
        }), 500