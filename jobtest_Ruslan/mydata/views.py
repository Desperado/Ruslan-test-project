#!/usr/bin/python
# -*- coding: utf-8 -*-
# mydata/views.py
""" Mydata views page """

from jobtest_Ruslan.shortcuts import render_to
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.utils.translation import ugettext as _
from django.core.urlresolvers import reverse
from forms import ProfileForm
from models import Mybio


def contact(*args, **kwargs):
    '''
    Contact view dispatcher
    @param request:
    @param first_name:
    @param last_name:
    '''
    if args[0].user.is_authenticated():
        return contact_edit(*args, **kwargs)
    else:
        return contact_view(*args, **kwargs)


@login_required
@render_to("accounts/profile_edit.html")
def contact_edit(request, first_name, last_name):
    '''
    get contact page
    @param request:
    @param first_name: Profile.first_name
    @param last_name: Profile.last_name
    '''
    profile = get_object_or_404(Mybio, 
                                pk=1)

    if request.method == "POST":
        profile_form = ProfileForm(request.POST, instance=profile)
        if profile_form.is_valid():
            profile = profile_form.save()

    if request.method == "GET":
        profile_form = ProfileForm(instance=profile)

    return {
            "profile": profile,
            "profile_form": profile_form,
            "utility_links": ((reverse('profile-view',
                                      kwargs={"first_name": profile.first_name,
                                              "last_name": profile.last_name, }), 
                              _("View profile"),
                              {}),)}

@render_to("accounts/profile_view.html")
def contact_view(request, first_name, last_name):
    profile = get_object_or_404(Mybio, 
                                first_name=first_name, 
                                last_name=last_name)
    return {"profile": profile,
            "utility_links": ((reverse('profile-edit',
                                      kwargs={"first_name": profile.first_name,
                                              "last_name": profile.last_name, }),
                              _("Edit profile"),
                              {}),)}
