from flask import render_template, request, redirect, url_for, Blueprint
from extensions import db
from flask_login import login_user, current_user, logout_user, login_required
from models import User

user_route = Blueprint('user', __name__, template_folder='templates')

@user_route.route("/login", methods=["POST","GET"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard.home'))
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username and password:
            user = User.query.filter_by(username=username, password=password).first()
            if user:
                login_user(user)
                return redirect(url_for('dashboard.home'))
            else:
                return render_template("login.html"), 401
        
    return render_template("login.html")

@user_route.route("/register", methods=["POST","GET"])
def register():
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']

        if username and password:
            new_user = User(username=username, password=password)
            db.session.add(new_user)
            db.session.commit()
            
            return redirect(url_for('dashboard.home'))

    return render_template("register.html")

@user_route.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home.home'))