from flask import Flask, render_template
from extensions import db, login_manager
from flask_login import login_required
import auth

application = Flask(__name__)
application.config['SECRET_KEY'] = "MINHA_CHAVE_140198"
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
db.init_app(application)
login_manager.init_app(application)

@application.route("/", methods=["POST","GET"])
def home():
    return render_template("index.html")

@application.route("/register", methods=["POST","GET"])
def register():
    return render_template("register.html")

@application.route("/dashboard", methods=["POST","GET"])
@login_required
def dashboard():
    return render_template("dashboard.html")

with application.app_context():
    db.create_all()

if __name__ == "__main__":
    application.run(debug=True)