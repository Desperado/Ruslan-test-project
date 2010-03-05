from django.core import management
from mydata.forms import ProfileForm
from django.shortcuts import render_to_response, get_object_or_404
from django.contrib.auth.decorators import login_required
from mydata.models import Mybio
from django.forms.models import inlineformset_factory


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

