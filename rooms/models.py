from common.models import CommonModel
from django.db import models
from django.conf import settings
from django_countries.fields import CountryField


class Room(CommonModel):
    class RoomKindChoices(models.TextChoices):
        ENTIRE_PLACE = "entire_place", "Entire Place"
        PRIVATE_ROOM = "private_room", "Private Room"
        SHARED_ROOM = "shared_room", "Shared Room"

    name = models.CharField(max_length=180, default="")
    country = CountryField()
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    price = models.PositiveIntegerField()
    rooms = models.PositiveIntegerField()
    toilets = models.PositiveIntegerField()
    description = models.TextField()
    address = models.CharField(
        max_length=250,
    )
    pet_friendly = models.BooleanField(
        default=True,
    )
    kind = models.CharField(
        max_length=20,
        choices=RoomKindChoices.choices,
    )
    owner = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE,
    )
    amenities = models.ManyToManyField(
        "Amenity",
        related_name="rooms",
    )
    category = models.ForeignKey(
        "categories.Category",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )

    def __str__(self):
        return f"{self.country} {self.city}에 있는 {self.name}"

    class Meta:
        verbose_name = "방"
        verbose_name_plural = "방들"


class Amenity(CommonModel):
    """Amenity Definition"""

    name = models.CharField(max_length=50)
    description = models.CharField(
        max_length=150,
        null=True,
        blank=True,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "어메니티"
        verbose_name_plural = "어메니티들"
