from django.conf.urls.defaults import *
from jobtest_Ruslan.books.views import search
from jobtest_Ruslan.mydata.views import contact
from jobtest_Ruslan.contact import views
from django.conf import settings


from django.contrib.auth.views import login, logout

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	
	
	#('^$', main_page),

        url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="auth"),
        (r'^search/$', search),
        (r'^accounts/logout/$', 'django.contrib.auth.views.logout', {'next_page': '/accounts/login/'}),
        (r'^accounts/profile/$', contact),
        (r'^contact/$', views.contact),
        (r'^admin/doc/', include('django.contrib.admindocs.urls')),
        (r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
    urlpatterns += patterns('',
    (r'^media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),

)

