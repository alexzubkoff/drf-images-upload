from django.contrib.auth.models import AbstractUser
from django.conf import settings
from django.db import models


class CustomUser(AbstractUser):
    pass


class Profile(models.Model):

    class Plan(models.TextChoices):
        BASIC = 'BA', 'Basic'
        PREMIUM = 'PR', 'Premium'
        ENTERPRISE = 'EN', 'Enterprise'

    user = models.OneToOneField(
        settings.AUTH_USER_MODEL,
        on_delete=models.CASCADE
    )
    plan = models.CharField(
        max_length=3,
        choices=Plan.choices,
        default=Plan.BASIC
    )

    def __str__(self):
        return f'Profile of {self.user.username}'
