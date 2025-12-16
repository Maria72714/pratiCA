from flask import Flask
from flask import render_template
from sqlalchemy.orm import Session
from models import engine, Usuarios
from flask_login import LoginManager
from controllers import auth, user, horario


app = Flask(__name__)
app.config['SECRET_KEY'] = 'senha_super_secreta1234567'

app.register_blueprint(user.usuarios_bp)
app.register_blueprint(auth.auth_bp)
app.register_blueprint(horario.horarios_bp)

login_manager = LoginManager(app)
login_manager.login_view = 'auth.login'


@login_manager.user_loader
def load_user(user_id):
    with Session(bind=engine) as session:
        return session.get(Usuarios, int(user_id))

@app.errorhandler(404)
def erro_404(teste):
    return render_template("erro_base.html", erro = 404, mensagem = "Página não encontrada.")

@app.errorhandler(500)
def erro_500(teste):
    return render_template("erro_base.html", erro = 500, mensagem = "Erro interno do servidor.")