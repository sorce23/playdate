from django.contrib import admin
from .models import Photo


@admin.register(Photo)
class PhotoAdmin(admin.ModelAdmin):
    list_display = ("id", "playground", "date_of_publication")
    list_filter = ("playground", "user")
