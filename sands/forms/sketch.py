from flask_wtf import Form
from wtforms import BooleanField

from sands.forms.share import QueryMixin


class SketchForm(Form, QueryMixin):
    when = BooleanField()
    where = BooleanField()
    who = BooleanField()
    what = BooleanField()
    how = BooleanField()