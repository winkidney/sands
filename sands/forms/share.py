# coding: utf-8
from sands.models._data import types_map


class QueryMixin(object):
    def get_true_field(self):
        return tuple(
            types_map.get(field.name) for field in self
            if field.name != "csrf_token" and field.data
        )
