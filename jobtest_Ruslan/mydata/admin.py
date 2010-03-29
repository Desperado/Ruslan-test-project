from django.contrib import admin
from models import Mybio

class MybioAdmin(admin.ModelAdmin):
    list_display = ("first_name", "last_name", "bio", "contacts", "date_of_birth", )

admin.site.register(Mybio, MybioAdmin)
