from django.contrib import admin
from .models import Ad, Comment


@admin.register(Ad)
class AdAdmin(admin.ModelAdmin):
    list_display = ('title', 'price', 'created_at')
    search_fields = ('title', 'description')
    list_filter = ('created_at', 'price')


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ('ad', 'created_at')
    search_fields = ('text',)
    list_filter = ('created_at',)
