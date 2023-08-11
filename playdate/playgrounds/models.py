from enum import Enum

from django.core.validators import MinLengthValidator
from django.db import models
from django.urls import reverse
from django.contrib.auth import get_user_model
from django.utils.text import slugify

UserModel = get_user_model()


class ChoicesMixinWithModifiedDisplay(Enum):
    @classmethod
    def choices(cls):
        return [(choice.value, choice.name.replace("_", " ")) for choice in cls]

    def _generate_next_value_(name, start, count, last_values):
        return name.replace("_", " ")


class Availability(ChoicesMixinWithModifiedDisplay, Enum):
    FREE = 1
    PAID = 2


class Country(ChoicesMixinWithModifiedDisplay, Enum):
    ALBANIA = 1
    ANDORRA = 2
    AUSTRIA = 3
    BELARUS = 4
    BELGIUM = 5
    BOSNIA_AND_HERZEGOVINA = 6
    BULGARIA = 7
    CROATIA = 8
    CYPRUS = 9
    CZECH_REPUBLIC = 10
    DENMARK = 11
    ESTONIA = 12
    FINLAND = 13
    FRANCE = 14
    GERMANY = 15
    GREECE = 16
    HUNGARY = 17
    ICELAND = 18
    IRELAND = 19
    ITALY = 20
    KOSOVO = 21
    LATVIA = 22
    LIECHTENSTEIN = 23
    LITHUANIA = 24
    LUXEMBOURG = 25
    MALTA = 26
    MOLDOVA = 27
    MONACO = 28
    MONTENEGRO = 29
    NETHERLANDS = 30
    NORTH_MACEDONIA = 31
    NORWAY = 32
    POLAND = 33
    PORTUGAL = 34
    ROMANIA = 35
    RUSSIA = 36
    SAN_MARINO = 37
    SERBIA = 38
    SLOVAKIA = 39
    SLOVENIA = 40
    SPAIN = 41
    SWEDEN = 42
    SWITZERLAND = 43
    UKRAINE = 44
    UNITED_KINGDOM = 45
    VATICAN_CITY = 46


class Rating(ChoicesMixinWithModifiedDisplay, Enum):
    VERY_POOR = 1
    POOR = 2
    MEDIOCRE = 3
    GOOD = 4
    VERY_GOOD = 5
    PERFECT = 6


class Playground(models.Model):
    NAME_MAX_LENGTH = 50
    NAME_MIN_LENGTH = 2
    ADDRESS_MAX_LENGTH = 200
    ADDRESS_MIN_LENGTH = 3
    CITY_MAX_LENGTH = 100

    name = models.CharField(
        max_length=NAME_MAX_LENGTH,
        validators=(MinLengthValidator(NAME_MIN_LENGTH),),
    )
    description = models.TextField()
    address = models.CharField(
        max_length=ADDRESS_MAX_LENGTH,
        validators=(MinLengthValidator(ADDRESS_MIN_LENGTH),),
    )
    city = models.CharField(
        max_length=CITY_MAX_LENGTH
    )
    country = models.IntegerField(
        choices=Country.choices(),
    )
    latitude = models.FloatField(
        blank=True,
        null=True,
    )
    longitude = models.FloatField(
        blank=True,
        null=True,
    )
    availability = models.IntegerField(
        choices=Availability.choices(),
    )
    price = models.FloatField(
        blank=True,
        null=True,
    )
    website = models.URLField(
        unique=True,
        blank=True,
        null=True,
    )
    rating = models.IntegerField(
        choices=Rating.choices(),
        blank=True,
        null=True,
    )
    slug = models.SlugField(
        unique=True,
        blank=True,
        null=True,
    )
    created_at = models.DateTimeField(
        auto_now_add=True
    )
    owner = models.ForeignKey(
        UserModel,
        on_delete=models.CASCADE,
        related_name="playgrounds"
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.name}-{self.id}")

        return super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.name} - {self.pk}"

    def get_absolute_url(self):
        return reverse("playground details", args=[str(self.pk)])
