from django.conf.urls.defaults import patterns, url, include
from django.views.generic import RedirectView
from venuesbasedleantest.views import landing, instagram_poll, college, suggest_a_college


urlpatterns = patterns(
    '',
    url(r'instagram_poll$', instagram_poll, name="venuesbasedleantest_instagram_poll"),

    url(r'college/(?P<college_name>\w+)$', college, name="venuesbasedleantest_college"),

    url(r'suggest-a-college$', suggest_a_college, name="venuesbasedleantest_suggest_a_college"),


    url(r'fdu$', RedirectView.as_view(url="/college/fdu"), name="venuesbasedleantest_fdu"),
    url(r'msu$', RedirectView.as_view(url="/college/msu"), name="venuesbasedleantest_msu"),

    url(r'', landing, name='venuesbasedleantest_landing'),
)
