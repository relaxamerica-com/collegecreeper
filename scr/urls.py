from django.conf.urls.defaults import patterns, url, include
from django.contrib import admin

admin.autodiscover()

urlpatterns = patterns(
    '',
    url(r'^djangoadmin/', include(admin.site.urls)),
    url(r'', include('venuesbasedleantest.urls')),
)
