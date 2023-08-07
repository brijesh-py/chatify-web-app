from flask import render_template, request, redirect, url_for, flash
from .forms import JoinForm, LoginForm
from app import current_user, login_user, logout_user, db, bcrypt, login_required
from ..models import User

def check_user_if_logged_in(func):
    def wrapper(*args, **kwargs):
        if current_user.is_authenticated:
            return redirect(url_for('app.index'))
        else:
            return func(*args, **kwargs)
    wrapper.__name__ = func.__name__
    return wrapper

class AuthViews:
    @check_user_if_logged_in
    def join_view(self):
        form = JoinForm()
        if request.method == 'POST' and form.validate():
            username = form.username.data.strip()
            email = form.email.data.strip()
            password = form.password.data.strip()
            user_agent = request.headers.get('User-Agent')
            check_email = User.query.filter_by(email=email).first()
            check_user = User.query.filter_by(username=username).first()
            if check_email or check_user:
                flash(['Email or Username already exists', 'danger'])
                return render_template('join.html', form = form)
            else:
                user = User(username, email, bcrypt.generate_password_hash(password), user_agent)
                db.session.add(user)
                db.session.commit()
                login_user(user)
                return redirect(url_for('app.index'))
        return render_template('join.html', form = form)
    
    @check_user_if_logged_in
    def login_view(self):
        form = LoginForm()
        if request.method == 'POST' and form.validate():
            email = form.email.data.strip()
            password = form.password.data.strip()
            user = User.query.filter_by(email=email).first()
            if user and bcrypt.check_password_hash(user.password, password):
                login_user(user)
                return redirect(url_for('app.index'))
            else:
                flash(['Invalid email or password', 'danger'])
                return render_template('login.html', form = form)
        return render_template('login.html', form = form)
    
    @login_required
    def logout_view(self):
        logout_user()
        return redirect(url_for('auth.login_view'))
    

auth_view = AuthViews()