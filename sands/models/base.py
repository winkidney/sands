from peewee import (
    Model,
)

from sands.database import db


class BaseModel(Model):
    class Meta:
        database = db
