from django.conf.urls.defaults import *
from jobtest_Ruslan.views import current_datetime, main_page

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = patterns('',
	
	('^time/$', current_datetime),
	('^$', main_page),

	#(r'^time/plus/(\d{1,2})/$', hours_ahead),


    # Example:
    # (r'^jobtest_Ruslan/', include('jobtest_Ruslan.foo.urls')),

    # Uncomment the admin/doc line below and add 'django.contrib.admindocs' 
    # to INSTALLED_APPS to enable admin documentation:
    # (r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # (r'^admin/', include(admin.site.urls)),
)
