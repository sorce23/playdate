from django.contrib import admin
from .models import Playground


@admin.register(Playground)
class PlaygroundAdmin(admin.ModelAdmin):
    list_display = ("name", "country", "owner")
    list_filter = ("availability", "country")
