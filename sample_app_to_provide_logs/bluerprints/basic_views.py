from flask import Blueprint


front_page = Blueprint("front_page", __name__, url_prefix="")


@front_page.route("/")
def hello_world():
    return {"hello": "world"}
