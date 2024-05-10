from django.contrib import admin

# Register your models here.
from .models import Certificate, CertifyingInstitution, Profile, Project


admin.site.register(Profile)
admin.site.register(Project)
admin.site.register(CertifyingInstitution)
admin.site.register(Certificate)
