from django.contrib import admin

from .models import Certificados
# Register your models here.

class CertificadosAdmin (admin.ModelAdmin):
    readonly_fields= ('created','updated')

admin.site.register(Certificados)