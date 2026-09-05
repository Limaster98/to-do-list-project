from flask import render_template, request, redirect, url_for, Blueprint
from extensions import db
from flask_login import login_required, current_user
from models import Tasks

dashboard_routes = Blueprint('dashboard', __name__, template_folder='templates')

@dashboard_routes.route("/", methods=["POST","GET"])
@login_required
def home():
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

@dashboard_routes.route("/task_add", methods=["POST","GET"])
@login_required
def add_task():
    if request.method == 'POST':
        status_task = request.form['status']
        description_task = request.form['description']

        if status_task and description_task:
            task = Tasks(user_id=current_user.id, status=status_task, description=description_task)
            db.session.add(task)
            db.session.commit()
            return redirect(url_for('dashboard.home'))

    return render_template("add_task.html")

@dashboard_routes.route("/task_delete/<int:task_id>", methods=["POST","GET"])
@login_required
def delete_task(task_id):
    task = db.session.query(Tasks).filter_by(id=task_id).first()
    if task:
        db.session.delete(task)
        db.session.commit()
    return redirect(url_for('dashboard.home'))