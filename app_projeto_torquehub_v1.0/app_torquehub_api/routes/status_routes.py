from flask import Blueprint, jsonify


status_routes = Blueprint(
    "status_routes",
    __name__,
    url_prefix="/api"
)


@status_routes.route("/status", methods=["GET"])
def status():
    return jsonify({
        "sucesso": True,
        "sistema": "TorqueHub API",
        "versao": "1.0.0",
        "status": "online"
    }), 200