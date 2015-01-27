from django.core.paginator import Paginator, EmptyPage, InvalidPage
from django.http import HttpResponse, Http404
from django.shortcuts import render
from django.conf import settings

from venuesbasedleantest.models import InstagramMedia


def landing(request):
    return render(request, 'venuesbasedleantest/colleges.html')


def college(request, college_name):
    c = settings.COLLEGES.get(college_name)
    if not c:
        raise Http404
    instagram_media = InstagramMedia.objects.filter(college=college_name).all()
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

    return render(request, 'venuesbasedleantest/college.html', {"media": media})


def instagram_poll(request):
    for c in settings.COLLEGES:
        InstagramMedia.get_new_for_college(c)
    return HttpResponse("done")