from django.contrib import admin

from entrepreneurs.models import Entrepreneur, EntrepreneurCategory, EntrepreneurStatus

admin.site.register(Entrepreneur)
admin.site.register(EntrepreneurCategory)
admin.site.register(EntrepreneurStatus)
