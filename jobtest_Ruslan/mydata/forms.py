#!/usr/bin/python
# -*- coding: utf-8 -*-
# mydata/forms.py
""" Mydata forms page """

from models import Mybio
from django import forms
from widgets import DateTimeWidget
from django.conf import settings
from django.utils.datastructures import SortedDict


class ProfileForm(forms.ModelForm):
    """Profile form"""
    first_name = forms.CharField(max_length=100)
    date_of_birth = forms.DateField(widget=DateTimeWidget)
    last_name = forms.CharField(max_length=100)

    class Meta:
        model = Mybio
        widgets = {
            'date_of_birth': DateTimeWidget(),
        }


class FormReverse(forms.ModelForm):
    """Reversed form"""
    def __init__(self, *args, **kwargs):
        reverse = bool(kwargs.pop("reverse", False))
        super(FormReverse, self).__init__(*args, **kwargs)
        if reverse:
            fields_list = self.fields.items()
            fields_list.reverse()
            self.fields = SortedDict(fields_list)
