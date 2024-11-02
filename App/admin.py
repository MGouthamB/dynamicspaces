from django.contrib import admin
from .models import *
# Register your models here.
admin.site.site_header="Groziit Dynamic Spaces"
admin.site.register(Jobs)
admin.site.register(Profiles)
admin.site.register(JobApplication)
admin.site.register(FormData)
admin.site.register(Content)
admin.site.register(Integration)
admin.site.register(AccountIntegrations)
admin.site.register(IntegrationJobApplication)
