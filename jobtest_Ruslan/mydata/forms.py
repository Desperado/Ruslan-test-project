#from models import Contact, BiographyEntry, Profile
from mydata.models import Mybio
from django.forms import ModelForm
from django.contrib.admin.options import TabularInline


class ProfileForm(ModelForm):
    class Meta:
        model = Mybio

