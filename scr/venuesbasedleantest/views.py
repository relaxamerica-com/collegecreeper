from django.core.mail import send_mail
from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.conf import settings
from venuesbasedleantest.forms import SuggestACollegeForm

from venuesbasedleantest.models import InstagramMedia


def landing(request):
    return render(request, 'venuesbasedleantest/colleges.html')


def college(request, college_name):
    c = settings.COLLEGES.get(college_name)
    if not c:
        raise Http404
    instagram_media = InstagramMedia.objects.filter(college=college_name).order_by('-created_time').all()[:45]
    paginator = Paginator(instagram_media, 9)  # Show 25 contacts per page

    # Make sure page request is an int. If not, deliver first page.
    try:
        page = int(request.GET.get('page', '1'))
    except ValueError:
        page = 1

    # If page request (9999) is out of range, deliver last page of results.
    try:
        media = paginator.page(page)
    except (EmptyPage, InvalidPage):
        media = paginator.page(paginator.num_pages)

    template_data = {"media": media, "college": c}
    return render(request, 'venuesbasedleantest/college.html', template_data)


def suggest_a_college(request):
    form = SuggestACollegeForm()
    template_data = {}
    if request.method == "POST":
        form = SuggestACollegeForm(request.POST)
        if form.is_valid():
            send_mail(
                'Message from college creeper',
                "NAME: %s,  EMAIL: %s,  COLLEGE: %s" % (
                    form.cleaned_data.get('name'),
                    form.cleaned_data.get('email'),
                    form.cleaned_data.get('college')),
                'no-reply@collegecreeper.com',
                ['mg@metalayer.com', 'dennis@relaxtax.com', 'david@spudder.com'],
                fail_silently=False)
            template_data['sent'] = True
    template_data['form'] = form
    return render(request, 'venuesbasedleantest/suggest_a_college.html', template_data)


def instagram_poll(request):
    if settings.INSTAGRAM['POLLING_ENABLED']:
        for c in settings.COLLEGES:
            InstagramMedia.get_new_for_college(c)
    return HttpResponse("done")