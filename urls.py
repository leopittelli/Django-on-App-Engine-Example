from django.conf.urls import patterns, url, include
from django.views.generic.base import TemplateView, RedirectView
from main.views import cached_javascript_catalog

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

js_info_dict = {
    'packages': ('main',),
}

handler500 = 'djangotoolbox.errorviews.server_error'

urlpatterns = patterns('',
    ('^_ah/warmup$', 'djangoappengine.views.warmup'),
    url(r'^jsi18n/$', cached_javascript_catalog, js_info_dict, name='cached_javascript_catalog'),
    (r'^i18n/', include('django.conf.urls.i18n')),
    url(r'^admin/', include(admin.site.urls)),
    (r'^summernote/', include('django_summernote.urls')),

    (r'^favicon\.ico$', RedirectView.as_view(url='/static/global/favicon.ico')),
    (r'^robots\.txt$', TemplateView.as_view(template_name='main/robots.txt', content_type='text/plain')),
    (r'^sitemap\.xml$', TemplateView.as_view(template_name='main/sitemap.xml', content_type='application/xml')),

    url('', include('main.urls', namespace='main')),
)
