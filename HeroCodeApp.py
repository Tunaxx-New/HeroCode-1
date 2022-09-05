from os import getenv

from HeroCode import create_app


def main():
    host = getenv('host')
    port = getenv('port')
    debug = getenv('debug') == '1'

    if None in [host, port, debug]:
        raise Exception('Host, port or debug values not given')

    app = create_app()

    app.run(host=host, port=port, debug=debug)


if __name__ == '__main__':
    main()
