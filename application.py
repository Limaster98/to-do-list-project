from flask import Flask, render_template

application = Flask(__name__)

@application.route("/", methods=["POST","GET"])
def home():
    return render_template("index.html")

@application.route("/register", methods=["POST","GET"])
def register():
    return render_template("register.html")

@application.route("/dashboard", methods=["POST","GET"])
def dashboard():
    return render_template("dashboard.html")

if __name__ == "__main__":
    application.run(debug=True)