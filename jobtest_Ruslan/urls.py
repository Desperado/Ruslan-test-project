from django.conf.urls.defaults import *
from jobtest_Ruslan.views import main_page 
from jobtest_Ruslan.books import views


from django.contrib.auth.views import login, logout

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
	
	
	#('^$', main_page),

        url(r'^accounts/login/$', 'django.contrib.auth.views.login', name="auth"),
        #(r'^accounts/login/$', login),
        (r'^search-form/$', views.search_form),
        (r'^search/$', views.search),


        (r'^accounts/logout/$', logout),
        (r'^accounts/profile/$', main_page),





    # Example:
    # (r'^jobtest_Ruslan/', include('jobtest_Ruslan.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
     (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
     (r'^admin/', include(admin.site.urls)),
)
