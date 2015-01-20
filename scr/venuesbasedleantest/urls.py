from django.conf.urls.defaults import patterns, url, include
from venuesbasedleantest.views import landing


urlpatterns = patterns(
    '',
    url(r'', landing, name='venuesbasedleantest_landing')
)
