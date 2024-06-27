from .extensions import dictConfig
from flask import Flask


def create_app(config_filename="develop.cfg"):

    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    from .extensions import db, login_manager, bcrypt

    db.init_app(app)

    bcrypt.init_app(app)

    from .views import views
    from .auth import auth

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    from .models import User

    login_manager.init_app(app)

    @login_manager.user_loader
    def load_user(id):
        return User.query.get(int(id))

    if config_filename == "develop.cfg":
        with app.app_context():
            db.create_all()

    return app
