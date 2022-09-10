from django.contrib import admin
from feed.models import Event, Comment

admin.site.register(Event)

@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('event', 'user', 'content', 'created_at')
    list_filter = ('event', 'created_at')
    search_fields = ('user', 'content')