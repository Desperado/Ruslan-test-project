#!/usr/bin/python
# -*- coding: utf-8 -*-
# context_proc/processor.py
""" Context processor """
from django.conf import settings
def cont_settings(request):
    """
    Get context settings from settings file
    """
    
    return {"settings": settings}
