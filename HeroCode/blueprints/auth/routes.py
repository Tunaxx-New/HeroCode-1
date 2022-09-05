from sqlalchemy.exc import IntegrityError
from flask import request
import re

from HeroCode.blueprints.auth import auth
from HeroCode.models import Users
from HeroCode import db


@auth.route('/register', methods=['POST'])
def main():
    username = request.form.get('username', None)
    email = request.form.get('email', None)
    password = request.form.get('password', None)

    if None in [username, email, password]:
        return dict(status=False, reason='Not all data was given')

    user = Users(username=username, email=email, password=password)

    db.session.add(user)

    try:
        db.session.commit()
    except IntegrityError as e:
        try:
            # https://stackoverflow.com/questions/4666973/how-to-extract-the-substring-between-two-markers
            duplicate_key = re.search('\'users.(.+?)\'"', e.args[0]).group(1)
        except AttributeError:
            return dict(status=False, reason='Unexpected error with duplicate key')

        return dict(status=False, reason=f'Duplicate key - {duplicate_key}')

    return dict(status=True)
