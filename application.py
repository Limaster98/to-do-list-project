from flask import Flask
from extensions import db, login_manager
from routes.home import home_route
from routes.user import user_route
from routes.dashboard import dashboard_routes
import auth

application = Flask(__name__)
application.config['SECRET_KEY'] = "MINHA_CHAVE_140198"
application.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'
db.init_app(application)
login_manager.init_app(application)

application.register_blueprint(home_route)
application.register_blueprint(user_route, url_prefix='/user')
application.register_blueprint(dashboard_routes, url_prefix='/dashboard')

with application.app_context():
    db.create_all()

if __name__ == "__main__":
    application.run(debug=True)