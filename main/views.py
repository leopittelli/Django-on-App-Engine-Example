from django.shortcuts import render_to_response
from django.template.context import RequestContext
from settings import JAVASCRIPT_TRANSLATION_VERSION

def index(request):

    extra_context = {}

#     extra_context['id'] =

    return render_to_response('main/index.html',
                              extra_context,
                              context_instance=RequestContext(request))


from django.views.decorators.cache import cache_page
from django.views.i18n import javascript_catalog
# The value returned by get_version() must change when translations change.
@cache_page(86400, key_prefix='js18n-%s' % JAVASCRIPT_TRANSLATION_VERSION)
def cached_javascript_catalog(request, domain='djangojs', packages=None):
    return javascript_catalog(request, domain, packages)
