from django.db import models

from common.models import BaseModel


class Event(BaseModel):
    title = models.CharField(max_length=255)
    date = models.DateField()
    time = models.TimeField()
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
