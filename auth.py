from extensions import login_manager, db
from models import User

@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User,user_id)

login_manager.login_view="home.home"