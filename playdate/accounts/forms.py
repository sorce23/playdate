from django import forms
from django.contrib.auth import forms as auth_forms, get_user_model

UserModel = get_user_model()


class LoginUserForm(auth_forms.AuthenticationForm):
    username = forms.CharField()


class RegisterUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        result = super().save(commit)
        return result
