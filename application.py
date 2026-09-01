from flask import Flask, render_template, request, redirect, url_for
from extensions import db, login_manager
from flask_login import login_required, login_user
from models import User
import auth

application = Flask(__name__)
application.config['SECRET_KEY'] = "MINHA_CHAVE_140198"
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
db.init_app(application)
login_manager.init_app(application)

@application.route("/", methods=["POST","GET"])
def home():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username and password:
            user = User.query.filter_by(username=username, password=password).first()
            if user:
                login_user(user)
            
            return redirect(url_for('dashboard'))
        
    return render_template("index.html")

@application.route("/register", methods=["POST","GET"])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username and password:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            
            return redirect(url_for('dashboard'))

    return render_template("register.html")

@application.route("/dashboard", methods=["POST","GET"])
@login_required
def dashboard():
    return render_template("dashboard.html")

with application.app_context():
    db.create_all()

if __name__ == "__main__":
    application.run(debug=True)