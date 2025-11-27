from flask import Flask, render_template, url_for, request, redirect,get_flashed_messages, flash
from sqlalchemy.orm import Session
from models import engine, Usuario
from flask_login import LoginManager
from controllers.usuarios import usuarios_bp
from controllers.auth import auth_bp


app = Flask(__name__)
app.config['SECRET_KEY'] = 'senha_super_secreta1234567'

app.register_blueprint(usuarios_bp)
app.register_blueprint(auth_bp)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    with Session(bind=engine) as session:
        return session.get(Usuario, int(user_id))

