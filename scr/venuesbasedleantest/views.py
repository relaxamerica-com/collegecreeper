from django.shortcuts import render


def landing(request):
    return render(request, 'venuesbasedleantest/base.html')