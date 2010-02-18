from django.core import management
from django.core.context_processors import csrf

from django.shortcuts import render_to_response
from django.contrib.auth.decorators import login_required

from mydata.models import Mybio
import datetime

@login_required
def main_page(request):
     """
     Generates main page with bio data
     """
     management.call_command('loaddata', 'initial_data.json', verbosity=0)
     data = Mybio.objects.get(first_name = 'Ruslan')
     return render_to_response('accounts/profile.html', locals())




