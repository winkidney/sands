from flask_wtf import Form
from wtforms import BooleanField

from sands.forms.share import QueryMixin
from sands.models.data import types_map


class SketchForm(Form, QueryMixin):
    pass

for name, value in types_map.iteritems():
    setattr(
        SketchForm, name, BooleanField(value['label'])
    )