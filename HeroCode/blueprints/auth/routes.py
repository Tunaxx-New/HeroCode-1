from HeroCode.blueprints.auth import auth


@auth.route('/')
def main():
    return '<h1>yo</h1>'
