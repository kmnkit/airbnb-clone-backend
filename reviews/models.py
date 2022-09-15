from common.models import CommonModel
from django.db import models
from django.conf import settings
from django.core.validators import MinValueValidator, MaxValueValidator


class Review(CommonModel):
    """Review from a User to a Room or Experience"""

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        on_delete=models.DO_NOTHING,
    )
    room = models.ForeignKey(
        "rooms.Room",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    experience = models.ForeignKey(
        "experiences.Experience",
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
    )
    payload = models.TextField()
    rating = models.PositiveIntegerField(
        validators=[
            MaxValueValidator(5),
            MinValueValidator(1),
        ],
    )

    def __str__(self):
        return f"{self.user.name}'s Review"
