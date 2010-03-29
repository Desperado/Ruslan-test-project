#!/usr/bin/python
# -*- coding: UTF8 -*-

from django.conf.urls.defaults import *
from django.conf import settings
from django.contrib import admin
from django.http import HttpResponseRedirect
from django.core.urlresolvers import reverse

admin.autodiscover()


def index(request):
    return HttpResponseRedirect(reverse("profile-view",
                                        kwargs={"first_name": "Ruslan",
                                                "last_name": "Strazhnyk"}))

urlpatterns = patterns('',
        url(r'^$', index, name="index"),
        url(r'^admin/', include(admin.site.urls)),
        url(r'^profile/', include("jobtest_Ruslan.mydata.urls")),
        url(r'^accounts/login/$', 'django.contrib.auth.views.login',\
           {'template_name': 'registration/login.html'}, name="login", ),
        url(r'^accounts/logout/$', 'django.contrib.auth.views.logout',\
           {'template_name': 'registration/logout.html'}, name="logout"),
        url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

)

if settings.DEBUG:
    urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

)
