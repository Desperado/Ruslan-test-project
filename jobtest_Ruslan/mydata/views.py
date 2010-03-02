from django.core import management
#from django.core.context_processors import csrf
from mydata.forms import ProfileForm
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from mydata.models import Mybio


@login_required
def contact(request):
    '''
    get contact page
    @param request:
    @param first_name: Profile.first_name
    @param last_name: Profile.last_name
    '''
    management.call_command('loaddata', 'initial_data.json', verbosity=0)
    profile = get_object_or_404(Mybio, 
                                first_name='Ruslan', )
                               
    if request.method == "POST":
        profile_form = ProfileForm(request.POST, instance=profile)
    
    if request.method == "GET":
        profile_form = ProfileForm(instance=profile)
    
    return render_to_response("accounts/profile.html", {
                           "profile_form": profile_form,
                           })

