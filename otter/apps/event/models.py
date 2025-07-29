from django.db import models

from phonenumber_field.modelfields import PhoneNumberField

from common.models import BaseModel

from .choices import CampaignType, GuestCategory


class Event(BaseModel):
    title = models.CharField(max_length=255)
    start_date = models.DateField()
    start_time = models.TimeField()
    end_date = models.DateTimeField(blank=True, null=True)
    location = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    invitation_link = models.URLField(blank=True, null=True)

    # FK
    organization = models.ForeignKey(
        "organization.Organization",
        on_delete=models.CASCADE,
        related_name="organization_events",
    )

    def __str__(self):
        return self.title


class Campaign(BaseModel):
    name = models.CharField(unique=True, max_length=255)
    campaign_type = models.CharField(
        max_length=30, choices=CampaignType.choices, default=CampaignType.WHATSAPP
    )
    guests_category = models.CharField(max_length=30, choices=GuestCategory.choices)
    is_meal_choice = models.BooleanField(
        default=False, help_text="Dietary preferences or menu selection"
    )
    is_dietary_restrictions = models.BooleanField(
        default=False, help_text="Allergies and dietary requirements"
    )
    is_parking_needed = models.BooleanField(
        default=False, help_text="Whether guest needs parking"
    )
    is_accessibility_needed = models.BooleanField(
        default=False, help_text="Any accessibility accommodations"
    )
    is_accommodation_required = models.BooleanField(
        default=False, help_text="Hotel or lodging needs"
    )
    description = models.TextField(blank=True, null=True)

    # FK
    organization = models.ForeignKey(
        "organization.Organization",
        on_delete=models.CASCADE,
        related_name="organization_campaigns",
    )
    event = models.ForeignKey(
        "event.Event",
        on_delete=models.CASCADE,
        related_name="event_campaigns",
    )

    def __str__(self):
        return f"UID: {self.uid} | Title: {self.campaign_type}"


class Guest(BaseModel):
    name = models.CharField(max_length=255)
    phone = PhoneNumberField()

    # FK
    campaign = models.ForeignKey(
        "event.Campaign",
        on_delete=models.CASCADE,
        related_name="campaign_guests",
    )

    def __str__(self):
        return f"UID: {self.uid}"
