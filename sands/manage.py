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
    from sands.models.sketch import (
        Word,
        Type,
        WordType,
        Tag,
        WordTag,
    )
    tables = [
        User,
        Word,
        Type,
        WordType,
        Tag,
        WordTag,
    ]
    db.create_tables(tables)


@entry.command(
    help="create init tags and type"
)
def init_data():
    from sands.models.sketch import (
        Type,
    )
    from sands.database import db
    from sands.models import _data as data

    data_source = [
        {"key": key, "name": name}
        for key, name in data.types.iteritems()
    ]

    with db.atomic():
        Type.insert_many(data_source).execute()


if __name__ == "__main__":
    entry()