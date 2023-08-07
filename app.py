from app import app, db, login, load_app, socketio
from app.models import User
from app.chats import *

if __name__ == "__main__":
    load_app()
    with app.app_context():
        db.create_all()

    @login.user_loader
    def load_user(id):
        return User.query.get(int(id))

    # app.run(debug=True, host='0.0.0.0')
    socketio.run(app, debug=True, host='0.0.0.0')
