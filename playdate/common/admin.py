from django.contrib import admin
from .models import Comment, Like


@admin.register(Comment)
class CommentAdmin(admin.ModelAdmin):
    list_display = ("user", "id", "date_time_of_publication", "to_photo")


@admin.register(Like)
class LikeAdmin(admin.ModelAdmin):
    list_display = ("user", "to_photo")
