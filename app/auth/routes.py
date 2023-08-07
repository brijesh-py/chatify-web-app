# The code is importing the `Blueprint` class from the Flask module and the `auth_view` module from
# the current package.
from flask import Blueprint
from .views import auth_view


# The line `bp_auth = Blueprint('auth', __name__, template_folder='templates',
# static_folder='static')` is creating a Flask blueprint named `bp_auth`.
bp_auth = Blueprint('auth', __name__, template_folder='templates', static_folder='static')

# The code is adding URL rules to the `bp_auth` blueprint.
bp_auth.add_url_rule('/join/', view_func=auth_view.join_view, methods=['GET', 'POST'])
bp_auth.add_url_rule('/login/', view_func=auth_view.login_view, methods=['GET', 'POST'])
bp_auth.add_url_rule('/logout/', view_func=auth_view.logout_view, methods=['GET'])