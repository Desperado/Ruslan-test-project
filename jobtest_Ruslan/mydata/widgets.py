#!/usr/bin/python
# -*- coding: utf-8 -*-
# mydata/widgets.py

'''Widget Form'''

from django import forms
from django.conf import settings

class DateTimeWidget(forms.TextInput):
    '''Display calendar from http://code.google.com/p/dyndatetime/'''
    class Media:
        js = (
		'%s/js/jquery-1.4.2.min.js' % settings.MEDIA_PREFIX,
             	'%s/datepicker/datepicker.js' % settings.MEDIA_PREFIX,
        )
        css = {'all': (
                '%s/datepicker/css/datepicker.css' % settings.MEDIA_PREFIX,
        )}
  
    def __init__(self, attrs={}):
        super(DateTimeWidget, self).__init__(
            attrs={'class': 'dateField', 'size': '10'}
        )
