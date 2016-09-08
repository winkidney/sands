import os
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
        Word,
        WordType,
    )
    from sands.database import db
    from sands.models import data

    types = [
        {"name": t['name']}
        for t in data.types_map.values()
    ]

    words = []
    for names in data.init_words.itervalues():
        for name in names:
            words.append({"name": name})

    # Type and Word Base
    with db.atomic():
        Type.insert_many(types).execute()
        Word.insert_many(words).execute()

    # Words ForeignKey
    with db.atomic():
        rows = []
        for type_name, words in data.init_words.iteritems():
            type_instance = Type.get(name=type_name)
            for word in words:
                rows.append(
                    dict(
                        type=type_instance,
                        word=Word.get(name=word)
                    )
                )
        WordType.insert_many(rows).execute()


if __name__ == "__main__":
    entry()