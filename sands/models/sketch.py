from peewee import (
    CharField,
    ForeignKeyField,

    fn)

from sands.models import BaseModel


class Word(BaseModel):
    name = CharField(index=True, unique=True)

    @classmethod
    def random_by_type(cls, type_name):
        type_id = Type.select(Type.id).where(
            Type.name == type_name
        )
        word_id = WordType.select(WordType.id).where(
            WordType.type == type_id
        ).order_by(fn.Random())
        return cls.select().where(
            cls.id == word_id
        ).get()


class Tag(BaseModel):
    name = CharField(index=True, unique=True)


class Type(BaseModel):
    name = CharField(index=True, unique=True)


class WordType(BaseModel):
    word = ForeignKeyField(Word)
    type = ForeignKeyField(Type)


class WordTag(BaseModel):
    word = ForeignKeyField(Word)
    tag = ForeignKeyField(Tag)