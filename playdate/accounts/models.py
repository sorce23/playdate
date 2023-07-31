from enum import Enum

from django.core import validators
from django.db import models
from django.contrib.auth import models as auth_models


class ChoicesMixin:
    @classmethod
    def choices(cls):
        return [(choice.value, choice.name) for choice in cls]


class ChoicesStringsMixin(ChoicesMixin):
    @classmethod
    def max_length(cls):
        return max(len(x.value) for x in cls) + 1


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
        default="profile_picture/person02.svg",
    )

    @property
    def full_name(self):
        if self.first_name or self.last_name:
            return f"{self.first_name} {self.last_name}"
        return self.username

    def save(self, *args, **kwargs):
        result = super().save(*args, **kwargs)

        return result
