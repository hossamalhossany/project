from django.contrib import admin
from .models import Login,Patient_data,registration_info
# Register your models here.

admin.site.register(Login)
admin.site.register(Patient_data)
admin.site.register(registration_info)

