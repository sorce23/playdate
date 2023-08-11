from django.contrib.auth import get_user_model
from django.db import models
from django.core.validators import MinLengthValidator
from django.urls import reverse

from .validators import image_size_validator_5mb

from playdate.playgrounds.models import Playground

UserModel = get_user_model()


class Photo(models.Model):
    DESCRIPTION_MAX_LENGTH = 300
    DESCRIPTION_MIN_LENGTH = 5
    LOCATION_MAX_LENGTH = 50

    playground_image = models.ImageField(
        blank=False,
        null=False,
        validators=(image_size_validator_5mb,),
        upload_to="playground_photos",
    )
    description = models.TextField(
        max_length=DESCRIPTION_MAX_LENGTH,
        validators=(MinLengthValidator(DESCRIPTION_MIN_LENGTH),),
        blank=True,
        null=True,
    )
    location = models.CharField(
        max_length=LOCATION_MAX_LENGTH,
        blank=True,
        null=True,
    )
    playground = models.ForeignKey(
        Playground,
        on_delete=models.CASCADE,
        blank=True,
        related_name="photos",
    )
    date_of_publication = models.DateField(auto_now=True)

    user = models.ForeignKey(
        UserModel,
        on_delete=models.DO_NOTHING,
    )

    def __str__(self):
        return f"{self.pk} - {self.playground_image}"

    def get_absolute_url(self):
        return reverse("photo details", args=[str(self.pk)])
