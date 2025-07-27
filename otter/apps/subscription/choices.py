from django.db import models


class SubscriptionType(models.TextChoices):
    FREE = "FREE", "Free"
    PREMIUM = "PREMIUM", "Premium"
