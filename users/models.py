from django.db import models
from django.contrib.auth.models import AbstractUser


class User(AbstractUser):
    first_name = models.CharField(max_length=150, editable=False)
    last_name = models.CharField(max_length=150, editable=False)
    name = models.CharField("이름", max_length=140)
    is_host = models.BooleanField(default=False)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name = "유저"
        verbose_name_plural = "유저들"
