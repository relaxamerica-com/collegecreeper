from django.core.management.base import BaseCommand
from venuesbasedleantest.models import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        InstagramMediaItem.objects.all().delete()
        InstagramUser.objects.all().delete()
        InstagramMedia.objects.all().delete()