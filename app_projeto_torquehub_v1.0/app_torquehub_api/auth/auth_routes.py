from flask import Blueprint
from auth.auth_controller import login

auth_routes = Blueprint(
    "auth_routes",
    __name__,
    url_prefix="/api"
)

@auth_routes.route("/login", methods=["POST"])
def post_login():
    return login()