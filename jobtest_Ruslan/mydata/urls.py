from django.conf.urls.defaults import url, patterns, include

from jobtest_Ruslan.mydata.views import contact, contact_edit, contact_view

urlpatterns = patterns('',
    url(r'^(?P<first_name>\w+)_(?P<last_name>\w+)/$', 
        contact, 
        name='profile'),
    url(r'^edit/(?P<first_name>\w+)_(?P<last_name>\w+)/$', 
        contact_edit, 
        name='profile-edit'),
    url(r'^view/(?P<first_name>\w+)_(?P<last_name>\w+)/$', 
        contact_view, 
        name='profile-view'),
    )
