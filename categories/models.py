from django.db import models
from common.models import CommonModel


class Category(CommonModel):
    """Room Or Experience Category Model Definition"""

    class CategoryKindChoices(models.TextChoices):
        ROOMS = "rooms", "Rooms"
        EXPERIENCES = "experiences", "Experiences"

    name = models.CharField(max_length=50)
    kind = models.CharField(max_length=15, choices=CategoryKindChoices.choices)

    def __str__(self):
        return f"{self.kind}: {self.name}"

    class Meta:
        verbose_name_plural = "여러 카테고리"
