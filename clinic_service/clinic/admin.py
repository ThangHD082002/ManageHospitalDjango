from django.contrib import admin
from .models import TypeClinic, Clinic, Bed
# Register your models here.

admin.site.register(TypeClinic)
admin.site.register(Clinic)
admin.site.register(Bed)