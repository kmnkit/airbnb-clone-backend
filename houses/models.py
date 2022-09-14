from django.db import models
from django.conf import settings


class House(models.Model):
    name = models.CharField(max_length=140)
    price_per_night = models.PositiveIntegerField("요금", help_text="양수만 입력")
    address = models.CharField(max_length=140)
    description = models.TextField()
    pets_allowed = models.BooleanField(
        "애완동물 가능", default=True, help_text="이 집이 애완동물을 허가하는가?"
    )
    owner = models.ForeignKey(settings.AUTH_USER_MODEL, related_name="houses", on_delete=models.CASCADE)

    def __str__(self):
        return self.name
