from flask import jsonify, request
from auth.auth_service import autenticar_usuario

def login():
    try:
        dados = request.get_json(silent=True)

        if not dados:
            return jsonify({
                "sucesso": False,
                "mensagem": "Nenhum dado foi enviado."
            }), 400

        email = dados.get("email")
        senha = dados.get("senha")

        usuario = autenticar_usuario(email, senha)

        return jsonify({
            "sucesso": True,
            "mensagem": "Login realizado com sucesso.",
            "dados": usuario
        }), 200

    except ValueError as erro:
        return jsonify({
            "sucesso": False,
            "mensagem": str(erro)
        }), 400

    except PermissionError as erro:

        mensagem = str(erro)

        if mensagem == "Usuário inativo. Acesso não permitido.":
            status_code = 403
        else:
            status_code = 401

        return jsonify({
            "sucesso": False,
            "mensagem": mensagem
        }), status_code

    except Exception as erro:
        return jsonify({
            "sucesso": False,
            "mensagem": "Erro ao realizar login.",
            "erro": str(erro)
        }), 500