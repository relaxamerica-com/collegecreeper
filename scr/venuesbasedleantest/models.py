import json
import urllib2
from django.conf import settings
from django.db import models


class InstagramMedia(models.Model):
    college = models.CharField(max_length=255)
    instagram_id = models.CharField(max_length=255)
    distance = models.FloatField()
    type = models.CharField(max_length=255)
    caption = models.TextField()
    link = models.CharField(max_length=255)
    user = models.ForeignKey('InstagramUser')
    created_time = models.CharField(max_length=255)

    def get_thumbnail(self):
        return self.instagrammediaitem_set.all()[0].url

    @classmethod
    def get_new_for_college(cls, college):
        college_data = settings.COLLEGES.get(college)
        if not college_data:
            return None
        url = "https://api.instagram.com/v1/media/search?lat=%s&lng=%s&access_token=%s" % (
            college_data['latitude'],
            college_data['longitude'],
            settings.INSTAGRAM_ACCESS_TOKEN)
        if InstagramMedia.objects.filter(college=college).count():
            last_object = InstagramMedia.objects.filter(college=college).order_by('-created_time')[0]
            url += "&min_timestamp=%s" % last_object.created_time
        response = urllib2.urlopen(url)
        data = json.load(response)
        for d in data.get('data', []):
            cls.from_api_return(college, d)

    @classmethod
    def from_api_return(cls, college, data):
        instagram_id = data.get('id')
        if not instagram_id:
            return None

        user_instagram_id = data.get('user', {}).get('id')
        if not user_instagram_id:
            return None

        type = data.get('type')
        if not type:
            return None

        user, created = InstagramUser.objects.get_or_create(
            instagram_id=user_instagram_id,
            defaults={
                'username': data.get('user', {}).get('username'),
                'profile_picture': data.get('user', {}).get('profile_picture')})

        media, created = InstagramMedia.objects.get_or_create(
            college=college,
            instagram_id=instagram_id,
            defaults={
                'distance': data.get('distance', 0),
                'type': type,
                'caption': (data.get('caption') or {}).get('text') or '',
                'link': data.get('link', ''),
                'user': user,
                'created_time': data.get('created_time')})

        for key, value in data.get('%ss' % type, {}).items():
            media_item, created = InstagramMediaItem.objects.get_or_create(
                media=media,
                url=value.get('url'),
                defaults={
                    'type': key,
                    'width': value.get('width'),
                    'height': value.get('height')})

        return media


class InstagramMediaItem(models.Model):
    media = models.ForeignKey('InstagramMedia')
    url = models.CharField(max_length=1023)
    type = models.CharField(max_length=255)
    width = models.IntegerField()
    height = models.IntegerField()


class InstagramUser(models.Model):
    instagram_id = models.CharField(max_length=255)
    username = models.CharField(max_length=255)
    profile_picture = models.CharField(max_length=1023)