import click

from sands.app import app


def register_views():
    import sands.views


@click.group("manage")
def entry():
    pass


@entry.command(
    help="run development server"
)
def run(host="0.0.0.0", port=8888):
    register_views()
    app.run(host, port, debug=True)


@entry.command(
    help="create database tables"
)
def create_db():
    from sands.database import db
    from sands.models.auth import User

    db.connect()
    db.create_table(User)


if __name__ == "__main__":
    entry()