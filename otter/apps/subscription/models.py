from django.db import models

from common.models import BaseModel

from apps.organization.models import Organization

from .choices import SubscriptionType


class SubscriptionPlan(BaseModel):
    subscription_type = models.CharField(
        max_length=30, choices=SubscriptionType.choices, default=SubscriptionType.FREE
    )
    event_limit = models.PositiveIntegerField(blank=True, null=True)
    invitation_limit = models.PositiveIntegerField(blank=True, null=True)
    description = models.TextField(blank=True, null=True)

    # FK
    organization = models.ForeignKey(
        Organization,
        on_delete=models.CASCADE,
        related_name="organizations_subscription_plan",
    )

    class Meta:
        verbose_name = "Subscription Plan"
        verbose_name_plural = "Subscription Plans"

    def __str__(self):
        return f"UID: {self.uid} | Name: {self.subscription_type}"

    def is_event_unlimited(self):
        return self.event_limit is None

    def is_invitation_unlimited(self):
        return self.invitation_limit is None
