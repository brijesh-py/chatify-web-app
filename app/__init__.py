from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask_bcrypt import Bcrypt
from flask_caching import Cache
from flask_socketio import SocketIO, emit, close_room, join_room, leave_room, rooms
from flask_login import (
    LoginManager,
    current_user,
    login_manager,
    login_user,
    logout_user,
    UserMixin,
    login_required,
)

app = Flask(__name__)
app.secret_key = "secret_key"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db.sqlite"

db = SQLAlchemy(app)
migrate = Migrate(app, db)
socketio = SocketIO(app)
login = LoginManager(app)
login.login_view = "auth.login_view"
cache = Cache(app)
bcrypt = Bcrypt(app)

# @login_required
@socketio.on('join')
def join(data):
    room = data["room"]
    emit("message", {"username": current_user.username}, room=room)


def load_app():
    from .routes import bp
    from .auth.routes import bp_auth

    app.register_blueprint(bp)
    app.register_blueprint(bp_auth, url_prefix="/auth")
