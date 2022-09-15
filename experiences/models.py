from common.models import CommonModel
from django.conf import settings
from django.db import models
from django_countries.fields import CountryField

class Experience(CommonModel):
    """Experience Model Definition"""
    country = CountryField()
    city = models.CharField(
        max_length=80,
        default="서울",
    )
    name = models.CharField(max_length=250,)
    host = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,)
    price = models.PositiveIntegerField()
    address = models.CharField(max_length=250,)
    start = models.TimeField()
    end = models.TimeField()
    perks = models.ManyToManyField("Perk")

class Perk(CommonModel):
    """What is included on an Experience"""
    name = models.CharField(max_length=30,)
    details = models.CharField(max_length=250,)
    description = models.TextField()


