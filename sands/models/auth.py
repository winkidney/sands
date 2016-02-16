from flask.ext.login import UserMixin
from peewee import (
    CharField,
    DateTimeField,
)

from sands.models import BaseModel


class User(BaseModel, UserMixin):
    name = CharField(index=True)
    email = CharField()
    create_at = DateTimeField()