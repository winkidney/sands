from flask.ext.login import UserMixin
from peewee import (
    Model,
    CharField,
    DateTimeField,
)

from sands.database import db


class User(Model, UserMixin):

    name = CharField(index=True)
    email = CharField()
    create_at = DateTimeField()

    class Meta:
        db = db