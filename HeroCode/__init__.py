from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate
from flask import Flask

from config import Config


db = SQLAlchemy()
migrate = Migrate()


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    with app.app_context():
        db.init_app(app)
        migrate.init_app(app, db)

    from HeroCode.blueprints import auth
    app.register_blueprint(auth, url_prefix='/auth')

    return app
