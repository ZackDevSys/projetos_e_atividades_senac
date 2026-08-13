from flask import Flask
from flask_cors import CORS

from routes.status_routes import status_routes
from routes.usuario_routes import usuario_routes
from routes.cliente_routes import cliente_routes
from routes.veiculo_routes import veiculo_routes
from routes.servico_routes import servico_routes
from routes.ordem_servico_routes import ordem_servico_routes
from routes.item_servico_routes import item_servico_routes
from routes.ordem_servico_usuario_routes import ordem_servico_usuario_routes

app = Flask(__name__)

CORS(app)

app.register_blueprint(status_routes)
app.register_blueprint(usuario_routes)
app.register_blueprint(cliente_routes)
app.register_blueprint(veiculo_routes)
app.register_blueprint(servico_routes)
app.register_blueprint(ordem_servico_routes)
app.register_blueprint(item_servico_routes)
app.register_blueprint(ordem_servico_usuario_routes)

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