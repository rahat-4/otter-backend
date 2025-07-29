from django.db import models


class CampaignType(models.TextChoices):
    SMS = "SMS", "SMS"
    WHATSAPP = "WHATSAPP", "WhatsApp"


class GuestCategory(models.TextChoices):
    SOLO_GUESTS = "SOLO_GUESTS", "Solo Guests (Standard General)"
    COUPLES_INVITED = "COUPLES_INVITED", "+1/Couples Invited"
    MEAL_OR_PREFERENCE_REQUIRED = (
        "MEAL_OR_PREFERENCE_REQUIRED",
        "Meal/Preference required",
    )
    GROUPS = "GROUPS", "Groups"
    VIP_OR_PRIORITY_GUESTS = "VIP_OR_PRIORITY_GUESTS", "VIP/Priority Guests"
    KIDS_INCLUDED_OR_FAMILY = "KIDS_INCLUDED_OR_FAMILY", "Kids Included/Family"
