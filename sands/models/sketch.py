from peewee import (
    CharField,
    ForeignKeyField,

)

from sands.models import BaseModel


class Word(BaseModel):
    content = CharField()


class Tag(BaseModel):
    key = CharField()
    name = CharField()


class Type(BaseModel):
    key = CharField()
    name = CharField()


class WordType(BaseModel):
    name = CharField()


class WordTag(BaseModel):
    word = ForeignKeyField(Word)
    tag = ForeignKeyField(Tag)