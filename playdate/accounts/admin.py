from django.contrib import admin
from django.contrib.auth import get_user_model

UserModel = get_user_model()


@admin.register(UserModel)
class UserModelAdmin(admin.ModelAdmin):
    list_display = ("username", "email", "first_name", "last_name", "date_joined")
    ordering = ("date_joined",)
    list_filter = ("groups", "gender",)
