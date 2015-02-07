from django.conf.urls.defaults import patterns, url, include
from django.views.generic import RedirectView
from venuesbasedleantest.views import landing, instagram_poll, college


urlpatterns = patterns(
    '',
    url(r'instagram_poll$', instagram_poll, name="venuesbasedleantest_instagram_poll"),

    url(r'college/(?P<college_name>\w+)$', college, name="venuesbasedleantest_college"),


    url(r'fdu$', RedirectView.as_view(url="/college/fdu")),
    url(r'msu$', RedirectView.as_view(url="/college/msu")),

    url(r'', landing, name='venuesbasedleantest_landing'),
)
