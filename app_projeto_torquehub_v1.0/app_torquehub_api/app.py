from flask import Flask
from flask_cors import CORS

from routes.status_routes import status_routes
from routes.usuario_routes import usuario_routes


app = Flask(__name__)

CORS(app)

app.register_blueprint(status_routes)
app.register_blueprint(usuario_routes)


@app.route("/")
def inicio():
    return {
        "sistema": "TorqueHub API",
        "mensagem": "API funcionando"
    }


if __name__ == "__main__":
    app.run(
        host="0.0.0.0",
        port=5000,
        debug=True
    )