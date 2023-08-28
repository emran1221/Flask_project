# -*- encoding: utf-8 -*-
"""
Copyright (c) 2019 - present AppSeed.us
"""
from apps import db, create_app
from apps.views import views as views_blueprint
from flask_login import LoginManager
from apps.models import Coach, Player, Exercise, WorkoutRoutine
from apps.accounts import accounts
import warnings
from sqlalchemy.exc import SAWarning
app = create_app()

warnings.filterwarnings('ignore', category=SAWarning, message='.*relationship .* will copy column .*')


app.register_blueprint(accounts, url_prefix='/accounts')  # Register the blueprint with a URL prefix
app.register_blueprint(views_blueprint)

login_manager = LoginManager(app)
login_manager.login_view = 'accounts.accounts_auth_signin'


@login_manager.user_loader
def load_user(user_id):
    return Coach.query.get(int(user_id)) or Player.query.get(int(user_id))


if __name__ == "__main__":
    with app.app_context():
        db.create_all()
        app.run(host='0.0.0.0', port=5000)

