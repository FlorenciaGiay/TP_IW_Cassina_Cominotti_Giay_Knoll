from django.contrib import admin

# Register your models here.
from entrepreneurs.models import EntrepreneurProfile#, EntrepreneurStatus, EntrepreneurCategory

@admin.register(EntrepreneurProfile)
class AdminEntrepreneurProfile(admin.ModelAdmin):
    list_display = ('entrepreneurship_name', 'entrepreneurship_email')