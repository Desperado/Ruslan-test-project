#!/usr/bin/python
# -*- coding: UTF8 -*-
# views.py
""" Views page """

from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse


def index(request):
    return HttpResponseRedirect(reverse("profile-view",
                                        kwargs={"first_name": "Ruslan",
                                                "last_name": "Strazhnyk"}))
