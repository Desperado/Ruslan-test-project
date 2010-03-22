#!/usr/bin/python
# -*- coding: utf-8 -*-
# mydata/views.py
""" Mydata views page """

from forms import ProfileForm
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from models import Mybio


@login_required
def contact(request):
    '''
    get contact page
    @param request:
    '''

    profile = get_object_or_404(Mybio, 
                                first_name='Ruslan', )
                               
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile = profile_form.save()
            
    if request.method == "GET":
        profile_form = ProfileForm(instance=profile)

    
    return render_to_response("accounts/profile.html", {
                           "profile_form": profile_form,
                           })

