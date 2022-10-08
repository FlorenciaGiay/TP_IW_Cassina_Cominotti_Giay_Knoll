from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Entrepreneur
from django.conf import settings


class EntrepreneurSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6
    protocol = "http" if settings.DEBUG else "https"

    def items(self):
        return Entrepreneur.objects.all()

    def location(self, obj):
        return "/enterpreneur/%s" % (obj.id)
