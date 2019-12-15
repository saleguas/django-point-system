from django.contrib.sitemaps import Sitemap

from .models import Student, MeetingKey
from django.urls import reverse

class StaticViewSitemap(Sitemap):
    priority = 0.9
    changeFreq = 'weekly'

    def items(self):
        return ['gallery', 'meetings', 'main', 'points:list', 'points:point-entry-form']

    def location(self, item):
        return reverse(item)

class StudentSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(sef):
        return Student.objects.all()



class MeetingEntryMap(Sitemap):
    changefreq = "weekly"
    priority = 0.5

    def items(sef):
        return MeetingKey.objects.all()
