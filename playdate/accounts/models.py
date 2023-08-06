from enum import Enum

from django.core import validators
from django.core.files.storage import default_storage
from django.db import models
from django.contrib.auth import models as auth_models
from django.templatetags.static import static


class ChoicesMixin:
    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]


class Gender(ChoicesMixin, Enum):
    MALE = 1
    FEMALE = 2
    DO_NOT_SHOW = 3


class PlaydateUser(auth_models.AbstractUser):
    FIRST_NAME_MIN_LENGTH = 2
    FIRST_NAME_MAX_LENGTH = 30
    LAST_NAME_MIN_LENGTH = 2
    LAST_NAME_MAX_LENGTH = 30

    first_name = models.CharField(
        max_length=FIRST_NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(FIRST_NAME_MIN_LENGTH),
            validators.RegexValidator(r"^[A-Z][A-z]*$", "Your name must start with a capital letter!"),
        ),
        null=True,
        blank=True,
    )

    last_name = models.CharField(
        max_length=LAST_NAME_MAX_LENGTH,
        validators=(
            validators.MinLengthValidator(LAST_NAME_MIN_LENGTH),
            validators.RegexValidator(r"^[A-Z][A-z]*$", "Your name must start with a capital letter!"),
        ),
        null=True,
        blank=True,
    )

    email = models.EmailField(
        unique=True,
    )

    gender = models.IntegerField(
        choices=Gender.choices(),
        default=Gender.DO_NOT_SHOW.value,
    )

    profile_picture = models.ImageField(
        upload_to="profile_picture/",
        null=True,
        blank=True,
    )

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username

    def save(self, *args, **kwargs):
        if self.pk is not None:
            existing_object = PlaydateUser.objects.get(pk=self.pk)

            if existing_object.profile_picture != self.profile_picture:
                self.delete_old_profile_picture(existing_object.profile_picture)

        result = super().save(*args, **kwargs)

        return result

    def delete_old_profile_picture(self, old_file):
        if old_file and default_storage.exists(old_file.name):
            old_file.delete()

    def clean(self):
        super().clean()
