#!/usr/bin/python
# -*- coding: utf-8 -*-
# req_log/fields.py
""" Request log fields """

from django.conf import settings
from django.db import models

if getattr(settings, 'USE_CPICKLE', False):
    import cPickle as pickle
else:
    import pickle


class PickleField(models.TextField):
    __metaclass__ = models.SubfieldBase

    editable = False
    serialize = False

    def get_db_prep_value(self, value):
        return pickle.dumps(value)

    def to_python(self, value):
        if not isinstance(value, basestring):
            return value

        # Tries to convert unicode objects to string, cause loads pickle from
        # unicode excepts ugly ``KeyError: '\x00'``.
        #
        # If not possible, this value is returned, cause it's not pickled yet.
        if isinstance(value, unicode):
            try:
                str_value = str(value)
            except UnicodeEncodeError:
                return value
        else:
            str_value = value

        try:
            return pickle.loads(str_value)
        except ValueError:
            # If pickle could not load from string it means that it's Python
            # string saved to PickleField.
            return value
