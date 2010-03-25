#!/usr/bin/python
# -*- coding: UTF8 -*-

from django.conf.urls.defaults import *
from mydata.views import contact
from django.conf import settings
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
        url(r'^accounts/login/$', 'django.contrib.auth.views.login',\
                 {'template_name': 'registration/login.html'}, name="auth", ),
        (r'^accounts/logout/$', 'django.contrib.auth.views.logout',\
                 {'template_name': 'registration/logout.html'}),
        (r'^accounts/profile/$', contact),
        (r'^admin/doc/', include('django.contrib.admindocs.urls')),
        (r'^admin/', include(admin.site.urls)),

)

if settings.DEBUG:
    urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

)
