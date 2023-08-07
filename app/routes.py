from flask import Blueprint
from .views import index

bp = Blueprint("app", __name__, template_folder="templates", static_folder="static")

bp.add_url_rule("/", view_func=index, methods=["GET"])
