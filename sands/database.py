import os

from peewee import SqliteDatabase

from sands.settings import PROJECT_ROOT

db = SqliteDatabase(
    os.path.join(PROJECT_ROOT, "sands.sqlite3")
)
