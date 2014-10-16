from django.contrib import admin
from solo.admin import SingletonModelAdmin
from config.models import SiteConfiguration

admin.site.register(SiteConfiguration, SingletonModelAdmin)

# There is only one item in the table, you can get it this way:
from .models import SiteConfiguration
try:
    config = SiteConfiguration.objects.get()
except SiteConfiguration.DoesNotExist:
    config = SiteConfiguration.objects.create().save()