import os

from peewee import SqliteDatabase

from sands.settings import PROJECT_ROOT


db_file = os.path.join(PROJECT_ROOT, "sands.sqlite3")

db = SqliteDatabase(
    db_file
)
