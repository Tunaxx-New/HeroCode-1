from flask import Blueprint

auth = Blueprint('auth', __name__)

from HeroCode.blueprints.auth import routes
