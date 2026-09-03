from flask import Flask, render_template, request, redirect, url_for
from extensions import db, login_manager
from flask_login import login_required, login_user, current_user, logout_user
from models import User, Tasks
import auth

application = Flask(__name__)
application.config['SECRET_KEY'] = "MINHA_CHAVE_140198"
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
db.init_app(application)
login_manager.init_app(application)

@application.route("/", methods=["POST","GET"])
def home():
    if current_user.is_authenticated:
        return redirect(url_for('dashboard'))
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
    todo_tasks, progress_tasks, complete_tasks= [], [], []
    all_tasks = current_user.tasks

    if all_tasks:
        for task in all_tasks:
            match task.status:
                case "todo":
                    todo_tasks.append(task)
                case "progress":
                    progress_tasks.append(task)
                case "complete":
                    complete_tasks.append(task)

    return render_template("dashboard.html", todo_tasks=todo_tasks, progress_tasks=progress_tasks, complete_tasks=complete_tasks, username=current_user.username)

@application.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('home'))

@application.route("/dashboard/task_add", methods=["POST","GET"])
@login_required
def add_task():
    if request.method == 'POST':
        status_task = request.form['status']
        description_task = request.form['description']

        if status_task and description_task:
            task = Tasks(user_id=current_user.id, status=status_task, description=description_task)
            db.session.add(task)
            db.session.commit()
            return redirect(url_for('dashboard'))

    return render_template("task/add_task.html")

@application.route("/dashboard/task_delete/<int:task_id>", methods=["POST","GET"])
@login_required
def delete_task(task_id):
    task = db.session.query(Tasks).filter_by(id=task_id).first()
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('dashboard'))

with application.app_context():
    db.create_all()

if __name__ == "__main__":
    application.run(debug=True)