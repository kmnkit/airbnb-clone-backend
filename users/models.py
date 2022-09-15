from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    class GenderChoices(models.TextChoices):
        MALE = ("male", "Male")
        FEMALE = ("female", "Female")

    class LanguageChoices(models.TextChoices):
        KR = ("kr", "Korean")
        EN = ("en", "English")
        JP = ("jp", "Japanese")

    class CurrencyChoices(models.TextChoices):
        WON = "won", "Korean Won"
        USD = "usd", "Dollar"
        JPY = "jpy", "Japanese Yen"

    first_name = models.CharField(
        max_length=150,
        editable=False,
    )
    last_name = models.CharField(
        max_length=150,
        editable=False,
    )
    avatar = models.ImageField()
    name = models.CharField(
        "이름",
        max_length=140,
    )
    is_host = models.BooleanField(
        default=False,
    )
    gender = models.CharField(
        max_length=10,
        choices=GenderChoices.choices,
    )
    language = models.CharField(
        max_length=2,
        choices=LanguageChoices.choices,
    )
    currency = models.CharField(
        max_length=5,
        choices=CurrencyChoices.choices,
    )

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "유저"
        verbose_name_plural = "유저들"
