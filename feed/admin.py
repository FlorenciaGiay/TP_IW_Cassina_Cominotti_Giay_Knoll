from django.contrib import admin
from feed.models import Event, Comment, EventPetitionStatus, EventEntrepreneur

admin.site.register(Event)
admin.site.register(EventPetitionStatus)
admin.site.register(EventEntrepreneur)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'content', 'created_at')
    list_filter = ('event', 'created_at')
    search_fields = ('user', 'content')