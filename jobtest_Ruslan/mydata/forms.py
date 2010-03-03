#from models import Contact, BiographyEntry, Profile
from mydata.models import Mybio
from django import forms
from django.conf import settings
from django.contrib.admin.options import TabularInline
from django.contrib.admin.widgets import AdminDateWidget

class DateTimePickerWidget(forms.DateInput):
    class Media:
        css = css = {"all":('%s/css/rfnet.css'%settings.MEDIA_PREFIX,)}
        js = ('%s/js/datetimepicker_css.js'%settings.MEDIA_PREFIX)

class DatePickerForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super(DatePickerForm, self).__init__(*args, **kwargs)
        for field_name, field_class in self.fields.items():
            if issubclass(type(field_class), forms.DateField):
                field_class.widget = DateTimePickerWidget(attrs={'class': 'datepicker',
                                                             'autocomplete': 'off',}) 

class ProfileForm(DatePickerForm):
    class Meta:
        model = Mybio

