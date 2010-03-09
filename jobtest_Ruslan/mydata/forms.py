
from models import Mybio
from django import forms
from django.conf import settings
from django.contrib.admin.options import TabularInline
from django.contrib.admin import widgets
from widgets import DateTimeWidget 


class ProfileForm(forms.ModelForm):
    first_name = forms.CharField(max_length=100)
    date_of_birth = forms.DateField(widget=DateTimeWidget)
    last_name = forms.CharField(max_length=100)
    class Meta:
        model = Mybio
        widgets = {
            'date_of_birth': DateTimeWidget(),
        }

class FormReverse(forms.ModelForm):
    pass
 
