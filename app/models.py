from app import db, UserMixin
from datetime import datetime

class User(db.Model, UserMixin):
    __tablename__ = 'users'
    def __init__(self, username, email, password, user_agent):
        self.username = username
        self.email = email
        self.password = password
        self.user_agent = user_agent

    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    email = db.Column(db.String(100), nullable=False, unique=True)
    password = db.Column(db.String(100), nullable=False)
    user_agent = db.Column(db.String(100), nullable=False)
    create_at = db.Column(db.DateTime, default=datetime.now)
    is_active = db.Column(db.Boolean(), default = True)

    def is_active(self):
        return self.is_active

    def is_anonymous(self):
        return False
    
    def is_authenticated(self):
        return True
    