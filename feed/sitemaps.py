from django.contrib.sitemaps import Sitemap
from django.urls import reverse
from .models import Event
from django.conf import settings


class EventSitemap(Sitemap):
    changefreq = "weekly"
    priority = 0.6
    protocol = "http" if settings.DEBUG else "https"

    def items(self):
        return Event.objects.all()

    def lastmod(self, obj):
        return obj.created_at

    def location(self, obj):
        return "/event/%s" % (obj.id)


class StaticFeedSitemap(Sitemap):
    changefreq = "monthly"
    priority = 0.9
    protocol = "http" if settings.DEBUG else "https"

    def items(self):
        return [
            "feed-home",
            "login",
            "register",
            "password_reset",
            "events",
            "entrepreneurs",
        ]

    def location(self, item):
        return reverse(item)
