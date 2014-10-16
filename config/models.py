from django.db import models
from solo.models import SingletonModel

class SiteConfiguration(SingletonModel):
    site_name = models.CharField(max_length=255, default='Site Name')
    site_description = models.TextField(max_length=1000, default='Site Description')
    google_oauth2_key = models.CharField(max_length=255)
    google_oauth2_secret = models.CharField(max_length=255)
    google_api_key = models.CharField(max_length=255)
    analytics_code = models.TextField(max_length=2000)

    def __unicode__(self):
        return u"Site Configuration"

    class Meta:
        verbose_name = "Site Configuration"
        verbose_name_plural = "Site Configuration"