from flask import Blueprint, render_template

home_route = Blueprint('home', __name__, template_folder='templates')

@home_route.route("/", methods=["POST","GET"])
def home():
    return render_template("index.html")