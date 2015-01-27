import json
import urllib2
from google.appengine.api.datastore_types import IM

from django.core.management.base import BaseCommand
from django.conf import settings
from venuesbasedleantest.models import *


class Command(BaseCommand):
    def handle(self, *args, **options):
        self.stdout.writelines(['Importing\n'])
        InstagramMedia.get_new_for_college('london')
        self.stdout.writelines([
            'Import finishedn\n',
            '%s InstagramMedia objects\n' % InstagramMedia.objects.count(),
            '%s InstagramMediaItem objects\n' % InstagramMediaItem.objects.count(),
            '%s InstagramUser objects\n' % InstagramUser.objects.count(),
            'Done\n'])
